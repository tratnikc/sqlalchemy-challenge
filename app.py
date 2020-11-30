from flask import Flask, jsonify
import pandas as pd
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect

# SQLAlchemy
engine = create_engine("sqlite:///Resources/hawaii.sqlite")
Base = automap_base()
Base.prepare(engine,reflect=True)
Measurement = Base.classes.measurement


#Flask
app = Flask(__name__)

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


if __name__ == "__main__":
    app.run(debug=True)
