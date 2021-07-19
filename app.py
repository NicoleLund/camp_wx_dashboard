####################################################
# # app.py
# ----
# 
# Written in the Python 3.7.9 Environment
# 
# By Nicole Lund 
# 
# This Python script stores scraped web data in a Pymongo DB 
# and displays on a webpage.
####################################################

# Import Dependencies
from flask import Flask, render_template, redirect
# from flask_pymongo import PyMongo
import refresh_data

app = Flask(__name__)

# # Use flask_pymongo to set up mongo connection
# app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_factoids"
# mongo = PyMongo(app)

# @app.route("/")
# def index():
#     mars_data = mongo.db.mars_data.find_one()
#     return render_template("index.html")

# @app.route("/scrape")
# def scraper():

#     # Delete existing collection
#     mongo.db.mars_data.drop()

#     # Insert scraped mars data document
#     mongo.db.mars_data.insert_one(refresh_data.scrape())

#     # Return to root
#     return redirect("/", code=302)


# if __name__ == "__main__":
#     app.run(debug=True)
