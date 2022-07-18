import os

if __name__=="__main__":
    print("HELLO FISHEYE EPA!")
    epa_zipfile_list = "../epa_zipfile_list.csv"
    with open(epa_zipfile_list, 'r') as f:
        for line in f.readlines():
            print(line)