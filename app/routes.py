from flask import Blueprint, jsonify, request
from .db import get_connection

bp = Blueprint("routes", __name__)

@bp.route("/api/trends", methods=["GET"])
def get_trends():
    period = request.args.get("since", "daily")

    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("""
            SELECT language_counts, updated_at
            FROM trending_languages
            WHERE since = %s
        """, (period,))
        row = cur.fetchone()
        cur.close()
        conn.close()

        if not row:
            return jsonify([])

        language_counts, updated_at = row
        result = [{"language": lang, "count": count} for lang, count in language_counts.items()]
        result.sort(key=lambda x: x["count"], reverse=True)

        return jsonify({
            "data": result,
            "updated_at": updated_at.isoformat()
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

