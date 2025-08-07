<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8" />
  <title>MBTI 직업 및 취미 추천기</title>
  <style>
    body {
      font-family: sans-serif;
      padding: 2em;
      max-width: 600px;
      margin: auto;
      background-color: #f9f9f9;
    }

    h1 {
      color: #333;
      text-align: center;
    }

    label, select, p {
      display: block;
      margin: 1em 0;
    }

    #result {
      padding: 1em;
      background: #e0f7fa;
      border-radius: 8px;
    }
  </style>
</head>
<body>
  <h1>MBTI 추천기</h1>
  <label for="mbti">MBTI 유형을 선택하세요:</label>
  <select id="mbti">
    <option value="">-- 선택 --</option>
    <option value="INTJ">INTJ</option>
    <option value="INTP">INTP</option>
    <option value="ENTJ">ENTJ</option>
    <option value="ENTP">ENTP</option>
    <option value="INFJ">INFJ</option>
    <option value="INFP">INFP</option>
    <option value="ENFJ">ENFJ</option>
    <option value="ENFP">ENFP</option>
    <option value="ISTJ">ISTJ</option>
    <option value="ISFJ">ISFJ</option>
    <option value="ESTJ">ESTJ</option>
    <option value="ESFJ">ESFJ</option>
    <option value="ISTP">ISTP</option>
    <option value="ISFP">ISFP</option>
    <option value="ESTP">ESTP</option>
    <option value="ESFP">ESFP</option>
  </select>

  <div id="result"></div>

  <script>
    const data = {
      INTJ: { job: "전략 컨설턴트, 데이터 과학자", hobby: "체스, 독서, 퍼즐" },
      INTP: { job: "연구원, 개발자", hobby: "코딩, 철학 토론, 보드게임" },
      ENTJ: { job: "CEO, 프로젝트 매니저", hobby: "리더십 활동, 경영 서적 읽기" },
      ENTP: { job: "창업가, 광고 기획자", hobby: "즉흥 연설, 새로운 기술 탐색" },
      INFJ: { job: "상담가, 작가", hobby: "글쓰기, 명상, 시 감상" },
      INFP: { job: "예술가, 사회복지사", hobby: "시 쓰기, 음악 감상, 자연 산책" },
      ENFJ: { job: "교사, 사회 운동가", hobby: "자원봉사, 팀 프로젝트" },
      ENFP: { job: "기획자, 콘텐츠 크리에이터", hobby: "여행, 인터뷰, 브이로그" },
      ISTJ: { job: "회계사, 공무원", hobby: "정리, 기록 정리, 역사 다큐 시청" },
      ISFJ: { job: "간호사, 보육교사", hobby: "다이어리 꾸미기, 요리" },
      ESTJ: { job: "경영 관리자, 경찰", hobby: "스포츠, 팀 조직 활동" },
      ESFJ: { job: "교사, 사회복지사", hobby: "파티 기획, 친구와의 대화" },
      ISTP: { job: "엔지니어, 파일럿", hobby: "기계 조립, 익스트림 스포츠" },
      ISFP: { job: "디자이너, 플로리스트", hobby: "드로잉, 식물 키우기" },
      ESTP: { job: "영업, 마케팅 전문가", hobby: "여행, 오토바이 타기" },
      ESFP: { job: "배우, 이벤트 기획자", hobby: "무대 공연, 사진 찍기" },
    };

    document.getElementById("mbti").addEventListener("change", function () {
      const selected = this.value;
      const resultDiv = document.getElementById("result");

      if (data[selected]) {
        resultDiv.innerHTML = `
          <h3>${selected} 유형 추천</h3>
          <p><strong>직업:</strong> ${data[selected].job}</p>
          <p><strong>취미:</strong> ${data[selected].hobby}</p>
        `;
      } else {
        resultDiv.innerHTML = "";
      }
    });
  </script>
</body>
</html>
