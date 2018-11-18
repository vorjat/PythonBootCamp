import json
import urllib.request
import sys
import tkinter
tkinter.Label(master=root, text="Parametr a")

#cityname = input ("City name: ")
cityname = sys.argv[1]
#cityname = "Warsaw"
link = "https://www.metaweather.com//api/location/search/?query=" + cityname

with urllib.request.urlopen(link) as f:
    temp = json.loads(f.read())

id = temp[0]['woeid']

link2 = "https://www.metaweather.com/api/location/" + str(id) + "/"
#print(link2)
with urllib.request.urlopen(link2) as f:
    temp2 = json.loads(f.read())

print(f"""Min temp:  {temp2['consolidated_weather'][0]['min_temp']}
Max temp:  {temp2['consolidated_weather'][0]['max_temp']}
""")
