import os
from pymongo import MongoClient
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get MongoDB credentials from environment variables
username = os.getenv('MONGODB_USERNAME')
password = os.getenv('MONGODB_PASSWORD')

# Construct the MongoDB URI
uri = f'mongodb+srv://{username}:{password}@cluster0.3ev7rmp.mongodb.net/'

# Connect to MongoDB
client = MongoClient(uri)

# Specify the database and collection
db = client['Personal']
collection = db['Test']

# Function to get user input and insert it into the database
def insert_user():
    # Get user input
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    hometown = input("Enter your hometown: ")

    # Create a dictionary with the user data
    user_data = {
        'name': name,
        'age': age,
        'hometown': hometown
    }

    # Insert the data into the MongoDB collection
    with pymongo.timeout(1):
        result = collection.insert_one(user_data)
    print(f"Data inserted with record id: {result.inserted_id}")

# Function to fetch and display all records from the collection
def fetch_all_users():
    filter = {}  # Empty filter to fetch all documents
    results = collection.find(filter)
    
    print("All records in the collection:")
    for doc in results:
        print(doc)
def main():
    # Call the function to insert user data
    insert_user()

    # Call the function to fetch and display all records
    fetch_all_users()

if __name__ == '__main__':
    main()
    