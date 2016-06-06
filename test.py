from naverWeather import *
l = naverWeather.map_cityNum.keys()
print(naverWeather().getWeather())
for s in l :
    print(naverWeather(s).getWeather())
