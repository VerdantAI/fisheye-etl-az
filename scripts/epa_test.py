import os, glob
import wget
import zipfile


def download_and_unzip(wget_filelist, dir):
    with open(wget_filelist, 'r') as f:
        for line in f.readlines():
            print(line)
            g = wget.download(line, out=EPA_TMP_DIR)
            with zipfile.ZipFile(g) as z:
                z.extractall(dir)

def process_downloaded_files(dir):
    for file in glob.glob(dir + "/*.csv"):
        print(file)


if __name__=="__main__":
    print("HELLO FISHEYE EPA!  Run from the Fisheye ETL root directory.  This grabs a LOT of data, so be patient.")
    epa_zipfile_list = "./epa/file_list.csv"
    EPA_TMP_DIR = "epa_tmp"
    try:
        tdir = os.mkdir(EPA_TMP_DIR)
    except:
        "Tmp dir already exists"
    # Just commit out if you have run this already
    #download_and_unzip(epa_zipfile_list, EPA_TMP_DIR)
    process_downloaded_files(EPA_TMP_DIR)
    


    #os.rmdir(EPA_TMP_DIR)