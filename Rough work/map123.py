import folium
map=folium.Map(location=(12.58,77.48),zoom_start=6)
fg=folium.FeatureGroup(name="bangloremap")
fg.add_child(folium.Marker(location=(12.58,77.48),popup="banglore",icon=folium.Icon(color="red")))
fg.add_child(folium.Marker(location=(17.22,78.29),popup="hyderabad",icon=folium.Icon(color="green")))
fg.add_child(folium.Marker(location=(13.06,80.16),popup="chennai",icon=folium.Icon(color="pink")))
map.add_child(fg)

map.save('bmap.html')

import folium
import pandas
data=pandas.read_csv("new locations.csv")
lat=list(data["lat"])
lon=list(data["lon"])
map=folium.Map(location=(12.58,77.48),zoom_start=6)
fg=folium.FeatureGroup(name="bangloremap")
for lt,ll in zip(lat,lon):
    fg.add_child(folium.Marker(location=(lt,ll),icon=folium.Icon(color="red")))
map.add_child(fg)
map.save('bmap1.html')
