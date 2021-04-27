naverWeather [![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
---
*used in: [SNUBot](https://github.com/norangLemon/snuBot)*

* [naver 날씨](https://weather.naver.com/), [코로나바이러스감염증-19](http://ncov.mohw.go.kr/) 정보를 크롤링합니다.

* 실행 : 지역 입력 시 해당 지역의 현재 날씨 정보와 COVID-19에 대한 정보를 얻을 수 있습니다.

* 실행 결과 :
```
[서울 날씨 검색 결과]
지역을 입력하시오 : 
대구

[대구 날씨 검색 결과]
현재 온도15° ( 흐림 )
강수 : 30%	습도 : 57%
바람 : 1m/s	체감 : 16°
미세먼지 : 좋음	초미세먼지 : 좋음	자외선 : 매우높음

뉴스 요약 코맨트
[날씨] 오늘 황사 유입...구름 많고 건조한 날씨
[날씨] 밤사이 서울 등 중부 지방 비...내일 황사 유입


[대구 covid-19 현황] (해당지역)

누적 확인자(전일대비) : 9,289(+12)
거리 두기 단계 : 1.5단계 (지역적 유행 단계)
개념 : 지역적 유행 개시
핵심 메세지 : 지역유행 시작, 위험지역은 철저한 생활방역
```
* 현재 적용 가능 지역 : 부산, 서울, 춘천, 강릉, 청주, 수원, 안동, 대전, 제주, 여수, 전주, 대구, 광주, 목포, 울산

* 주의 사항 : 해당 프로그램은 selenium의 기능을 포함하고 있습니다. Chrome driver를 기반으로 작성하였으며, co19Stat.py의 line.35의 driver path를 사용자에 따라 수정해야 할 필요가 있습니다