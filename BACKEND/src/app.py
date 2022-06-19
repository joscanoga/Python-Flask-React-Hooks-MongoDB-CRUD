import json

from bson import json_util
from flask import Flask, request, jsonify
from flask_pymongo import PyMongo,ObjectId
from flask_cors import CORS

app=Flask(__name__)
app.config['MONGO_URI']='mongodb://localhost:27017/pythonreactdb'
mongo=PyMongo(app)
CORS(app)

#hace referencia a la colecion usuarios dentro de la base de datos
db=mongo.db.users

@app.route("/users", methods=["POST"])
def createUsers():
    id=db.insert_one({
    'name': request.json['name'],
    'email': request.json['email'],
    'password': request.json['password']
    })
    return(str(id.inserted_id))


@app.route("/users", methods=["GET"])
def getUsers():
    users=[]
    for u in db.find():
        users.append({
            '_id': str(ObjectId(u['_id'])),
            'name': u['name'],
            'email': u['email'],
            'password': u['password']
        })


    return(jsonify(users))

@app.route("/users/<id>", methods=["GET"])
def getUser(id):
    user=db.find_one({'_id':ObjectId(id)})
    print(type(user),id)
    return(jsonify({
            '_id': str(ObjectId(user['_id'])),
            'name': user['name'],
            'email': user['email'],
            'password': user['password']
        }))

@app.route("/users/<id>", methods=["DELETE"])
def deleteUser(id):
    db.delete_one({'_id':ObjectId(id)})
    return(jsonify({"msg":"user delete"}))

@app.route("/users/<id>", methods=["PUT"])
def updateUser(id):
    db.update_one({'_id':ObjectId(id)},{'$set':{
    'name': request.json['name'],
    'email': request.json['email'],
    'password': request.json['password']
    }})
    return(jsonify({"msg":"user update"}))


if __name__=="__main__":
    app.run(debug=True)