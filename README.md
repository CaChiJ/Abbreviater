# Korean Abbreviater
글 축약 서비스입니다. 초기 개발버전은 http://34.64.192.127 에서 (한국 시간대인 UTC+9 기준으로)주말에 한해 호스팅 중입니다.

# 구조
파이썬의 cgi 모듈을 이용하여 페이지를 구성합니다. index.py의 form을 통해 입력된 정보는 analysis.py로 전달되며 Abbreviater 모듈을 통해 분석됩니다. Abbreviater는 1) 축약할 수 있는 지점 2) 대상 문자열 길이 3) 대체할 문자열로 구성되는 리스트들의 모음을 반환합니다. analysis.py에서는 이 결과를 바탕으로 사용자에게 축약 가능한 문자열을 정보를 제공합니다.

# 실행 환경
Debian 10 OS에서 올바른 작동을 보장합니다.

# 업데이트
2021.04.28 : 기초적인 웹페이지와 축약 모듈 생성

# 로드맵
1. 문자열 대체를 통한 축약 기능 강화
2. KoNLPy를 이용해 분석 기능 강화 및 정확도 개선
3. 결과 표시 화면 UX 디자인 개선(정적 -> 동적)
4. 맞춤법 검사 기능 삽입

# Task Board
Trello link : https://trello.com/b/NLLUHrtp/%EA%B8%80%EC%9E%90%EC%88%98-%EC%B6%95%EC%95%BD%EA%B8%B0
