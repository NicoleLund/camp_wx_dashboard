def create_classes(db):
    class camp_data(db.Model):
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
        nws_meta_json = db.Column(db.String(65535))
        nws_grid_json = db.Column(db.String(65535))
        fire_danger = db.Column(db.String(50))
        map_code = db.Column(db.String(255))


        def __repr__(self):
            return '<camp_data %r>' % (self.campground)
    return camp_data
