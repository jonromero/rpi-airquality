"""
Reads json files from data/ and spits out a well-formatted csv

Jon V
"""

from os import walk
import json

PATH = "data/airquality_111/"

_, _, filename = walk(PATH).next()
f = open('result.csv', "w")

for filename in filename:

    dandt = filename.split(".json")[0]
    with open(PATH+filename) as f:
        data = json.load(f)

    avg_pm10 = (data[0]['pm10'] + data[1]['pm10'] + data[2]['pm10'])/3
    avg_pm25 = (data[0]['pm25'] + data[1]['pm25'] + data[2]['pm25'])/3

    f.writelines("%s;%s;%s", dandt, avg_pm10, avg_pm25)

f.close()
