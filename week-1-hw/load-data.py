import pandas as pd
import psycopg2
from sqlalchemy import create_engine

conn = psycopg2.connect(
    host="localhost",
    database="de-zoomcamp",
    user="postgres",
    password="postgres"
)
cursor = conn.cursor()

def create_table():
    cursor.execute(f"""
    CREATE TABLE IF NOT EXISTS green_trip (
        vendorid INTEGER,
        lpep_pickup_datetime TIMESTAMP,
        lpep_dropoff_datetime TIMESTAMP,
        store_and_fwd_flag CHAR(1),
        ratecodeid INTEGER,
        pulocationid INTEGER,
        dolocationid INTEGER,
        passenger_count INTEGER,
        trip_distance FLOAT,
        fare_amount FLOAT,
        extra FLOAT,
        mta_tax FLOAT,
        tip_amount FLOAT,
        tolls_amount FLOAT,
        ehail_fee FLOAT,
        improvement_surcharge FLOAT,
        total_amount FLOAT,
        payment_type INTEGER,
        trip_type INTEGER,
        congestion_surcharge FLOAT
    );
    """)
    conn.commit()
    
    
def extract():
    df = pd.read_csv("./green_tripdata_2019-09.csv")
    print(df.head())
    return df


def load(df: pd.DataFrame):
    connection_str = "postgresql://postgres:postgres@localhost:5432/de-zoomcamp"
    engine = create_engine(connection_str)
    table_name = "green_trip"
    
    df.to_sql(table_name, con=engine, if_exists="replace", index=False)
    print("Data Loaded Successfully!!!")
    
    
extracted_df = extract()
load(extracted_df)