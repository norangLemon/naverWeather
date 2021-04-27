from naverWeather import *
from co19Stat import *
from selenium import webdriver


print(naverWeather('대구').getWeather())
print(co19Stat('서울').getStat())

## driver = webdriver.Chrome(executable_path='/Users/ehdud/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Python 3.8/chromedriver.exe')




