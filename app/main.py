# import pandas as pd
# from fastapi import FastAPI
# from fastapi import FastAPI, File, UploadFile
# import psycopg2
# import csv
# from typing import Optional
# from pydantic import BaseModel
# import asyncpg
# from datetime import datetime

# app = FastAPI()
csv_file_path = "app/Backend_assignment_gg_dataset.csv"  
# df = pd.read_csv(csv_file_path)
# print(df.head(1))


# DATABASE_URL = "postgresql://vetgelns:ojOrPasEQ1Y-9gulxIQsV5h3naTDyJK8@satao.db.elephantsql.com/vetgelns"


# # class Events(BaseModel):
# #     event_name: str
# #     city_name: str
# #     date: str
# #     time: str
# #     latitude: float
# #     longitude: float



# from fastapi import FastAPI, HTTPException
# from sqlalchemy import create_engine, Column, Integer, String, DateTime, Float
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker
# import csv

# app = FastAPI()

# Base = declarative_base()

# class Event(Base):
#     __tablename__ = 'event'
#     id = Column(Integer, primary_key=True, index=True)
#     event_name = Column(String, index=True)
#     city_name = Column(String, index=True)
#     date = Column(DateTime)
#     time = Column(String)
#     latitude = Column(Float)
#     longitude = Column(Float)

# engine = create_engine(DATABASE_URL)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# @app.get("/add_events/")
# async def add_events_from_csv():
#     try:
#         with open(csv_file_path, mode='r') as csv_file:
#             csv_reader = csv.DictReader(csv_file)
#             db = SessionLocal()
#             for row in csv_reader:
#                 event = Event(event_name=row['event_name'],
#                               city_name=row['city_name'],
#                               date=row['date'],
#                               time=row['time'],
#                               latitude=row['latitude'],
#                               longitude=row['longitude'])
#                 db.add(event)
#             db.commit()
#             return {"message": "Events added successfully"}
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))

import pandas as pd
from fastapi import FastAPI, HTTPException
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import csv

# Remove duplicate app definition
app = FastAPI()

Base = declarative_base()

class Event(Base):
    __tablename__ = 'event'
    id = Column(Integer, primary_key=True, index=True)
    event_name = Column(String, index=True)
    city_name = Column(String, index=True)
    date = Column(DateTime)
    time = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)

DATABASE_URL = "postgresql://vetgelns:ojOrPasEQ1Y-9gulxIQsV5h3naTDyJK8@satao.db.elephantsql.com/vetgelns"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(engine)  


def add_events_from_csv():
    try:
        with open(csv_file_path, mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            db = SessionLocal()
            for row in csv_reader:
                event = Event(event_name=row['event_name'],
                              city_name=row['city_name'],
                              date=row['date'],
                              time=row['time'],
                              latitude=row['latitude'],
                              longitude=row['longitude'])
                db.add(event)
            db.commit()
            return {"message": "Events added successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/add_events/")
def start_adding_events():
    add_events_from_csv()
    return {"message": "Event addition process started"}


