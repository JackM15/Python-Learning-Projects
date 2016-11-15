#first import folium and pandas
import pandas
import folium

#store data in a variable from csv
dataframe = pandas.read_csv("Volcanoes-USA.txt")

#create a map oject
map = folium.Map(location=[dataframe['LAT'].mean(),dataframe['LON'].mean()],zoom_start=6,tiles="Stamen Terrain")

#loop over the data in the dataframe
for lat,lon,name in zip(dataframe['LAT'],dataframe['LON'],dataframe['NAME']):
    #create marker(s)
    map.add_child(folium.Marker(location=[lat,lon],popup=name,icon=folium.Icon(color='red')))

#save the map file
map.save(outfile="map2.html")
