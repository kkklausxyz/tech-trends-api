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
            SELECT language_counts
            FROM trending_languages
            WHERE since = %s
        """, (period,))
        row = cur.fetchone()
        cur.close()
        conn.close()

        if not row:
            return jsonify([])

        language_counts = row[0]  # 这是一个字典
        result = [{"language": lang, "count": count} for lang, count in language_counts.items()]
        result.sort(key=lambda x: x["count"], reverse=True)  # 按 count 降序排
        return jsonify(result)

    except Exception as e:
        return jsonify({"error": str(e)}), 500
