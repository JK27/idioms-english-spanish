import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = "idioms"
app.config["MONGO_URI"] = "mongodb+srv://jk27:07diciembre18@cluster0-9pga0.mongodb.net/idioms-and-proverbs?retryWrites=true&w=majority"

mongo = PyMongo(app)

@app.route("/")
@app.route("/get_idioms")
def get_idioms():
    return render_template("idioms.html", idioms=mongo.db.idioms.find())
    
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
