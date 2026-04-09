# MongoDB Integration Guide

This project now uses MongoDB for persistent data storage instead of in-memory dictionaries.

## Setup

### 1. Install MongoDB Locally

**macOS (using Homebrew):**
```bash
brew tap mongodb/brew
brew install mongodb-community
brew services start mongodb-community
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt-get install -y mongodb
sudo systemctl start mongodb
```

**Windows:**
Download from [MongoDB Community Server](https://www.mongodb.com/try/download/community)

Or use Docker:
```bash
docker run -d -p 27017:27017 --name mongodb mongo
```

### 2. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 3. Set Up Environment Variables

Copy `.env.example` to `.env`:
```bash
cp .env.example .env
```

Edit `.env` if your MongoDB is not on the default localhost:27017:
```
MONGODB_URL=mongodb://localhost:27017
MONGODB_DB=mergington_school
PORT=8000
```

### 4. Seed the Database

Run the seed script to populate initial activities:
```bash
cd src
python seed_db.py
```

You should see output like:
```
✅ Connected to MongoDB: mergington_school
🧹 Cleared existing activities
✅ Inserted 9 activities
📋 Activities in database:
  - Chess Club: 2 participants
  - Programming Class: 2 participants
  ...
```

### 5. Run the Application

```bash
cd src
uvicorn app:app --reload --port 8000
```

The API will be available at `http://localhost:8000`

## Project Structure

```
src/
├── app.py          # Main FastAPI application
├── config.py       # Configuration settings
├── database.py     # Database connection and collections
├── models.py       # Pydantic models and schemas
├── seed_db.py      # Database seeding script
└── static/         # Frontend files
```

## API Endpoints

- `GET /` - Redirect to frontend
- `GET /activities` - Get all activities
- `POST /activities/{activity_name}/signup` - Sign up for activity
- `DELETE /activities/{activity_name}/unregister` - Unregister from activity

## Data Persistence

All activity and participant data is now persisted in MongoDB. The data will survive application restarts.

## Troubleshooting

### MongoDB Connection Error
If you get "Cannot connect to MongoDB":
- Ensure MongoDB is running: `docker ps` (for Docker) or check your system service
- Verify the MONGODB_URL in `.env` is correct
- Try connecting manually: `mongosh` or `mongo`

### Database Already Exists
- You can safely re-run `seed_db.py` - it clears old data first

### Port Already in Use
- Change the PORT in `.env` to an available port
