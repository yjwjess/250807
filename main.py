import streamlit as st

st.set_page_config(page_title="MBTI 추천기")

st.markdown("""
    <style>
    body {
        font-family: sans-serif;
        background-color: #f9f9f9;
    }
    </style>
""", unsafe_allow_html=True)

st.title("MBTI 직업 및 취미 추천기")

mbti = st.selectbox("MBTI 유형을 선택하세요", [
    "", "INTJ", "INTP", "ENTJ", "ENTP", "INFJ", "INFP", "ENFJ", "ENFP",
    "ISTJ", "ISFJ", "ESTJ", "ESFJ", "ISTP", "ISFP", "ESTP", "ESFP"
])

data = {
    "INTJ": {"job": "전략 컨설턴트, 데이터 과학자", "hobby": "체스, 독서, 퍼즐"},
    "INTP": {"job": "연구원, 개발자", "hobby": "코딩, 철학 토론, 보드게임"},
    "ENTJ": {"job": "CEO, 프로젝트 매니저", "hobby": "리더십 활동, 경영 서적 읽기"},
    "ENTP": {"job": "창업가, 광고 기획자", "hobby": "즉흥 연설, 새로운 기술 탐색"},
    "INFJ": {"job": "상담가, 작가", "hobby": "글쓰기, 명상, 시 감상"},
    "INFP": {"job": "예술가, 사회복지사", "hobby": "시 쓰기, 음악 감상, 자연 산책"},
    "ENFJ": {"job": "교사, 사회 운동가", "hobby": "자원봉사, 팀 프로젝트"},
    "ENFP": {"job": "기획자, 콘텐츠 크리에이터", "hobby": "여행, 인터뷰, 브이로그"},
    "ISTJ": {"job": "회계사, 공무원", "hobby": "정리, 기록 정리, 역사 다큐 시청"},
    "ISFJ": {"job": "간호사, 보육교사", "hobby": "다이어리 꾸미기, 요리"},
    "ESTJ": {"job": "경영 관리자, 경찰", "hobby": "스포츠, 팀 조직 활동"},
    "ESFJ": {"job": "교사, 사회복지사", "hobby": "파티 기획, 친구와의 대화"},
    "ISTP": {"job": "엔지니어, 파일럿", "hobby": "기계 조립, 익스트림 스포츠"},
    "ISFP": {"job": "디자이너, 플로리스트", "hobby": "드로잉, 식물 키우기"},
    "ESTP": {"job": "영업, 마케팅 전문가", "hobby": "여행, 오토바이 타기"},
    "ESFP": {"job": "배우, 이벤트 기획자", "hobby": "무대 공연, 사진 찍기"},
}

if mbti and mbti in data:
    st.subheader(f"{mbti} 유형 추천")
    st.markdown(f"""
    **추천 직업**: {data[mbti]["job"]}  
    **추천 취미**: {data[mbti]["hobby"]}
    """)
