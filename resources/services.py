def cursor_to_json(cursor, rows):
    cols = [col[0] for col in cursor.description]
    data = [dict(zip(cols, row)) for row in rows]

    return data