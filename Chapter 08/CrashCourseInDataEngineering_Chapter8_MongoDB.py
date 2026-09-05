# Import the necessary modules from pymongo
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# Define the connection string (URI) for MongoDB
uri = "mongodb+srv://<username>:<password>@cluster0.uqmarno.mongodb.net/?appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
# The MongoClient is now set up and connected to the MongoDB server

# Create or use database 'school'
db = client["school"]

# Create (or use) a collection (table equivalent) 'students'
students = db["students"]

# Insert multiple student documents
students.insert_many([
    {"firstname": "Leonardo", "lastname": "DiCaprio", "age": 7, "grade": "2nd"},
    {"firstname": "Tom", "lastname": "Cruise", "age": 10, "grade": "5th"},
    {"firstname": "Harry", "lastname": "Potter", "age": 12, "grade": "7th"}
])
print("Data inserted successfully!")

#Querying the data: see complete table
for student in students.find():
    print(student)

# Querying the data: see table with conditional statement
print("\nStudents with age > 8:")
for student in students.find({"age": {"$gt": 8}}):
    print(student)

# Querying the data: see specific columns of the table
for student in students.find({}, {"firstname": 1, "age": 1, "_id": 0}):
    print(student)

# Updating the data: modify a specific record
students.update_one(
    {"firstname": "Leonardo"},
    {"$set": {"grade": "3rd"}}
)
print("\nAfter updating Leonardo’s grade:")
for student in students.find():
    print(student)

students.delete_many({"age": {"$lt": 8}})

# Updating the data: delete a specific record based on a condition
print("\nAfter deleting students with age < 8:")
for student in students.find():
    print(student)

#Delete a table and database
students.drop()
print("\nCollection 'students' dropped.")
client.drop_database("school")
print("Database 'school' dropped.")

# Close the connection
client.close()
print("Connection closed!")