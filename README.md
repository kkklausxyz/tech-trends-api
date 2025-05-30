# Tech Trends Explorer (Backend)

This is the backend API for **Tech Trends Explorer**, a web application that visualizes trending programming languages on GitHub. The API is built with Flask, retrieves data from a PostgreSQL database, and serves JSON responses to the frontend.

## 🌐 Live API

👉 [Visit the API](https://tech-trends-api-dymi.onrender.com/api)

## ⚙️ Tech Stack

- **Backend Framework**: [Flask](https://flask.palletsprojects.com/)
- **Database**: [PostgreSQL](https://www.postgresql.org/) hosted on [Supabase](https://supabase.com/)
- **Deployment**: [Render](https://render.com/)
- **ETL**: Python-based script fetching GitHub trending data

## 📡 API Endpoints

### 1. GET /api/language-distribution?since=period
Returns the most frequent languages appearing in GitHub Trending repositories.

Query Parameters:

since — One of daily, weekly, or monthly
Example:

```bash
curl https://your-api-url/api/language-distribution?since=weekly
```

Response:
```json
{
  "code": 200,
  "message": "success",
  "data": [
    { "language": "Python", "count": 125, "color": "#3572A5" },
    { "language": "JavaScript", "count": 103, "color": "#f1e05a" }
  ]
}
```

### 2. GET /api/keywords?since=period
Returns the most common keywords extracted from trending repository descriptions.

Query Parameters:

since — One of daily, weekly, or monthly
Example:

```bash
curl https://your-api-url/api/keywords?since=weekly
```

Response:

```json
{
  "code": 200,
  "message": "success",
  "data": [
    { "keyword": "agent", "weight": 8 },
    { "keyword": "data", "weight": 6 }
  ]
}
```

### 3. GET /api/top-repositories?since=period
Returns the top starred repositories on GitHub Trending.

Query Parameters:

since — One of daily, weekly, or monthly
Example:

```bash
curl https://your-render-url.onrender.com/api/top-repositories?since=weekly
```

Response:

```json
{
  "code": 200,
  "message": "success",
  "data": [
    {
      "repo_name": "mindsdb/mindsdb",
      "repo_url": "https://github.com/mindsdb/mindsdb",
      "language": "Python",
      "stars": 30776,
      "description": "AI's query engine for federated data"
    }
  ]
}
```

## 🛠️ Getting Started Locally

### 1. Clone the repository

```bash
git clone https://github.com/kkklausxyz/tech-trends-api.git
cd tech-trends-api
```

### 2. Create and activate virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure environment variables
Create a .env file:

```bash
DATABASE_URL=your-postgres-connection-url
```

You can get this from Supabase project settings.
### 5. Run the app

```bash
flask run
```

Visit http://localhost:5000/api/trends

## 🔒 Notes

- Data ETL is run separately and updates the database with GitHub trending data (fully compliant with GitHub’s usage policies)

## 📊 Part of the Tech Trends Explorer Project

- Frontend: React + Tailwind CSS → Vercel
- Backend: Flask + PostgreSQL → Render + Supabase
- Data: GitHub Trending (ETL via Python)
