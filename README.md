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
**<OpenAI API 사용>**<br>
  https://openai.com/index/openai-api/<br>
-  위의 OpenAI API 주소에서 key를 발급받을 수 있습니다.
-  발급받은 key를 ongi_bot.py의 'API_KEY' 부분에 입력합니다.
-  OpenAI API의 Dashboard에서 assistants를 생성한 후, ongi_bot.py의 "ASSISTANT_ID"에 assistant ID를 입력합니다.
-  OpenAI API의 Dashboard에서 assistants의 instruction에 챗봇의 목적에 따른 챗봇의 성격과 대화 흐름을 입력합니다.

**<실행에 필요한 패키지 설치>**
   ```bash
   pip install openai
   pip install streamlit
   pip install Flask
```
**<프로젝트 클론>**
   ```bash
   git clone https://github.com/nonopenah/chatbot-AI-for-runaway-teenager.git
```
**<터미널 실행 방법>**
  ```bash
  python ongi_web.py
  "ongi_web"자리에 만들어둔 웹배포 파일이름을 넣으면 됩니다.
```
- 이렇게 실행할 경우, local URL과 network URL이 발급됩니다.<br>
이 URL을 공유하여 다른 사용자들도 챗봇을 사용하게 할 수 있습니다.

- ongi_bot.py만을 실행시킬 경우에도 작동이 가능합니다.( 이 경우 실행 방법 코드는 streamlit run ongi_bot.py ) <br>
  그러나 이 방법은 다른 사용자들에게 url를 공유해도 다른 사용자들은 사용할 수 없습니다.<br>
  그렇기에 Flask를 이용해 웹 서버를 만드는 ongi_web.py를 실행시켜 다른 사용자들도 사용할 수 있게 해야 배포가 가능합니다.

<br>

## 유저 사용 방법
1. 웹브라우저에 접속합니다.
   - 링크: http://localhost:8501
   (웹 서버가 켜져 있을 경우에만 가능)
     
2. 챗봇과 대화하며 고민을 나눕니다.
3. 필요 시 자신의 위치를 제공하고 근처 쉼터 정보를 얻습니다.
4. 위험 시그널이 감지될 경우, 챗봇이 잘못된 선택을 하지 않도록 관련 정보들을 제공해줍니다.
<br><br>

## 결과 예시
**[고민 상담]**<br>
![result1.png](https://github.com/nonopenah/chatbot-AI-for-runaway-teenager/blob/main/resultPNG/result1.png)

**[쉼터 정보]**<br>
![result2.png](https://github.com/nonopenah/chatbot-AI-for-runaway-teenager/blob/main/resultPNG/result2.png)

**[위험 시그널]**<br>
![result3.png](https://github.com/nonopenah/chatbot-AI-for-runaway-teenager/blob/main/resultPNG/result3.png)
<br>
## 참고
**<참고 github>**<br>
URL: https://gist.github.com/youtube-jocoding/ba302959cc05af01a04edc6e864e2c09<br>

**<여성가족부 청소년 쉼터 현황_일부>**

| 쉼터 이름                | 지역   | 구      | 주소                                                         | 전화번호         | 
| ----------------------- | ------ | ------- | ------------------------------------------------------------ | ---------------- |
| 서울시립신림남자중장기청소년쉼터 | 서울    | 관악구   | 서울특별시 관악구 난곡로 24가길 54, 301호                    | 02-3281-7942     |
| 부산광역시여자단기청소년쉼터     | 부산    | 수영구   | 부산광역시 수영구 광안해변로 255번길 58(구. 부산광역시광역시 민락동165-7) | 051-756-0924     |
| 대구광역시남자중장기청소년쉼터   | 대구    | 수성구   | 대구광역시 수성구 들안로28길 70-26 (황금동) 1층             | 053-426-2275     |


## 프로젝트 팀 구성원
| 이름          | GitHub 사용자명                              | 기여 내용                          |
| --------------- | ------------------------------------------- | ---------------------------------- |
| 이유민(팀장)    | [YUM1yum](https://github.com/YUM1yum) |  챗봇 서비스 로직 코드 구현  |
| 김나희          | [nonopenah](https://github.com/nonopenah) |  데이터 수집, UI 구성  |
| 박다인          | [qkrekdls](https://github.com/qkrekdls)        |  데이터 전처리, 웹 배포  |
