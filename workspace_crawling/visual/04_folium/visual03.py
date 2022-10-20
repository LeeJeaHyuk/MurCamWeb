import folium
import json



starbucks_map = folium.Map(location=[37.34635118,126.98146812], zoom_start=14)

with open('./starbucks.json','r', encoding='utf-8') as file:
    starbucks_json = json.load(file)

# print(starbucks_json)

for starbucks in starbucks_json['list']:
    folium.Marker([starbucks['lat'], starbucks['lot']], popup=folium.Popup(starbucks['s_name'], max_width=100)).add_to(starbucks_map)

starbucks_map.save('starbucks.html')