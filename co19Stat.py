import requests
from bs4 import BeautifulSoup
import re
from selenium import webdriver


class co19Stat():
    session = requests.Session()
    coronic_addr = "http://ncov.mohw.go.kr/bdBoardList_Real.do?brdId=1&brdGubun=13&ncvContSeq=&contSeq=&board_id=&gubun="   # 현재 확진자 수 url
    dis_addr = "http://ncov.mohw.go.kr/regSocdisBoardView.do?brdId=6&brdGubun=68&ncvContSeq=495"                            # 거리 두기 단계 url
    map_cityNum = {  # 지역 번호 매핑
        '서울': 0, '부산': 1, '대구': 2, '인천': 3, '광주': 4, '대전': 5, '울산': 6, '세종': 7, '경기': 8, '수원': 8,
        '강원': 9, '춘천': 9, '강릉': 9, '충북': 10, '청주': 10, '충남': 11, '전북': 12, '전주': 12, '전남': 13,
        '목포': 13, '여수': 13, '경북': 14, '안동': 14, '경남': 15, '제주': 16
    }

    def __init__(self, area="대구"):
        self.area = area
        self.cityNum = co19Stat.map_cityNum[area]
        self.result = None

        self.search()

    def search(self):
        co19Stat.session.encoding = 'UTF-8'

        req1 = co19Stat.session.get(self.coronic_addr)
        soup1 = BeautifulSoup(req1.text, "html.parser")

        coronic_list1 = soup1.find_all('span', {'class': 'num'})     # coronic_list1 = 누적 확신자
        coronic_list2 = soup1.find_all('span', {'class': 'before'})  # coronic_list2 = 신규 확신자


        # selenium 사용, chrome기준, cromedriver의 경로
        driver = webdriver.Chrome(executable_path='cromedriver의 경로')
        link = self.dis_addr.format(1)
        driver.get(link)
        driver.implicitly_wait(0.5)             # 사용자의 네트워크 환경 및 CPU 사양에 따라 값 조정
        html = driver.page_source
        soup2 = BeautifulSoup(html, "html.parser")

        dis_list = soup2.find_all('span', {'class': 'num'})  # dis_list = 거리 두기 단계 리스트
        dis_stage = dis_list[self.cityNum].get_text()        # dis_stage = 현재 거리 두기 단계
        if (dis_stage=='1') :
            sortation = "생활방역"
            concept = "생활 속 거리 두기"
            core_message = "일상생활과 사회경제적 활동을 유지하면서, 코로나19 예방을 위해 방역수칙 준수"
        elif (dis_stage=='1.5') :
            sortation = "지역적 유행 단계"
            concept = "지역적 유행 개시"
            core_message = "지역유행 시작, 위험지역은 철저한 생활방역"
        elif (dis_stage == '2'):
            sortation = "지역적 유행 단계"
            concept = "지역 유행 급속 전파, 전국적 확산 개시"
            core_message = "지역유행 본격화, 위험지역은 불필요한 외출과 모임 자제, 사람이 많이 모이는 다중이용시설 이용 자제"
        elif (dis_stage == '2.5'):
            sortation = "전국적 유행 단계"
            concept = "전국적 유행 본격화"
            core_message = "전국 유행 확산, 가급적 집에 머무르며 외출·모임과 다중이용시설 이용을 최대한 자제"
        else:
            sortation = "전국적 유행 단계"
            concept = "전국적 대유행"
            core_message = "전국적 대유행, 원칙적으로 집에 머무르며 다른 사람과 접촉 최소화"

        self.result = (
             "\n\n[" + self.area + " covid-19 현황] (해당지역)"
             + "\n\n누적 확인자(전일대비) : " + coronic_list1[self.cityNum].get_text() + coronic_list2[self.cityNum].get_text()
             + "\n거리 두기 단계 : " + dis_stage + "단계 (" + sortation + ")"
             + "\n개념 : "+ concept
             + "\n핵심 메세지 : " + core_message

        )

    def getStat(self):
        if not self.result:
            # 도시명을 잘못 입력한 경우 결과가 나오지 않는다.
            return "잘못된 도시명입니다"
        return self.result
