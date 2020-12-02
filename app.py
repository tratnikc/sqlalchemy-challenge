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
Base.classes.keys()

# Reference tables
Measurement = Base.classes.measurement
Station = Base.classes.station


# Flask
app = Flask(__name__)

# dates
session = Session(engine)
latest_date = session.query(Measurement.date) \
                     .order_by(Measurement.date.desc()).first()
one_year = dt.datetime.strptime(*latest_date,"%Y-%m-%d") - timedelta(days=365)
session.close()

# Flask routes
# Home route
@app.route("/")
def welcome():
    return """
        <h1>Welcome to the Surf's Up website!</h1><br/>
        <strong>Available routes:</strong><br/>
          <ul>
            <li><a href="/api/v1.0/precipitation" target="_blank">/api/v1.0/precipitation</a></li>
            <li><a href="/api/v1.0/stations" target="_blank">/api/v1.0/stations</a></li>
            <li><a href="/api/v1.0/tobs" target="_blank">/api/v1.0/tobs</a></li>
            <li><a href="/api/v1.0/start" target="_blank">/api/v1.0/yyyymmdd </a></li>
            <li><a href="/api/v1.0/start/end" target="_blank">/api/v1.0/yyyymmdd/yyyymmdd </a></li>
          </ul>
    """

# Precipitation route
@app.route("/api/v1.0/precipitation")
def precipitation():
    session = Session(engine)
    results = session.query(Measurement.date, Measurement.prcp) \
                     .filter(Measurement.date >= one_year) \
                     .all()
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
#  .filter(Measurement.tobs.isnot(None)) \
    most_active = session.query(Measurement.station) \
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

# Start Date route
@app.route("/api/v1.0/<start>")
def start_day(start):
    session = Session(engine)
    results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)) \
                     .filter(func.strftime("%Y%m%d", Measurement.date) >= start ) \
                     .all()
    session.close()

    return jsonify(list(results))

# Start Date and End Date route
@app.route("/api/v1.0/<start>/<end>")
def start_end(start, end):
    session = Session(engine)
    results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)) \
                     .filter(func.strftime("%Y%m%d", Measurement.date) >= start) \
                     .filter(func.strftime("%Y%m%d", Measurement.date) <= end) \
                     .all()
    session.close()

    return jsonify(list(results))


# Main
if __name__ == "__main__":
    app.run(debug=True)
