# oracle_lib.py
# Copyright 2026, Denis Rothman
# The Oracle Connection Manager
# -------------------------------------------------------------------------
# This module acts as the "Infrastructure Layer" for our Enterprise Agents.
# It abstracts away the complexity of Oracle Wallets, TNSNAMES, and 
# connection strings. 
#
# Instead of every agent managing its own connection (which is inefficient 
# and risky), they all request a cursor from this centralized manager.
#
# USAGE PATTERN:
# 1. Initialize: OracleManager.initialize(wallet_path, creds_path)
# 2. Get Cursor: with OracleManager.get_cursor() as cursor: ...
# -------------------------------------------------------------------------

import oracledb
import os
import logging
from contextlib import contextmanager

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - [OracleLib] - %(levelname)s - %(message)s')

class OracleManager:
    """
    A Singleton-style wrapper for Oracle Database connections.
    It manages the connection pool and handles secure wallet authentication.
    """
    _connection = None
    _creds = {}

    @classmethod
    def initialize(cls, creds_path=None, wallet_path=None):
        """
        Reads credentials and establishes the primary connection.
        This must be called once before any agent attempts to work.
        """
        logging.info("Initializing Oracle Connection Manager...")

        if not creds_path:
            # Default to the standard location used in the book's notebooks
            creds_path = "/content/drive/MyDrive/files/oracle/credentials.txt"
        
        if not wallet_path:
            wallet_path = "/content/drive/MyDrive/files/oracle"

        # 1. Load Credentials
        if not os.path.exists(creds_path):
            logging.error(f"Credentials file not found at {creds_path}")
            raise FileNotFoundError(f"Credentials file missing: {creds_path}")

        cls._creds = cls._read_key_value_file(creds_path)
        
        # 2. Connect
        try:
            cls._connection = oracledb.connect(
                user=cls._creds.get("user"),
                password=cls._creds.get("password"),
                dsn=cls._creds.get("dsn"),
                config_dir=wallet_path,
                wallet_location=wallet_path,
                wallet_password=cls._creds.get("wallet_password")
            )
            logging.info("✅ Secure connection to Oracle 23ai established.")
            
            # Simple heartbeat check
            with cls._connection.cursor() as cursor:
                cursor.execute("SELECT 'Heartbeat OK' FROM dual")
                result = cursor.fetchone()
                logging.info(f"   Database says: {result[0]}")

        except Exception as e:
            logging.error(f"Failed to connect to Oracle: {e}")
            raise e

    @classmethod
    @contextmanager
    def get_cursor(cls):
        """
        A context manager that yields a cursor.
        Ensures the cursor is closed after use, even if errors occur.
        
        Usage:
            with OracleManager.get_cursor() as cursor:
                cursor.execute("SELECT * ...")
        """
        if cls._connection is None:
            raise ConnectionError("OracleManager is not initialized. Call initialize() first.")
        
        cursor = cls._connection.cursor()
        try:
            yield cursor
            # Auto-commit can be dangerous in some contexts, but for RAG agents 
            # (which are mostly read-only or self-contained updates), it is often useful.
            # We explicitly commit here to save any log updates or inserts.
            cls._connection.commit()
        except Exception as e:
            cls._connection.rollback()
            logging.error(f"Database operation failed: {e}")
            raise e
        finally:
            cursor.close()

    @staticmethod
    def _read_key_value_file(path):
        """Helper to parse the standard credentials.txt format."""
        creds = {}
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                if "=" not in line:
                    continue
                k, v = line.split("=", 1)
                creds[k.strip()] = v.strip()
        return creds

    @classmethod
    def close(cls):
        """Closes the main connection cleanly."""
        if cls._connection:
            cls._connection.close()
            cls._connection = None
            logging.info("Oracle connection closed.")