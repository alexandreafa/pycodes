# pip install folium

import folium

# create the map
map = folium.Map(
    location=[51.1788675,-1.8263168],
    tiles='Stamen Terrain', # map style
    zoom_start=16
)

# add marker
folium.Marker(
    [51.1788675,-1.8263168],
    popup='<i>Stonehenge</i>',
    tooltip='Click here!'
).add_to(map)

# save in html
map.save('map.html')