import folium
from numpy import FLOATING_POINT_SUPPORT
import pandas as pd

data = pd.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

with open("world.json",'r', encoding='utf-8-sig') as myfile:
    data = myfile.read()

def color_producer(elevation):
    if elevation < 1500:
        return 'green'
    elif 1500 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'
##simple popup

map = folium.Map(location=[-34.42,-58.82], zoom_start=6, tiles = "Stamen Terrain")

fgv = folium.FeatureGroup(name="Volcanoes")

for lt,ln,el in zip(lat,lon,elev):
    fgv.add_child(folium.CircleMarker(location=[lt,ln], radius=6, popup=str(el)+" m", color= 'grey',
                    fill_color= color_producer(el), fill_opacity = 0.7, fill=True))    

fgp = folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(data=data, style_function=lambda x: {'fillColor': 'green' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl()) #busca objetos agregados al map. Un fg lo toma como un obejto

map.save("Map1_circles.html")

#sin hacerlo con feature group:
#map.add_child(folium.Marker(location=[-34,-58], popup="Hi, I'm a marker", icon=folium.Icon(color='green')))

