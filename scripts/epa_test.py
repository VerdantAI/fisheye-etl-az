import os, glob
import wget
import zipfile
from dotenv import load_dotenv
import psycopg2



def download_and_unzip(wget_filelist, dir):
    print("This grabs a LOT of data, so be patient.")
    with open(wget_filelist, 'r') as f:
        for line in f.readlines():
            print(line)
            g = wget.download(line, out=EPA_TMP_DIR)
            with zipfile.ZipFile(g) as z:
                z.extractall(dir)

def process_downloaded_files(dir):
    for file in glob.glob(dir + "/*.csv"):
        print(DB_NAME)
        conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD)
        print(file)


if __name__=="__main__":
    print("HELLO FISHEYE EPA!  Run from the Fisheye ETL root directory.")
    load_dotenv()
    
    # This hold environment data, including the local database information"
    epa_zipfile_list = "./epa/file_list.csv"
    EPA_TMP_DIR = os.getenv('EPA_TMP_DIR')
    DB_NAME = os.getenv("DB_NAME")
    DB_USER= os.getenv("DB_USER")
    DB_PASSWORD= os.getenv("DB_PASSWORD")
    try:
        tdir = os.mkdir(EPA_TMP_DIR)
    except:
        "Tmp dir already exists"
    # Just commit out if you have run this already
    #download_and_unzip(epa_zipfile_list, EPA_TMP_DIR)
    process_downloaded_files(EPA_TMP_DIR)
    


    #os.rmdir(EPA_TMP_DIR)