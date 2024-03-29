import os, glob
import wget
import zipfile
from dotenv import load_dotenv
import psycopg2
import pandas as pd
from sqlalchemy import create_engine



def download_and_unzip(wget_filelist, dir):
    print("This grabs a LOT of data, so be patient.")
    with open(wget_filelist, 'r') as f:
        for line in f.readlines():
            print(line)
            g = wget.download(line, out=EPA_TMP_DIR)
            with zipfile.ZipFile(g) as z:
                z.extractall(dir)

def process_downloaded_files(dir):
    #conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD)
    conn_string = 'postgresql://{u}:{p}@127.0.0.1/{db}'.format(u=DB_USER, p=DB_PASSWORD, db=DB_NAME)
    print(conn_string)
    db = create_engine(conn_string)
    conn = db.connect()
    for file in glob.glob(dir + "/*.csv"):
        #print(DB_NAME)
        # Turn the file name into a table name
        tname = file.replace(EPA_TMP_DIR + "/", '').replace('.csv', '').replace('-', '_').lower().strip()
        print(file + "\t" + tname)
        #df = pd.read_csv(file)
        df = pd.read_csv(file, dtype={'REGISTRY_ID': 'str'
            , 'NAICS_CODE': 'str'
            , 'SRS_ID': 'str'
            , 'FAC_STATE': 'str'
            , 'FAC_ZIP': 'str'
            , 'POLLUTANT_CODES':'str'
            , 'PGM_SYS_ID': 'str'
            , 'NEI_TYPE': 'str'
            , 'NEI_HAP_VOC_FLAG': 'str'
            })
        try:
            df.to_sql(name=tname, con=conn, schema=EPA_SCHEMA, if_exists='fail')
        except:
            print("table {t} already exists".format(t=tname))


if __name__=="__main__":
    print("HELLO FISHEYE EPA!  Run from the Fisheye ETL root directory.")
    load_dotenv()
    
    # This hold environment data, including the local database information"
    epa_zipfile_list = "./epa/file_list.csv"
    EPA_TMP_DIR = os.getenv('EPA_TMP_DIR')
    DB_NAME = os.getenv("DB_NAME")
    DB_USER= os.getenv("DB_USER")
    DB_PASSWORD= os.getenv("DB_PASSWORD")
    EPA_SCHEMA = os.getenv("EPA_SCHEMA")
    try:
        tdir = os.mkdir(EPA_TMP_DIR)
    except:
        "Tmp dir already exists"
    # Just commit out if you have run this already
    #download_and_unzip(epa_zipfile_list, EPA_TMP_DIR)
    process_downloaded_files(EPA_TMP_DIR)
    


    #os.rmdir(EPA_TMP_DIR)