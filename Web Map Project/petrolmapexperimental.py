#first import folium and pandas
import pandas
import folium
from folium.map import *

#store data in a variable from csv
dataframe = pandas.read_csv("CardSites.csv")

#create a map oject
map = folium.Map(location=[dataframe['Lat'].mean(),dataframe['Long'].mean()],zoom_start=8,tiles="Stamen Terrain")

#create groups to toggle on/off
shellgroup = FeatureGroup(name="Shell Sites")
texacogroup = FeatureGroup(name="Texaco Sites")
essogroup = FeatureGroup(name="Esso Sites")

#loop over the data in the dataframe
for lat,lon,name,company in zip(dataframe['Lat'],dataframe['Long'],dataframe['SiteName'],dataframe['Company']):
    #create marker(s)
    if company == "Shell":
        shellgroup.add_child(folium.Marker(location=[lat,lon],popup=name,icon=folium.Icon(color='green')))
        print("Added Shell {} to the map!".format(name))
    elif company == "Esso":
        essogroup.add_child(folium.Marker(location=[lat,lon],popup=name,icon=folium.Icon(color='red')))
        print("Added Esso {} to the map!".format(name))
    elif company == "Texaco":
        texacogroup.add_child(folium.Marker(location=[lat,lon],popup=name,icon=folium.Icon(color='black')))
        print("Added Texaco {} to the map!".format(name))
    else:
        map.add_child(folium.Marker(location=[lat,lon],popup=name,icon=folium.Icon(color='blue')))
        print("Added {} to the map!".format(name))

# add the feature group to the map
map.add_children(shellgroup)
map.add_children(essogroup)
map.add_children(texacogroup)
# add a layer controller
map.add_children(folium.map.LayerControl())

#save the map file
map.save(outfile="xmopetrolmapexperimental.html")
print("Map Saved to xmopetrolmapexperimental.html")
