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

uri = os.environ.get('DATABASE_URL', '').replace('postgres://','postgresql://') + '?sslmode=require'
app.config['SQLALCHEMY_DATABASE_URI'] = uri

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

    # Delete existing collection

    # Insert refreshed data into db

    return render_template("index.html", refreshed_data=refreshed_data)


if __name__ == "__main__":
    app.run(debug=True)
