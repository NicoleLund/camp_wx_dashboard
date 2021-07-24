####################################################
# # models.py
# ----
# 
# Written in the Python 3.7.9 Environment
# 
# By Nicole Lund 
# 
# models.py defines the heroku postgreSQL db table
# classes.
####################################################

def create_classes(db):
    class camp_wx(db.Model):
        __tablename__ = 'camp_wx'

        id = db.Column(db.Integer, primary_key=True)
        campground = db.Column(db.String(255))
        lat = db.Column(db.Float)
        lon = db.Column(db.Float)
        elevation = db.Column(db.Float)
        nws_meta_url = db.Column(db.String(255))
        nws_grid_url = db.Column(db.String(255))
        forest_url = db.Column(db.String(255))
        campsite_url = db.Column(db.String(255))
        fire_danger = db.Column(db.String(50))
        map_code = db.Column(db.String(255))

        def __repr__(self):
            return '<camp_wx %r>' % (self.campground)

    class cg_bog_spring(db.Model):
        __tablename__ = 'cg_bog_spring'

        id = db.Column(db.Integer, primary_key=True)
        campground = db.Column(db.String(255))
        forecasted_temperature_degF = db.Column(db.Float)
        forecastTime_temperature = db.Column(db.Date)
        forecasted_windSpeed_miles_per_h = db.Column(db.Float)
        forecastTime_windSpeed = db.Column(db.Date)
        forecasted_windGust_miles_per_h = db.Column(db.Float)
        forecastTime_windGust = db.Column(db.Date)
        forecasted_probabilityOfPrecipitation = db.Column(db.Float)
        forecastTime_probabilityOfPrecipitation = db.Column(db.Date)
        forecasted_quantityOfPrecipitation_mm = db.Column(db.Float)
        forecastTime_quantityOfPrecipitation = db.Column(db.Date)

        def __repr__(self):
            return '<cg_bog_spring %r>' % (self.campground)

    class cg_rose_canyon(db.Model):
        __tablename__ = 'cg_rose_canyon'

        id = db.Column(db.Integer, primary_key=True)
        campground = db.Column(db.String(255))
        forecasted_temperature_degF = db.Column(db.Float)
        forecastTime_temperature = db.Column(db.Date)
        forecasted_windSpeed_miles_per_h = db.Column(db.Float)
        forecastTime_windSpeed = db.Column(db.Date)
        forecasted_windGust_miles_per_h = db.Column(db.Float)
        forecastTime_windGust = db.Column(db.Date)
        forecasted_probabilityOfPrecipitation = db.Column(db.Float)
        forecastTime_probabilityOfPrecipitation = db.Column(db.Date)
        forecasted_quantityOfPrecipitation_mm = db.Column(db.Float)
        forecastTime_quantityOfPrecipitation = db.Column(db.Date)

        def __repr__(self):
            return '<cg_rose_canyon %r>' % (self.campground)


    class cg_spencer_canyon(db.Model):
        __tablename__ = 'cg_spencer_canyon'

        id = db.Column(db.Integer, primary_key=True)
        campground = db.Column(db.String(255))
        forecasted_temperature_degF = db.Column(db.Float)
        forecastTime_temperature = db.Column(db.Date)
        forecasted_windSpeed_miles_per_h = db.Column(db.Float)
        forecastTime_windSpeed = db.Column(db.Date)
        forecasted_windGust_miles_per_h = db.Column(db.Float)
        forecastTime_windGust = db.Column(db.Date)
        forecasted_probabilityOfPrecipitation = db.Column(db.Float)
        forecastTime_probabilityOfPrecipitation = db.Column(db.Date)
        forecasted_quantityOfPrecipitation_mm = db.Column(db.Float)
        forecastTime_quantityOfPrecipitation = db.Column(db.Date)

        def __repr__(self):
            return '<cg_spencer_canyon %r>' % (self.campground)

    return camp_wx, cg_bog_spring, cg_rose_canyon, cg_spencer_canyon
