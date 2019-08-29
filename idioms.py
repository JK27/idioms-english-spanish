import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = "idioms-and-proverbs"
app.config["MONGO_URI"] = "mongodb+srv://jk27:07diciembre18@cluster0-9pga0.mongodb.net/idioms-and-proverbs?retryWrites=true&w=majority"

mongo = PyMongo(app)

@app.route("/")
@app.route("/get_idioms")
def get_idioms():
    return render_template("idioms.html", idioms=mongo.db.idioms.find())

# ---------------------------------------------------------------------     Functions to add idioms -- #
@app.route("/add_idiom")
def add_idiom():
    return render_template("addidiom.html")
    
@app.route("/insert_idiom", methods=["POST"])                           #-- Data from form in addidiom.html is posted using this function...
def insert_idiom():
    idioms = mongo.db.idioms                                            #-- ... data is inserted to the idioms database...
    idioms.insert_one(request.form.to_dict())                           #-- ... inserting one item to the dictionary...
    return redirect(url_for("get_idioms"))                              #-- ... and then redirecting to /get_idioms
    
# ---------------------------------------------------------------------     Functions to edit idioms -- #    
@app.route("/edit_idiom/ <idiom_id>")
def edit_idiom(idiom_id):                                               #-- Use idiom_id to target the idiom that want to edit
    the_idiom = mongo.db.idioms.find_one({"_id":ObjectId(idiom_id)})    #-- Retrieve the idiom from the idioms database, using its id to find it...
    return render_template("editidiom.html", idiom=the_idiom)           #-- ... and then redirecting to /editidiom.html
    
@app.route("/update_idiom/<idiom_id>", methods=["POST"])
def update_idiom(idiom_id):
    idioms = mongo.db.idioms
    idioms.update({"_id":ObjectId(idiom_id)},
    {
        "spanish_idiom": request.form.get("spanish_idiom"),
        "english_literal": request.form.get("english_literal"),
        "english_meaning": request.form.get("english_meaning"),
        "english_idiom": request.form.get("english_idiom"),
        "spanish_literal": request.form.get("spanish_literal"),
        "spanish_meaning": request.form.get("spanish_meaning")
    })
    return redirect(url_for("get_idioms"))
    
    
    
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
