import os
from flask import Flask, render_template, redirect, request, url_for, Blueprint
from flask_pymongo import PyMongo, pymongo
from bson.objectid import ObjectId
from flask_paginate import Pagination, get_page_parameter

app = Flask(__name__)
# app = Blueprint('idioms', __name__)

app.config["MONGO_DBNAME"] = "idioms-and-proverbs"
app.config["MONGO_URI"] = "mongodb+srv://jk27:07diciembre18@cluster0-9pga0.mongodb.net/idioms-and-proverbs?retryWrites=true&w=majority"

mongo = PyMongo(app)                                    

# --------------------------------------------------------------------------- Functions for displaying the idioms and pagination
@app.route("/")
@app.route("/get_idioms")
def get_idioms():
    
    idiom = mongo.db.idioms
    pageSize = 2
    
    search = False
    q = request.args.get('q')
    if q:
        search = True

    page = request.args.get(get_page_parameter(), type=int, default=1)

    idioms = idiom.find().sort('_id', pymongo.DESCENDING).limit(pageSize).skip(pageSize*(page-1))
    pagination = Pagination(page=page, total=idioms.count(), search=search, record_name='idioms')
    # 'page' is the default name of the page parameter, it can be customized
    # e.g. Pagination(page_parameter='p', ...)
    # or set PAGE_PARAMETER in config file
    # also likes page_parameter, you can customize for per_page_parameter
    # you can set PER_PAGE_PARAMETER in config file
    # e.g. Pagination(per_page_parameter='pp')

    return render_template('idioms.html',
                           idioms=idioms,
                           pagination=pagination,
                           )
    
    
    
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
    
@app.route("/update_idiom/<idiom_id>", methods=["POST"])                #-- Data from form in editidiom.html is posted using this function...
def update_idiom(idiom_id):
    idioms = mongo.db.idioms                                            #-- ... data is updated in the idioms database...
    idioms.update({"_id":ObjectId(idiom_id)},                           #-- ... updating the item with a specific id...
    {
        "spanish_idiom": request.form.get("spanish_idiom"),             #-- ... each field for that item will be updated taking the input from...
        "english_literal": request.form.get("english_literal"),         #-- ... the corresponding field on the form
        "english_meaning": request.form.get("english_meaning"),
        "english_idiom": request.form.get("english_idiom"),
        "spanish_literal": request.form.get("spanish_literal"),
        "spanish_meaning": request.form.get("spanish_meaning")
    })
    return redirect(url_for("get_idioms"))
    
# -------------------------------------------------------------------- Function to delete idioms -- #
@app.route("/delete_idiom/<idiom_id>")
def delete_idiom(idiom_id):
    mongo.db.idioms.remove({"_id": ObjectId(idiom_id)})
    return redirect(url_for("get_idioms"))
    
    
    

    
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
