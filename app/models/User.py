import psycopg2

def UserModel(conn: psycopg2.extensions.connection) -> None:
    cur: psycopg2.extensions.cursor = conn.cursor()

    # Execute queries to create table
    try:
        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                email TEXT NOT NULL UNIQUE,
                username TEXT NOT NULL,
                password TEXT NOT NULL,
                time_stamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            """
        )
        conn.commit()
        cur.close()
        print("User table created successfully")
    except Exception as e:
        print(f"Failed to execute table creation with error: {e}")

    return None
