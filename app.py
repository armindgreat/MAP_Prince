from flask import Flask, request
import json


import pymongo

# Replace CONNECTION_STRING with your actual connection string
client = pymongo.MongoClient("mongodb://localhost:27017/")

# Access the database
dbname = client['LPW']

# Access a collection
collection_name = dbname['Patient']
app=Flask(__name__)
patient=[
    {
        "name":"John",
        "Age":"18",
        "Address":"Ahmedabad",
        "Phone":"1234567890"
    },
     {
        "name":"Alice",
        "Age":"8",
        "Address":"Dubai",
        "Phone":"1234567890"
    },
     {
        "name":"Krishna",
        "Age":"18",
        "Address":"Ahmedabad",
        "Phone":"1234567890"
    },
]
# python flask application for hospital management system ?
# convert list to json ?
# hospital management system using python flask
@app.route('/patients', methods=['GET'])
def give():
    return json.dumps(patient)

# intergrate with mongodb compass ?

# add data to mongodb compass?
@app.route('/patients', methods=['POST'])
def create():
    data = request.get_json()
    patient.append(data)
    collection_name.insert_one(data)
    return {'message': 'Patient added successfully'}, 201
# delete record in mongodb compass ?
@app.route('/patients',methods=['DELETE'])
def delete():
    data = request.get_json()
    collection_name.delete_one(data)
    return {'message':'Patient Data Deleted'},200

filter={"name":"Ram"}
@app.route('/patients',methods=['PUT'])
def put():
    data = request.get_json()
    collection_name.update_one(filter,data)
    return {'message':'Patient Data Updated'},200

if __name__=="__main__":
    app.run(debug=True)

# create docker image for this file ?

# command to add current file to git repo ?