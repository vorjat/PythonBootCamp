import json
import urllib.request
import sys
import tkinter


def getWeather():
    cityname = cityEntry.get()
    link = "https://www.metaweather.com//api/location/search/?query=" + cityname

    with urllib.request.urlopen(link) as f:
        temp = json.loads(f.read())

    id = temp[0]['woeid']

    link2 = "https://www.metaweather.com/api/location/" + str(id) + "/"
    # print(link2)
    with urllib.request.urlopen(link2) as f:
        temp2 = json.loads(f.read())

    minTempEntry.configure(text=temp2['consolidated_weather'][0]['min_temp'])
    maxTempEntry.configure(text=temp2['consolidated_weather'][0]['max_temp'])

root = tkinter.Tk()
cityLabel = tkinter.Label(master=root, text="City name:")
cityLabel.grid(row=0, column=0)
cityEntry = tkinter.Entry(master=root)
cityEntry.grid(row=0, column=1)

policz_button = tkinter.Button(master=root, text="Get temperatures", command=getWeather)
policz_button.grid(row=1, column=0)

minTempLabel = tkinter.Label(master=root, text="Min temperature:")
minTempLabel.grid(row=2, column=0)
minTempEntry = tkinter.Label(master=root, text="-")
minTempEntry.grid(row=2, column=1)
maxTempLabel = tkinter.Label(master=root, text="Max temperature:")
maxTempLabel.grid(row=3, column=0)
maxTempEntry = tkinter.Label(master=root, text="-")
maxTempEntry.grid(row=3, column=1)

root.title("Weather")
root.mainloop()
