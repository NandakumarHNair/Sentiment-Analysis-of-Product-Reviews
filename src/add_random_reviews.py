import sqlite3
import random
from faker import Faker

# Initialize Faker for generating random reviews
fake = Faker()

# Connect to the SQLite database
# The database name is sentimental_analysis.db
connection = sqlite3.connect('sentimental_analysis.db')
cursor = connection.cursor()

# Function to generate random reviews
def generate_random_reviews(num_reviews=50):
    reviews = []
    for _ in range(num_reviews):
        review_text = fake.sentence(nb_words=random.randint(5, 15))  # Generate random sentence as review
        rating = random.randint(1, 5)  # Random rating between 1 and 5
        reviews.append((review_text, rating))
    return reviews

# Function to delete existing reviews and insert new ones
def reset_and_insert_reviews_to_db(reviews):
    try:
        # Delete all existing rows in the table
        cursor.execute('DELETE FROM product_reviews')
        connection.commit()
        print("Deleted existing content in product_reviews table.")

        # Insert new random reviews into the table
        cursor.executemany('''
            INSERT INTO product_reviews (review_text, rating)
            VALUES (?, ?)
        ''', reviews)
        connection.commit()
        print(f"Successfully inserted {len(reviews)} new reviews into the database.")
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        connection.close()

if __name__ == "__main__":
    # Generate 50 random product reviews
    random_reviews = generate_random_reviews(50)

    # Delete existing content and insert new reviews into the database
    reset_and_insert_reviews_to_db(random_reviews)
import sqlite3
import random
from faker import Faker

# Initialize Faker for generating random reviews
fake = Faker()

# Connect to the SQLite database
# The database name is now sentimental_analysis.db
connection = sqlite3.connect('sentimental_analysis.db')
cursor = connection.cursor()

# Function to generate random reviews
def generate_random_reviews(num_reviews=50):
    reviews = []
    for _ in range(num_reviews):
        review_text = fake.sentence(nb_words=random.randint(5, 15))  # Generate random sentence as review
        rating = random.randint(1, 5)  # Random rating between 1 and 5
        reviews.append((review_text, rating))
    return reviews

# Function to insert reviews into the database
def insert_reviews_to_db(reviews):
    try:
        cursor.executemany('''
            INSERT INTO product_reviews (review_text, rating)
            VALUES (?, ?)
        ''', reviews)
        connection.commit()
        print(f"Successfully inserted {len(reviews)} reviews into the database.")
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        connection.close()

if __name__ == "__main__":
    # Generate 50 random product reviews
    random_reviews = generate_random_reviews(50)

    # Insert the generated reviews into the database
    insert_reviews_to_db(random_reviews)

