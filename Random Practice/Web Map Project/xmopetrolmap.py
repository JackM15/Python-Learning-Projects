#first import folium and pandas
import pandas
import folium

#store data in a variable from csv
dataframe = pandas.read_csv("CardSites.csv")

#create a map oject
map = folium.Map(location=[dataframe['Lat'].mean(),dataframe['Long'].mean()],zoom_start=5,tiles="Stamen Terrain")

#loop over the data in the dataframe
for lat,lon,name,company in zip(dataframe['Lat'],dataframe['Long'],dataframe['SiteName'],dataframe['Company']):
    #create marker(s)
    if company == "Shell":
        map.add_child(folium.Marker(location=[lat,lon],popup=name,icon=folium.Icon(color='yellow')))
    elif company == "Esso":
        map.add_child(folium.Marker(location=[lat,lon],popup=name,icon=folium.Icon(color='red')))
    elif company == "Texaco":
        map.add_child(folium.Marker(location=[lat,lon],popup=name,icon=folium.Icon(color='black')))
    else:
        map.add_child(folium.Marker(location=[lat,lon],popup=name,icon=folium.Icon(color='blue')))

#save the map file
map.save(outfile="xmopetrolmap.html")
print("Map Saved to xmopetrolmap.html")
