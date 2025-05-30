from flask import Blueprint, request
from app.db import get_connection
from app.utils import api_response

language_bp = Blueprint("language", __name__)

@language_bp.route("/api/language-distribution", methods=["GET"])
def get_language_distribution():
    since = request.args.get("since", "daily")

    try:
        conn = get_connection()
        cur = conn.cursor()

        cur.execute("""
            SELECT language, language_color, COUNT(*) as count
            FROM trending_repositories
            WHERE time_span = %s AND fetched_at::date = CURRENT_DATE
            GROUP BY language, language_color
            ORDER BY count DESC
        """, (since,))
        rows = cur.fetchall()
        cur.close()
        conn.close()

        results = [
            {
                "language": r[0],
                "color": r[1],
                "count": r[2]
            } for r in rows if r[0]  # 排除 language 为 NULL 的情况
        ]

        return api_response(data=results)

    except Exception as e:
        return api_response(code=500, message=str(e), data=[])
