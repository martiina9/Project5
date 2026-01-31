import mysql.connector

x = ("-" * 50) 


def create_database_if_not_exists():
    """Creates the database if it does not already exist."""

    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="zzjezivot"    
        )
        cursor = conn.cursor()   
        cursor.execute("CREATE DATABASE IF NOT EXISTS task_db")
        print("✅ Database 'task_db' is ready.")
        
    except mysql.connector.Error as err:
        print(f"❌ Error creating database: {err}")
    
    finally:
        if cursor is not None:
            cursor.close()
        if conn is not None:
            conn.close()


def get_connection():
    """Establishes and returns a connection to the task_db database."""

    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="zzjezivot",
            database="task_db"
        )
        return conn
    
    except mysql.connector.Error as err:
        print(f"❌ Connection error: {err}")

        return None
    

def create_table_if_not_exists():
    """Creates the task_crud table if it does not already exist."""

    conn = get_connection()

    if conn is None:
        print("❌ Failed to connect to the database.")
        return
    
    try:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS task_crud (
                id INT PRIMARY KEY AUTO_INCREMENT,
                name VARCHAR(100) NOT NULL,
                description TEXT NOT NULL,
                status ENUM('not started', 'in process', 'done') DEFAULT 'not started',
                created_on TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        print("✅ Table 'task_crud' exists or was created successfully.")
        print(x)

    except mysql.connector.Error as err:
        print(f"❌ Error creating table: {err}")

    finally:
        cursor.close()
        conn.close()