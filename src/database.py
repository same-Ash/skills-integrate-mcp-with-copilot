"""
Database connection and collection management
"""

from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from config import MONGODB_URL, MONGODB_DB

_client = None
_db = None


def connect_to_db():
    """
    Initialize MongoDB connection
    """
    global _client, _db
    try:
        _client = MongoClient(MONGODB_URL, serverSelectionTimeoutMS=5000)
        # Verify connection
        _client.admin.command('ismaster')
        _db = _client[MONGODB_DB]
        
        # Create indexes
        _db.activities.create_index("name", unique=True)
        
        print(f"✅ Connected to MongoDB: {MONGODB_DB}")
        return _db
    except ConnectionFailure as e:
        print(f"❌ Failed to connect to MongoDB: {e}")
        raise


def get_db():
    """
    Get database connection
    """
    if _db is None:
        connect_to_db()
    return _db


def close_db():
    """
    Close database connection
    """
    global _client
    if _client:
        _client.close()
        print("✅ Disconnected from MongoDB")


def get_activities_collection():
    """Get activities collection"""
    return get_db().activities


def get_participants_collection():
    """Get participants collection"""
    return get_db().participants
