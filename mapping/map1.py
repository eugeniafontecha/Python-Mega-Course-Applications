import folium
import pandas as pd

data = pd.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

def color_producer(elevation):
    if elevation < 1500:
        return 'green'
    elif 1500 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'
##simple popup

map = folium.Map(location=[-34.42,-58.82], zoom_start=6, tiles = "Stamen Terrain")

fg = folium.FeatureGroup(name="My Map")

for lt,ln,el in zip(lat,lon,elev):
    fg.add_child(folium.Marker(location=[lt,ln], popup=str(el)+" m", icon=folium.Icon(color=color_producer(el))))


map.add_child(fg)

map.save("Map1.html")

#sin hacerlo con feature group:
#map.add_child(folium.Marker(location=[-34,-58], popup="Hi, I'm a marker", icon=folium.Icon(color='green')))

