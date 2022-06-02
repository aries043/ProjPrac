import chargingMethod
import returnAddress
import findCurloc
import findDestination
import pandas as pd

chargingMethod.guide()

excel_source = pd.read_excel('C:/Users/cksdn/PycharmProjects/OSS_Project_04/전기차-충전소-설치현황_20220316.xlsx', usecols=[1, 2, 3, 4, 5])
print("Please enter the area where you want to find the location of the charging station. ex)청주")
str_want_go = input()
