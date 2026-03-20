from flask import Blueprint, request, jsonify, redirect
from models import insert_url, get_url, increment_clicks
import random, string

url_bp = Blueprint('url_bp', __name__)

def generate_code(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

@url_bp.route('/shorten', methods=['POST'])
def shorten_url():
    data = request.json

    if not data or 'url' not in data:
        return jsonify({"error": "URL is required"}), 400

    original_url = data.get('url')
    expires_at = data.get('expires_at')  # optional

    short_code = generate_code()

    insert_url(original_url, short_code, expires_at)

    return jsonify({
        "short_url": f"http://localhost:5000/{short_code}",
        "expires_at": expires_at
    })


@url_bp.route('/<short_code>')
def redirect_url(short_code):
    result = get_url(short_code)

    if result:
        increment_clicks(short_code)
        return redirect(result['original_url'])
    else:
        return jsonify({"error": "URL not found or expired"}), 404