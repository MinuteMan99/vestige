from db.connection import get_connection


def create_user(full_name, email, password_hash):
    connection = get_connection()
    cursor = connection.cursor()

    query = """
    INSERT INTO users (full_name, email, password_hash)
    VALUES (%s, %s, %s)
    """

    cursor.execute(query, (full_name, email, password_hash))
    connection.commit()

    cursor.close()
    connection.close()


def get_user_by_email(email):
    connection = get_connection()
    cursor = connection.cursor()

    query = "SELECT * FROM users WHERE email = %s"
    cursor.execute(query, (email,))

    user = cursor.fetchone()

    cursor.close()
    connection.close()

    return user
