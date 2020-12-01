# import dependencies
from flask import Flask, jsonify
import pandas as pd
import numpy as np
import datetime as dt
from datetime import date, timedelta
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect

# SQLAlchemy
engine = create_engine("sqlite:///Resources/hawaii.sqlite")
Base = automap_base()
Base.prepare(engine,reflect=True)

# Reference tables
Measurement = Base.classes.measurement
Station = Base.classes.station


# Flask
app = Flask(__name__)

# dates
session = Session(engine)
latest_date = session.query(Measurement.date) \
                     .order_by(Measurement.date.desc()).first()
print(latest_date)
one_year = dt.datetime.strptime(*latest_date,"%Y-%m-%d") - timedelta(days=365)
print(one_year)
session.close()

# Flask routes
# Home route
@app.route("/")
def welcome():
    return (
        f"<h1>Welcome to the Surf's Up website!</h1><br/>"
        f"<strong>Available routes:</strong><br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start=yyyy-mm-dd<br/>"
        f"/api/v1.0/start=yyyy-mm-dd/end=yyyy-mm-dd<br/>"
    )

# Precipitation route
@app.route("/api/v1.0/precipitation")
def precipitation():
    session = Session(engine)
    results = session.query(Measurement.date, Measurement.prcp).all()
    session.close()

    precip = []
    for date, prcp in results:
        precip_dict = {}
        precip_dict['date'] = date
        precip_dict['prcp'] = prcp
        precip.append(precip_dict)

    return jsonify(precip)

# Station route
@app.route("/api/v1.0/stations")
def station():
    session = Session(engine)
    results = session.query(Station.station).all()
    session.close()
    stns = list(np.ravel(results))

    return jsonify(stns)

# tobs route
@app.route("/api/v1.0/tobs")
def tobs():
    session = Session(engine)
    most_active = session.query(Measurement.station) \
                         .filter(Measurement.tobs.isnot(None)) \
                         .group_by(Measurement.station) \
                         .order_by(func.count(Measurement.station).desc()) \
                         .first()
    
    results = session.query(Measurement.date, Measurement.tobs) \
                     .filter(Measurement.station == most_active.station) \
                     .filter(Measurement.date >= dt.datetime.strftime(one_year,"%Y-%m-%d")) \
                     .order_by(Measurement.date) \
                     .all()
    session.close()

    return jsonify(list(results))


# Main
if __name__ == "__main__":
    app.run(debug=True)
