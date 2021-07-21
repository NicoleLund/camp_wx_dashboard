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
# index.html route
#################################################
@app.route("/")
def index():
    refreshed_data = refresh_data.refresh()
    selected_data = refreshed_data['bog_springs_fire']

    # Delete existing db table rows

    # Insert refreshed data into db table rows

    return render_template("index.html", selected_data=selected_data)

#################################################
# update route
#################################################
@app.route("/update")
def update_data():
    refreshed_data = refresh_data.refresh()
    selected_data = refreshed_data['bog_springs_fire']

    # Delete existing db table rows

    # Insert refreshed data into db table rows

    return render_template("index.html", selected_data=selected_data)

#################################################
# bog springs route
#################################################
@app.route("/bog_springs")
def show_bog_springs():
    refreshed_data = refresh_data.refresh()
    selected_data = refreshed_data['bog_springs_fire']

    # Delete existing db table rows

    # Insert refreshed data into db table rows

    return render_template("index.html", selected_data=selected_data)

#################################################
# rose canyon route
#################################################
@app.route("/rose_canyon")
def show_rose_canyon():
    refreshed_data = refresh_data.refresh()
    selected_data = refreshed_data['rose_canyon_fire']

    # Delete existing db table rows

    # Insert refreshed data into db table rows

    return render_template("index.html", selected_data=selected_data)

#################################################
# spencer canyon route
#################################################
@app.route("/spencer_canyon")
def show_spencer_canyon():
    refreshed_data = refresh_data.refresh()
    selected_data = refreshed_data['spencer_canyon_fire']

    # Delete existing db table rows

    # Insert refreshed data into db table rows

    return render_template("index.html", selected_data=selected_data)
    
#################################################
# Default run behavior
#################################################
if __name__ == "__main__":
    app.run(debug=True)
