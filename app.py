####################################################
# # app.py
# ----
# 
# Written in the Python 3.7.9 Environment
# 
# By Nicole Lund 
# 
# This python flask app displays weather forecast data 
# collected from the national weather that is stored in a 
# heroku postgreSQL DB.
####################################################

# Import Dependencies
import os
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect,
    session,
    url_for)
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
    sys.path.append(r"C:\Users\anne_\OneDrive\Documents\GitHub\untracked files")
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
    # Delete existing db table rows

    # Insert refreshed data into db table rows

    return render_template("index.html", location_display = 'Bog Springs')


#################################################
# update route
#################################################
@app.route("/update")
def update_data():
    # Delete existing db table rows

    # Insert refreshed data into db table rows

    return redirect(request.referrer, code=302)


#################################################
# Bog Springs route
#################################################
@app.route("/bog_springs")
def show_bog_springs():
    return render_template("index.html", location_display = 'Bog Springs')


#################################################
# Rose Canyon route
#################################################
@app.route("/rose_canyon")
def show_rose_canyon():
    return render_template("index.html", location_display = 'Rose Canyon')
    

#################################################
# Bog Springs route
#################################################
@app.route("/spencer_canyon")
def show_spencer_canyon():
    return render_template("index.html", location_display = 'Spencer Canyon')


#################################################
# box_plot json route
#################################################
@app.route("/api/box_plot.json")
def box_plot_json():
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


#################################################
# bog springs json route
#################################################
@app.route("/api/bog_springs.json")
def bog_springs_json():
    camp_wx_results = db.session.query(camp_wx.campground,camp_wx.forest_url,camp_wx.campsite_url,camp_wx.fire_danger,camp_wx.map_code).all()

    camp_wx_dict = {
        "campground": camp_wx_results[0][0],
        "forest_url": camp_wx_results[0][1],
        "campsite_url": camp_wx_results[0][2],
        "fire_danger": camp_wx_results[0][3],
        "map_code": camp_wx_results[0][4]
    }

    forecast_dict = {}

    results = db.session.query(cg_bog_spring.forecasted_temperature_degF).all()
    data = [datum[0] for datum in results]
    forecast_dict["forecasted_temperature_degF"] = data

    results = db.session.query(cg_bog_spring.forecastTime_temperature).all()
    data = [datum[0] for datum in results]
    forecast_dict["forecastTime_temperature"] = data

    results = db.session.query(cg_bog_spring.forecasted_windSpeed_miles_per_h).all()
    data = [datum[0] for datum in results]
    forecast_dict["forecasted_windSpeed_miles_per_h"] = data

    results = db.session.query(cg_bog_spring.forecastTime_windSpeed).all()
    data = [datum[0] for datum in results]
    forecast_dict["forecastTime_windSpeed"] = data

    results = db.session.query(cg_bog_spring.forecasted_windGust_miles_per_h).all()
    data = [datum[0] for datum in results]
    forecast_dict["forecasted_windGust_miles_per_h"] = data

    results = db.session.query(cg_bog_spring.forecastTime_windGust).all()
    data = [datum[0] for datum in results]
    forecast_dict["forecastTime_windGust"] = data

    results = db.session.query(cg_bog_spring.forecasted_probabilityOfPrecipitation).all()
    data = [results[0][0] for datum in results]
    forecast_dict["forecasted_probabilityOfPrecipitation"] = data

    results = db.session.query(cg_bog_spring.forecastTime_probabilityOfPrecipitation).all()
    data = [results[0][0] for datum in results]
    forecast_dict["forecastTime_probabilityOfPrecipitation"] = data

    results = db.session.query(cg_bog_spring.forecasted_quantityOfPrecipitation_mm).all()
    data = [datum[0] for datum in results]
    forecast_dict["forecasted_quantityOfPrecipitation_mm"] = data

    results = db.session.query(cg_bog_spring.forecastTime_quantityOfPrecipitation).all()
    data = [datum[0] for datum in results]
    forecast_dict["forecastTime_quantityOfPrecipitation"] = data

    detailed_data = [camp_wx_dict, forecast_dict]

    return jsonify(detailed_data)


