from os import mkdir
from os.path import exists, join
import urllib.request as request
from zipfile import ZipFile

import pandas as pd
from io import BytesIO

datadir = "data"
if not exists(datadir):
    mkdir(datadir)

if not exists("scripts/tmp"):
    mkdir("scripts/tmp")

source = "https://download.geonames.org/export/dump/"
dl = "http://download.geonames.org/export/dump/%s.zip"
cache = join("scripts/tmp", "main.html")

names = "geonameid,name,asciiname,alternatenames,latitude,longitude,feature class,feature code,country code,cc2,admin1 code,admin2 code,admin3 code,admin4 code,population,elevation,dem,timezone,modification date".split(",")
def retrieve():
    name = "cities500"
    z = request.urlopen(dl % name)
    myzip = ZipFile(BytesIO(z.read())).extract('%s.txt' % name)
    d = pd.read_csv(myzip, delimiter="\t", names=names)
    d.to_csv("data/%s.csv" % name, index=False)


def process():
    retrieve()

if __name__ == "__main__":
    process()
