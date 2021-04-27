import requests
from bs4 import BeautifulSoup
import re

class naverWeather():
    session = requests.Session()
    addr = "https://weather.naver.com/today/"
    map_cityNum = {     # 지역 번호 매핑
            '백령':"11720330", '서울':"09140104", '춘천':"01110675", '강릉':'01150615','청주':"16111120" ,
            '수원':"07110101", '안동':"04170690", '울릉':"04940320", '독도':"04940320", '대전':"07110101",
            '전주':"13113135", '대구':"06110101", '광주':"05110101", '목포':'12110152', '울산':"10110101",
            '제주':"14130116", '여수':"12130127", '부산':"08110580"
            }

    def __init__(self, area="대구"):
        self.area = area
        self.addr = None
        self.result = None
        
        cityNum = naverWeather.map_cityNum[area]
        if not cityNum:
            print("도시명 잘못")
            # 잘못된 도시명을 입력한 경우
            return
        self.addr = naverWeather.addr + cityNum
        
        self.search()

    def search(self):
        naverWeather.session.encoding = 'UTF-8'

        req = naverWeather.session.get(self.addr)
        soup = BeautifulSoup(req.text, "html.parser")

        summary = soup.find('span', {'class': 'weather before_slash'}).text   # summary : 오늘 최종 날씨 요약
        now_temper = soup.find('strong', {'class': 'current'}).text           # now_temper : 현재온도
        now_list1 = soup.find_all('dd', {'class': 'desc'})                    # now_list1 : list(습도, 풍속, 체감온도)
        now_rain = now_list1[0].get_text()                                    # now_rain : 현재 습도
        now_humidity = now_list1[1].get_text()                                # now_humidity : 현재 강수 확률
        now_wind = now_list1[2].get_text()                                    # now_wind : 현재 풍속
        now_body = now_list1[3].get_text()                                    # now_body : 현재 체감 온도
        now_list2 = soup.find_all('em', {'class': 'level_text'})              # now_list2 : list(미세먼지, 초미세먼지, 자외선)
        now_dust1 = now_list2[0].get_text()                                   # now_dust1 : 현재 미세먼지
        now_dust2 = now_list2[1].get_text()                                   # now_dust2 : 현재 초미세먼지
        now_uv = now_list2[2].get_text()                                      # now_uv : 현재 자외선

        self.result = (
            "출처 : " + self.addr
                + "\n\n["+ self.area + " 날씨 검색 결과]\n"
                + now_temper + " ( " + summary + " )"
                + "\n강수 : " + now_rain
                + "\t습도 : " + now_humidity
                + "\n바람 : " + now_wind
                + "\t체감 : " + now_body
                + "\n미세먼지 : " + now_dust1
                + "\t초미세먼지 : " + now_dust2
                + "\t자외선 : " + now_uv
        )

    def getWeather(self):
        if not self.result:
            # 도시명을 잘못 입력한 경우 결과가 나오지 않는다.
            return "잘못된 도시명입니다"
        return self.result
