"""
Database configuration and connection setup
"""

import os
from dotenv import load_dotenv

load_dotenv()

MONGODB_URL = os.getenv("MONGODB_URL", "mongodb://localhost:27017")
MONGODB_DB = os.getenv("MONGODB_DB", "mergington_school")
PORT = int(os.getenv("PORT", 8000))
