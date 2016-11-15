#first import folium
import folium

#create a map oject
map = folium.Map(location=[45.372,-121.697],zoom_start=12,tiles="Stamen Terrain")
#create marker(s)
map.simple_marker(location=[45.3288,-121.6625],popup='Mt. Hood Meadows',marker_color='red')
map.simple_marker(location=[45.3311,-121.7311],popup='Timberlake Lodge',marker_color='green')

#save the map file
map.save(outfile="map1.html")
