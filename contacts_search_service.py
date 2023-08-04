from flask import Flask, request, jsonify
from db_utils import get_db_connection

app = Flask(__name__)


@app.route('/search', methods=['GET'])
def search_contacts():
    """ Performs a full-text search for contacts in the database based on the given request """
    search_query = request.args.get('query', '')

    with get_db_connection() as conn, conn.cursor() as cursor:
        cursor.execute(
            "SELECT * FROM contacts "
            "WHERE to_tsvector('english', first_name || ' ' || last_name || ' ' || COALESCE(email, '')) "
            "@@ plainto_tsquery('english', %s)",
            (search_query,)
        )

        results = cursor.fetchall()

        contacts = [{'first_name': row[1], 'last_name': row[2], 'email': row[3]} for row in results]

    return jsonify(contacts)


if __name__ == '__main__':
    app.run()
