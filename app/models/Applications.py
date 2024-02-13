import psycopg2

def ApplicationModel(conn: psycopg2.extensions.connection) -> None:
    cur: psycopg2.extensions.cursor = conn.cursor()
    try:
        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS Applications (
                listingID SERIAL PRIMARY KEY,
                position TEXT NOT NULL,
                salary DECIMAL(10, 2),
                location TEXT NOT NULL,
                company TEXT NOT NULL,
                remote BOOLEAN,
                jobType TEXT NOT NULL,
                description TEXT,
                applicationDeadline DATE,
                notes TEXT,
                userID int,
                CONSTRAINT userID FOREIGN KEY(userID) REFERENCES users(id)
            )
            """
        )
        conn.commit()
        cur.close()
        print("Job Applications table created successfully")
    except Exception as e:
        print(f"Failed to execute table creation with error: {e}")

        return None