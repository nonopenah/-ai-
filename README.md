# 가출 청소년을 위한 온라인 쉼터 '온기'
![chatbot_logo_small.png](https://github.com/nonopenah/chatbot-AI-for-runaway-teenager/blob/main/LogoPNG/chatbot_logo_small.png)
## 개요
- **온기**는 가출 청소년들이 직면하는 다양한 문제와 고민에 대해 도움을 주기 위해 설계된 온라인 챗봇입니다.
- 사용자는 챗봇과 대화를 통해 심리적 지원을 받고, 가까운 쉼터의 정보를 얻을 수 있습니다. <br><br>

## 주요 기능
**1. 챗봇 상담 기능**
- 사용자와 자연스러운 대화를 통해 심리적으로 도움을 줍니다.
- 사용자의 상황과 감정을 이해하고 적절한 조언을 제공합니다.
- 필요한 경우 추가적인 지원이 가능한 곳으로 안내합니다. <br>
  
**2. 근처 쉼터 정보 제공**
- 사용자의 위치를 입력 받아 가까운 쉼터나 기관의 정보를 제공합니다.
- 해당 쉼터의 주소, 연락처, 제공하는 서비스 등을 상세히 안내합니다. <br>
  
**3. 대화 기록 저장**
- 대화 스레드가 저장되어 지속적인 상담이 가능하도록 합니다.
- 사용자가 언제든지 이전 대화 내용을 참고할 수 있습니다. <br><br>

## 개발자 실행 방법
**<실행에 필요한 패키지 설치>**
   ```bash
   pip install openai
   pip install streamlit
   pip install Flask
```

**<터미널 실행 방법>**
  ```bash
  python "챗봇웹배포파일이름".py
  ```
이렇게 실행할 경우, local URL과 network URL이 발급됩니다.
이 URL을 공유하여 다른 사용자들도 챗봇을 사용하게 할 수 있습니다.

<br>

## 유저 사용 방법
1. 웹브라우저에 접속합니다.
   - 링크: http://localhost:8501
   (웹 서버가 켜져 있을 경우에만 가능)
     
2. 챗봇과 대화하며 고민을 나눕니다.
3. 필요 시 자신의 위치를 제공하고 근처 쉼터 정보를 얻습니다.
4. 위험 시그널이 감지될 경우, 챗봇이 잘못된 선택을 하지 않도록 관련 정보들을 제공해준다.

