import json
from pymongo import MongoClient

# MongoDB Connection
client = MongoClient('mongodb://localhost:27017')
db = client.my_db

def insert_records_dynamic(dataframes):
    with open('context.json', 'r') as file:
        context = json.load(file)
    
    for df_name, collection_name in context.items():
        if df_name in dataframes:
            df = dataframes[df_name]
            records = df.to_dict('records')
            collection = db[collection_name]
            collection.delete_many({})
            if records:
                collection.insert_many(records)
                print(f"{collection_name} collection: Inserted {len(records)} records successfully.")
            else:
                print(f"{collection_name} collection: No records to insert.")
        else:
            print(f"Warning: DataFrame {df_name} not found in the provided data.")