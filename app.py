####################################################
# # app.py
# ----
# 
# Written in the Python 3.7.9 Environment
# 
# By Nicole Lund 
# 
# This Python script stores scraped web data in a postgreSQL DB 
# and displays on a webpage.
####################################################

# Import Dependencies
import os
import psycopg2
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)
from flask_sqlalchemy import SQLAlchemy

# Import local file dependencies
from models import create_classes
import refresh_data

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Database Setup
#################################################

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://hgquoluqhpempn:1250a45ed32360cfb6492b98943bc4cd80699a8f00a1144625b3cf52b2db11c9@ec2-44-194-112-166.compute-1.amazonaws.com:5432/d3lajcergj0dej?sslmode=require'

# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL?sslmode=require')

# Remove tracking modifications
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

camp_data = create_classes(db)


#################################################
# Create index.html route
#################################################
@app.route("/")
def index():
    refreshed_data = refresh_data.refresh()
    print("Index: ")
    print(refreshed_data)

    # Delete existing collection

    # Insert refreshed data into db

    return render_template("index.html", refreshed_data=refreshed_data)


if __name__ == "__main__":
    app.run(debug=True)
