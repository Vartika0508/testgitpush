from pymongo.mongo_client import MongoClient
uri = "mongodb+srv://vartikagupta85:Mbfn7k05@cluster0.dm30f.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(uri)
print(client)
try :
    client.admin.command("ping")
    print("Successfully connected to MongoDB")
except Exception as e:
    print(e)

d = {"name": "Vartika","email" : "vartika.gupta85@gmail.com", "surname": "Gupta"}
db = client["mydb"]
coll = db["test1"]
coll.insert_one(d)