from database.db import get_db_connection

def insert_url(original_url, short_code, expires_at=None):
    conn = get_db_connection()
    conn.execute(
        "INSERT INTO urls (original_url, short_code, expires_at) VALUES (?, ?, ?)",
        (original_url, short_code, expires_at)
    )
    conn.commit()
    conn.close()

def get_url(short_code):
    conn = get_db_connection()
    result = conn.execute(
        '''
        SELECT * FROM urls 
        WHERE short_code = ? 
        AND (expires_at IS NULL OR expires_at > CURRENT_TIMESTAMP)
        ''',
        (short_code,)
    ).fetchone()
    conn.close()
    return result

def increment_clicks(short_code):
    conn = get_db_connection()
    conn.execute(
        "UPDATE urls SET clicks = clicks + 1 WHERE short_code = ?",
        (short_code,)
    )
    conn.commit()
    conn.close()