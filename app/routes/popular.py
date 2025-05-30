from flask import Blueprint, request
from app.db import get_connection
from app.utils import api_response

popular_bp = Blueprint("popular", __name__)

@popular_bp.route("/api/top-repositories", methods=["GET"])
def get_top_repositories():
    since = request.args.get("since", "daily")

    try:
        conn = get_connection()
        cur = conn.cursor()

        cur.execute("""
            SELECT repo_name, repo_url, description, language, stars_total
            FROM trending_repositories
            WHERE time_span = %s AND fetched_at::date = CURRENT_DATE
            ORDER BY stars_total DESC
        """, (since,))
        rows = cur.fetchall()
        cur.close()
        conn.close()

        results = [
            {
                "repo_name": r[0],
                "repo_url": r[1],
                "description": r[2],
                "language": r[3],
                "stars": r[4]
            } for r in rows
        ]

        return api_response(data=results)

    except Exception as e:
        return api_response(code=500, message=str(e), data=[])
