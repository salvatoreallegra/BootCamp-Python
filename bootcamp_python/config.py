# -------------------------------------------------------
# config.py
# PURPOSE: Central place to load config (env vars, dotenv).
# -------------------------------------------------------
import os
from dotenv import load_dotenv

# Automatically load from .env (if present)
load_dotenv()

# Safe to use across project
API_KEY = os.getenv("API_KEY", "dev-fallback-key")
DB_CONN = os.getenv("DB_CONN", "sqlite:///:memory:")
