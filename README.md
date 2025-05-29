# Tech Trends Explorer (Backend)

This is the backend API for **Tech Trends Explorer**, a web application that visualizes trending programming languages on GitHub. The API is built with Flask, retrieves data from a PostgreSQL database, and serves JSON responses to the frontend.

## 🌐 Live API

👉 [Visit the API](https://tech-trends-api-dymi.onrender.com/api/trends)

## ⚙️ Tech Stack

- **Backend Framework**: [Flask](https://flask.palletsprojects.com/)
- **Database**: [PostgreSQL](https://www.postgresql.org/) hosted on [Supabase](https://supabase.com/)
- **Deployment**: [Render](https://render.com/)
- **ETL**: Python-based script fetching GitHub trending data

## 📡 API Endpoint

### `GET /api/trends?since=period`

Fetches trending language data.

#### Parameters:

- `since`: One of `daily`, `weekly`, or `monthly`

#### Example:

```bash
curl https://your-render-url.onrender.com/api/trends?since=weekly
```

Response:

```bash
[
  { "language": "Python", "count": 125 },
  { "language": "JavaScript", "count": 103 }
]
```

## 🛠️ Getting Started Locally

### 1. Clone the repository

```bash
git clone https://github.com/your-username/tech-trends-api.git
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

Data ETL is run separately and updates the database with GitHub trending data (fully compliant with GitHub’s usage policies)

## 📊 Part of the Tech Trends Explorer Project

Frontend: React + Tailwind CSS → Vercel
Backend: Flask + PostgreSQL → Render + Supabase
Data: GitHub Trending (ETL via Python)
