import os
from openai import OpenAI
import streamlit as st
import time

# 발급 받은 인증 키를 코드에 입력
API_KEY = 'API_KEY'  

#API 호출을 위해 OpenAI 클라이언트 생성
client = OpenAI(api_key=API_KEY)


# thread id를 하나로 관리하기 위함
if 'thread_id' not in st.session_state:
    thread = client.beta.threads.create() # 새로운 스레드 생성
    st.session_state.thread_id = thread.id  # 생성된 스레드 ID를 계속 사용하여 대화의 연속성 유지
thread_id = st.session_state.thread_id #이미 생성된 스레드 ID가 있는 경우 재사용

# 특정한 대화 에이전트를 지정하기 위해 OpenAI API에서 사용할 어시스턴드 ID를 설정
assistant_id = "asst_j4TpIYX2pAK7JarO71cGJ5Dr"

# 현재 대화 스레드의 모든 메세지 불러오기
thread_messages = client.beta.threads.messages.list(thread_id)

# 페이지 제목 및 로고
col1, col2 = st.columns([1, 5])
with col1:
    st.image("ongi_image.png", width=100)  # 로고 이미지 경로와 크기 설정
with col2: # HTML 코드를 사용해 페이지 제목과 소제목을 표시
    # h1: 제목, p: 소제목
    st.markdown("""
        <div style="display: flex; flex-direction: column; justify-content: center; margin-top: 10px;">
            <h1 style='display: inline; vertical-align: middle; margin-bottom: 0;'>온기</h1>
            <p style='margin-top: 5px;'>청소년들을 위한 온라인 쉼터</p>
        </div>
    """, unsafe_allow_html=True) # HTML을 안전하게 사용하기 위함


# 현재 스레드에 저장된 메세지들을 역순으로 불러와 이전 대화 내용을 UI에 표시
for msg in reversed(thread_messages.data):
    with st.chat_message(msg.role):
        st.write(msg.content[0].text.value)

# 입력창에 입력을 받아서 OpenAI API를 통해 처리할 수 있도록 준비
prompt = st.chat_input("무슨 일이 있었나요?")
if prompt:
    message = client.beta.threads.messages.create(
        thread_id=thread_id,
        role="user",
        content=prompt
    )

    # 사용자가 입력한 메세지 UI에 표시
    with st.chat_message(message.role):
        st.write(message.content[0].text.value)

    # 대화를 진행하여 챗봇이 사용자 입력에 응답하도록 함
    run = client.beta.threads.runs.create(
        thread_id=thread_id,
        assistant_id=assistant_id,
    )

    # RUN의 상태가 완료될 때까지 주기적으로 상태 체크
    while run.status != "completed":
        print("status 확인 중", run.status)
        time.sleep(1)
        run = client.beta.threads.runs.retrieve(
            thread_id=thread_id,
            run_id=run.id
        )

    # 대화 진행이 완료되면 업데이트된 메세지를 다시 불러오기
    messages = client.beta.threads.messages.list(
        thread_id=thread_id
    )
    # 새로 추가된 메세지를 UI에 추가하기
    with st.chat_message(messages.data[0].role):
        st.write(messages.data[0].content[0].text.value)
