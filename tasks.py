from celery import Celery
from db_utils import get_db_connection
from fetch_nimble_contacts import fetch_nimble_contacts

app = Celery('tasks', broker='redis://localhost:6379/0')


@app.task
def update_contacts_from_nimble():
    """ Updates contacts in the database from the Nimble service """
    try:
        contacts_data = fetch_nimble_contacts()

        conn = get_db_connection()
        cursor = conn.cursor()

        for contact in contacts_data:
            first_name = contact['first_name']
            last_name = contact['last_name']
            email = contact['emails'][0]['email'] if contact['emails'] else None

            cursor.execute(
                "INSERT INTO contacts (first_name, last_name, email) "
                "VALUES (%s, %s, %s) "
                "ON CONFLICT (email) DO UPDATE SET first_name = %s, last_name = %s",
                (first_name, last_name, email, first_name, last_name)
            )

        conn.commit()
    except Exception as e:
        print(f"Error updating contacts: {e}")
    finally:
        cursor.close()
        conn.close()
