from faker import Faker
from database import get_db_connection  # Import your existing database connection function

fake = Faker()

def insert_fake_notifications(n=99999):
    """Generate and insert fake notifications into the existing database."""
    conn = get_db_connection()  # Use your function to connect to the database
    cursor = conn.cursor()

    for _ in range(n):
        handling_office = fake.company()
        content = fake.sentence()
        is_active = fake.random_element([0, 1])  # Randomly set active or inactive status

        cursor.execute(
            "INSERT INTO notifications (handling_office, content, is_active) VALUES (?, ?, ?)",
            (handling_office, content, is_active),
        )

    conn.commit()
    print("enter fake data")
    conn.close()
    print(f"Inserted {n} fake notifications successfully.")

if __name__ == "__main__":
    insert_fake_notifications(99999)  # Change the number to insert more notifications
