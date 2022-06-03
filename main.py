import chargingMethod
import returnAddress
import findCurloc
import findDestination
import pandas as pd
import folium as g
import findTheDistanceBetweenCoordinates as Dis
import chargingStationMarker

chargingMethod.guide()

excel_source = pd.read_excel('전기차-충전소-설치현황_20220316.xlsx', usecols=[1, 2, 3, 4, 5])
print("Please enter the area where you want to find the location of the charging station. ex)청주")
str_want_go = input()

int_line = excel_source['주소'].str.contains(str_want_go)
want_go_excel = excel_source[int_line]
want_go_excel.to_excel('result.xlsx', sheet_name= 'Result')

cur_lat = 0.0
cur_lng = 0.0
cur_lat, cur_lng = findCurloc.find()

excel_source = pd.read_excel('result.xlsx', usecols=[1, 2, 3, 4, 5])
print("Please enter the type of car you want. ex) 1\n"
      "1.SM3 Z.E, 2.레이EV, 3.소울EV, 4.닛산리프, 5.아이오닉EV, 6. BMW i3, 7.스파크EV, 8.볼트EV, 9.테슬라")
car = input()
if car == "1" :
    str_want_go = "SM3 Z.E"
    int_line = excel_source['지원차종'].str.contains(str_want_go)
elif car == "2" :
    str_want_go = "레이EV"
    int_line = excel_source['지원차종'].str.contains(str_want_go)
elif car == "3" :
    str_want_go = "소울EV"
    int_line = excel_source['지원차종'].str.contains(str_want_go)
elif car == "4" :
    str_want_go = "닛산리프"
    int_line = excel_source['지원차종'].str.contains(str_want_go)
elif car == "5" :
    str_want_go = "아이오닉EV"
    int_line = excel_source['지원차종'].str.contains(str_want_go)
elif car == "6" :
    str_want_go = "BMW i3"
    int_line = excel_source['지원차종'].str.contains(str_want_go)
elif car == "7" :
    str_want_go = "스파크EV"
    int_line = excel_source['지원차종'].str.contains(str_want_go)
elif car == "8" :
    str_want_go = "볼트EV"
    int_line = excel_source['지원차종'].str.contains(str_want_go)
elif car == "9" :
    str_want_go = "테슬라"
    int_line = excel_source['지원차종'].str.contains(str_want_go)
want_go_excel = excel_source[int_line]
want_go_excel.to_excel('result1.xlsx', sheet_name= 'Result')

dst_lat = 0.0
dst_lng = 0.0
dst_lat, dst_lng = findDestination.find()

g_map = g.Map(location=[dst_lat, dst_lng],
              zoom_start=20,
              tiles='http://api.vworld.kr/req/wmts/1.0.0/D05C77C9-AB62-3E70-9183-0E044A461BBD/Base/{z}/{y}/{x}.png',
              attr = 'VworldBase')

marker_cur = g.Marker([cur_lat, cur_lng],
            popup = 'The starting point',
            icon = g.Icon(color='green')).add_to(g_map)

marker_dst = g.Marker([dst_lat, dst_lng],
            popup = 'Destination',
            icon = g.Icon(color='red')).add_to(g_map)

location = [[cur_lat, cur_lng], 
            [dst_lat, dst_lng]]

g.PolyLine(locations=location, tooltip='a straight path').add_to(g_map)

chargingStationMarker.chargingStationMarker(g_map)

g_map.save('.destination_map.html')

print(Dis.GeoUtil.get_harversion_distance(cur_lng, cur_lat, dst_lng, dst_lat))
