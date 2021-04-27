import requests
from bs4 import BeautifulSoup
import re


class co19Stat():
    session = requests.Session()
    map_cityNum = {  # 지역 번호 매핑
        '서울': 0, '부산': 1, '대구': 2, '인천': 3, '광주': 4, '대전': 5, '울산': 6,
        '세종': 7, '경기': 8, '강원': 9, '충북': 10, '충남': 11, '전북': 12, '전남': 13,
        '경북': 14, '경남': 15, '제주': 16
    }

    def __init__(self, area="대구"):
        self.area = area
        self.addr = "http://ncov.mohw.go.kr/bdBoardList_Real.do?brdId=1&brdGubun=13&ncvContSeq=&contSeq=&board_id=&gubun="
        self.cityNum = co19Stat.map_cityNum[area]
        self.result = None

        self.search()

    def search(self):
        co19Stat.session.encoding = 'UTF-8'

        req = co19Stat.session.get(self.addr)
        soup = BeautifulSoup(req.text, "html.parser")

        list1 = soup.find_all('span', {'class': 'num'})  # list1 = 누적 확신자
        list2 = soup.find_all('span', {'class': 'before'})  # list2 = 신규 확신자

        self.result = (
             "\n\n[" + self.area + " covid-19 현황]"
             + "\n\n현재 확인자(전일대비) : "+ list1[self.cityNum].get_text() + list2[self.cityNum].get_text()
             +""
        )

    def getStat(self):
        if not self.result:
            # 도시명을 잘못 입력한 경우 결과가 나오지 않는다.
            return "잘못된 도시명입니다"
        return self.result
