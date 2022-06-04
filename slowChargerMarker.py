import pandas as pd
import returnAddress
import folium as g
from folium.plugins import MarkerCluster


def slowChargerMarker(g_map):
    excel_source = pd.read_excel('C:/Users/cksdn/PycharmProjects/OSS_Project_04/result2.xlsx', usecols=[2])
    lat = []
    lng = []
for count in range(excel_source.shape[0]):
        chg_lat, chg_lng = returnAddress.getloc(str(excel_source.loc[count]))
        lat.append(chg_lat)
        lng.append(chg_lng)
    locations = list(zip(lat, lng))
    icons = [g.Icon(icon='glyphicon glyphicon-flash',
                    popup='Charging Station') for _ in range(len(locations))]
