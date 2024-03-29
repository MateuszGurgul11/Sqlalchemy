from sqlalchemy import create_engine
from sqlalchemy import Table, MetaData, Integer, Float, String, Column, PrimaryKeyConstraint
import csv

measure_file = "clean_measure.csv"
stations_file = "clean_stations.csv"

metadata = MetaData()

engine = create_engine('sqlite:///database.db', echo = True)

measure = Table(
    'measure', metadata,
    Column('station', String),
    Column('date', String),
    Column('precip', String),
    Column('tobs', Integer),
    PrimaryKeyConstraint('station', 'date')
)

stations = Table(
    'station', metadata,
    Column('station', String, primary_key = True),
    Column('latitude', Float),
    Column('longitude', Float),
    Column('elevation', Float),
    Column('name', String),
    Column('country', String),
    Column('state', String),
)

metadata.create_all(engine)

with engine.connect() as conn:
    with open(measure_file, 'r') as file:
            csv_reader = csv.reader(file, delimiter=',', quotechar='"')
            measure_data = [dict(zip(('station', 'date', 'precip', 'tobs'), row)) for row in csv_reader]
            conn.execute(measure.insert(), measure_data)

    with open(stations_file, 'r') as file:
            csv_reader = csv.reader(file, delimiter=',', quotechar='"')
            station_data = [dict(zip(('station', 'latitude', 'longitude', 'elevation', 'name', 'country', 'state'), row)) for row in csv_reader]
            conn.execute(stations.insert(), station_data)

with engine.connect() as conn:
    result = conn.execute("SELECT * FROM stations LIMIT 5").fetchall()
    for row in result:
        print(row)