#################################################
# rose canyon json route
#################################################
@app.route("/api/rose_canyon.json")
def rose_canyon_json():
    camp_wx_results = db.session.query(camp_wx.campground,camp_wx.forest_url,camp_wx.campsite_url,camp_wx.fire_danger,camp_wx.map_code).all()

    camp_wx_dict = {
        "campground": camp_wx_results[1][0],
        "forest_url": camp_wx_results[1][1],
        "campsite_url": camp_wx_results[1][2],
        "fire_danger": camp_wx_results[1][3],
        "map_code": camp_wx_results[1][4]
    }

    forecast_dict = {}

    results = db.session.query(cg_rose_canyon.forecasted_temperature_degF).all()
    data = [datum[0] for datum in results]
    forecast_dict["forecasted_temperature_degF"] = data

    results = db.session.query(cg_rose_canyon.forecastTime_temperature).all()
    data = [datum[0] for datum in results]
    forecast_dict["forecastTime_temperature"] = data

    results = db.session.query(cg_rose_canyon.forecasted_windSpeed_miles_per_h).all()
    data = [datum[0] for datum in results]
    forecast_dict["forecasted_windSpeed_miles_per_h"] = data

    results = db.session.query(cg_rose_canyon.forecastTime_windSpeed).all()
    data = [datum[0] for datum in results]
    forecast_dict["forecastTime_windSpeed"] = data

    results = db.session.query(cg_rose_canyon.forecasted_windGust_miles_per_h).all()
    data = [results[0][0] for datum in results]
    forecast_dict["forecasted_windGust_miles_per_h"] = data

    results = db.session.query(cg_rose_canyon.forecastTime_windGust).all()
    data = [results[0][0] for datum in results]
    forecast_dict["forecastTime_windGust"] = data

    results = db.session.query(cg_rose_canyon.forecasted_probabilityOfPrecipitation).all()
    data = [results[0][0] for datum in results]
    forecast_dict["forecasted_probabilityOfPrecipitation"] = data

    results = db.session.query(cg_rose_canyon.forecastTime_probabilityOfPrecipitation).all()
    data = [datum[0] for datum in results]
    forecast_dict["forecastTime_probabilityOfPrecipitation"] = data

    results = db.session.query(cg_rose_canyon.forecasted_quantityOfPrecipitation_mm).all()
    data = [datum[0] for datum in results]
    forecast_dict["forecasted_quantityOfPrecipitation_mm"] = data

    results = db.session.query(cg_rose_canyon.forecastTime_quantityOfPrecipitation).all()
    data = [datum[0] for datum in results]
    forecast_dict["forecastTime_quantityOfPrecipitation"] = data

    detailed_data = [camp_wx_dict, forecast_dict]

    return jsonify(detailed_data)


#################################################
# spencer canyon json route
#################################################
@app.route("/api/spencer_canyon.json")
def spencer_canyon_json():
    camp_wx_results = db.session.query(camp_wx.campground,camp_wx.forest_url,camp_wx.campsite_url,camp_wx.fire_danger,camp_wx.map_code).all()

    camp_wx_dict = {
        "campground": camp_wx_results[2][0],
        "forest_url": camp_wx_results[2][1],
        "campsite_url": camp_wx_results[2][2],
        "fire_danger": camp_wx_results[2][3],
        "map_code": camp_wx_results[2][4]
    }

    forecast_dict = {}

    results = db.session.query(cg_spencer_canyon.forecasted_temperature_degF).all()
    data = [datum[0] for datum in results]
    forecast_dict["forecasted_temperature_degF"] = data

    results = db.session.query(cg_spencer_canyon.forecastTime_temperature).all()
    data = [datum[0] for datum in results]
    forecast_dict["forecastTime_temperature"] = data

    results = db.session.query(cg_spencer_canyon.forecasted_windSpeed_miles_per_h).all()
    data = [datum[0] for datum in results]
    forecast_dict["forecasted_windSpeed_miles_per_h"] = data

    results = db.session.query(cg_spencer_canyon.forecastTime_windSpeed).all()
    data = [datum[0] for datum in results]
    forecast_dict["forecastTime_windSpeed"] = data

    results = db.session.query(cg_spencer_canyon.forecasted_windGust_miles_per_h).all()
    data = [datum[0] for datum in results]
    forecast_dict["forecasted_windGust_miles_per_h"] = data

    results = db.session.query(cg_spencer_canyon.forecastTime_windGust).all()
    data = [datum[0] for datum in results]
    forecast_dict["forecastTime_windGust"] = data

    results = db.session.query(cg_spencer_canyon.forecasted_probabilityOfPrecipitation).all()
    data = [datum[0] for datum in results]
    forecast_dict["forecasted_probabilityOfPrecipitation"] = data

    results = db.session.query(cg_spencer_canyon.forecastTime_probabilityOfPrecipitation).all()
    data = [results[0][0] for datum in results]
    forecast_dict["forecastTime_probabilityOfPrecipitation"] = data

    results = db.session.query(cg_spencer_canyon.forecasted_quantityOfPrecipitation_mm).all()
    data = [results[0][0] for datum in results]
    forecast_dict["forecasted_quantityOfPrecipitation_mm"] = data

    results = db.session.query(cg_spencer_canyon.forecastTime_quantityOfPrecipitation).all()
    data = [datum[0] for datum in results]
    forecast_dict["forecastTime_quantityOfPrecipitation"] = data

    detailed_data = [camp_wx_dict, forecast_dict]

    return jsonify(detailed_data)
    

#################################################
# Default run behavior
#################################################
if __name__ == "__main__":
    app.run(debug=True)
