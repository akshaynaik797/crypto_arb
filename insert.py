import pymongo, json

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["crypto_prices"]
mycol = mydb["wazirx"]
with open("wazirx.csv") as fp:
    for row in fp:
        a = row.split('|')
        record = json.loads(a[1].strip('\n').replace('\'', '\"'))
        try:
            x = mycol.insert_one({"_id":float(a[0]), "prices":record})
            print(x.inserted_id)
        except pymongo.errors.DuplicateKeyError:
            pass

