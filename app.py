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
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)
from flask_sqlalchemy import SQLAlchemy
import psycopg2

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

if len(uri) <= 16:
    import sys
    sys.path.append(r"C:\Users\nlund\Documents\GitHub\untracked_files")
    from camp_wx_uri import uri
    uri = uri.replace('postgres://','postgresql://') + '?sslmode=require'

print(uri)

app.config['SQLALCHEMY_DATABASE_URI'] = uri

# Remove tracking modifications
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

camp_wx, cg_bog_spring, cg_rose_canyon, cg_spencer_canyon = create_classes(db)


#################################################
# index.html route
#################################################
@app.route("/")
def index():
    # refreshed_data = refresh_data.refresh()
    # selected_data = refreshed_data['bog_springs_fire']

    # Delete existing db table rows

    # Insert refreshed data into db table rows

    # return render_template("index.html", selected_data=selected_data)
    return render_template("index.html")

#################################################
# box_plot route
#################################################
@app.route("/api/box_plot.json")
def box_plot():
    # Bog Springs Temperature Forecast
    bg_temp_results = db.session.query(cg_bog_spring.forecasted_temperature_degF).all()
    bg_temp = [bg_temp_results[0][0] for result in bg_temp_results]

    # Rose Canyon Temperature Forecast
    rc_temp_results = db.session.query(cg_rose_canyon.forecasted_temperature_degF).all()
    rc_temp = [rc_temp_results[0][0] for result in rc_temp_results]

    # Spencer Canyon Temperature Forecast
    sc_temp_results = db.session.query(cg_spencer_canyon.forecasted_temperature_degF).all()
    sc_temp = [sc_temp_results[0][0] for result in sc_temp_results]

    temp_data = [{
        "bog_springs_temp": bg_temp,
        "rose_canyon_temp": rc_temp,
        "spencer_canyon_temp": sc_temp
    }]

    return jsonify(temp_data)

# #################################################
# # update route
# #################################################
# @app.route("/update")
# def update_data():
#     # refreshed_data = refresh_data.refresh()
#     # selected_data = refreshed_data['bog_springs_fire']

#     # Delete existing db table rows

#     # Insert refreshed data into db table rows

#     return render_template("index.html", selected_data=selected_data)

# #################################################
# # bog springs route
# #################################################
# @app.route("/bog_springs")
# def show_bog_springs():
#     refreshed_data = refresh_data.refresh()
#     selected_data = refreshed_data['bog_springs_fire']

#     # Delete existing db table rows

#     # Insert refreshed data into db table rows

#     return render_template("index.html", selected_data=selected_data)

# #################################################
# # rose canyon route
# #################################################
# @app.route("/rose_canyon")
# def show_rose_canyon():
#     refreshed_data = refresh_data.refresh()
#     selected_data = refreshed_data['rose_canyon_fire']

#     # Delete existing db table rows

#     # Insert refreshed data into db table rows

#     return render_template("index.html", selected_data=selected_data)

# #################################################
# # spencer canyon route
# #################################################
# @app.route("/spencer_canyon")
# def show_spencer_canyon():
#     refreshed_data = refresh_data.refresh()
#     selected_data = refreshed_data['spencer_canyon_fire']

#     # Delete existing db table rows

#     # Insert refreshed data into db table rows

#     return render_template("index.html", selected_data=selected_data)
    

#################################################
# Default run behavior
#################################################
if __name__ == "__main__":
    app.run(debug=True)
