from flask import Blueprint, request
from app.db import get_connection
from app.utils.api_response import api_response
from app.utils.stopwords import stop_words

import re
from collections import Counter

keywords_bp = Blueprint("keywords", __name__)

@keywords_bp.route("/api/keywords", methods=["GET"])
def get_keywords():
    since = request.args.get("since", "daily")

    try:
        conn = get_connection()
        cur = conn.cursor()

        cur.execute("""
            SELECT description
            FROM trending_repositories
            WHERE time_span = %s AND fetched_at::date = CURRENT_DATE
        """, (since,))
        rows = cur.fetchall()
        cur.close()
        conn.close()

        all_text = " ".join([r[0] for r in rows if r[0]])
        words = re.findall(r'\b[a-zA-Z]{3,}\b', all_text.lower())

        filtered_words = [w for w in words if w not in stop_words]
        common = Counter(filtered_words).most_common(30)

        results = [{"keyword": w, "weight": c} for w, c in common]

        return api_response(data=results)

    except Exception as e:
        return api_response(code=500, message=str(e), data=[])
