from geopy.distance import distance, vincenty
import json
import csv

vivod = {}
with open('data.json', 'r', encoding='Windows-1251') as fh:
    data = json.load(fh)
with open('data2.json', 'r', encoding='Windows-1251') as fh1:
    data1 = json.load(fh1)
    for station1 in data:
        lon1 = float(station1["Longitude_WGS84"])
        lat1 = float(station1["Latitude_WGS84"])
        geo1 = (lon1, lat1)
        n = 0
        for row in data1:
            lon2 = float(row["Longitude_WGS84"])
            lat2 = float(row["Latitude_WGS84"])
            geo2 = (lon2, lat2)
            dist2 = vincenty(geo1, geo2).km
            # print(station1['Name'], dist,' ' ,dist2)
            if dist2 <= 0.5:
                n += 1
                # print('o.5')
                # print(dist2)
        vivod[station1['Name']] = n

# print(vivod)
vivod_max = [k for k,v in vivod.items() if v==max(vivod.values())][0]
print(vivod_max)