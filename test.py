from naverWeather import *
from co19Stat import *

print("지역을 입력하시오 : ")
area = input()
print(naverWeather(area).getWeather())
print(co19Stat(area).getStat())
print("\n\n\n[출처1] : " + naverWeather.addr + "\n[출처2] : " + co19Stat.dis_addr + "\n[출처3] : " + co19Stat.coronic_addr)






