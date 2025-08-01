print("this is working fine")
from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://htayyabhas:1234@cluster0.gbahfjc.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("error=======")
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print("erroe----")
    print(e)