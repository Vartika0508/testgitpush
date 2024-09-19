import pymongo
client = pymongo.MongoClient("mongodb+srv://vartikagupta85:Mbfn7k05@cluster0.dm30f.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client.test
print(db)

d = {
    "name": "sudhanshu",
    "email": "sudhanshu@ineuron.ai",
    "surname" : "Kumar"

}
db1 = client['mongotest1']
coll = db1['test1']
coll.insert_one(d)
