from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")

# Access the database and collection
db = client["student_database"]
collection = db["students"]

# Add your student ID
student_id = input("Enter your student ID: ")
collection.insert_one({"student_id": student_id})
print(f"Student ID {student_id} added successfully!")

# View all student IDs
print("\nHere are all the student IDs:")
for student in collection.find():
    print(student["student_id"])
