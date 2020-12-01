# import dependencies
from flask import Flask, jsonify
import pandas as pd
import numpy as np
import datetime as dt
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
    
# Main
if __name__ == "__main__":
    app.run(debug=True)
