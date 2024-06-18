import os
from openai import OpenAI
import streamlit as st
import time

API_KEY = 'API_KEY'  # API 키를 직접 코드에 입력

client = OpenAI(api_key=API_KEY)

# thread id를 하나로 관리하기 위함
if 'thread_id' not in st.session_state:
    thread = client.beta.threads.create()
    st.session_state.thread_id = thread.id  # 생성된 thread의 ID 저장
thread_id = st.session_state.thread_id

assistant_id = "asst_id" # assistant id를 직접 입력

# 메세지 모두 불러오기
thread_messages = client.beta.threads.messages.list(thread_id)

# 페이지 제목
st.header("온기")

# 메세지 역순으로 가져와서 UI에 뿌려주기
for msg in reversed(thread_messages.data):
    with st.chat_message(msg.role):
        st.write(msg.content[0].text.value)

# 입력창에 입력을 받아서 입력된 내용으로 메세지 생성
prompt = st.chat_input("물어보고 싶은 것을 입력하세요!")
if prompt:
    message = client.beta.threads.messages.create(
        thread_id=thread_id,
        role="user",
        content=prompt
    )

    # 입력한 메세지 UI에 표시
    with st.chat_message(message.role):
        st.write(message.content[0].text.value)

    # RUN을 돌리는 과정
    run = client.beta.threads.runs.create(
        thread_id=thread_id,
        assistant_id=assistant_id,
    )

    # RUN이 completed 되었나 1초마다 체크
    while run.status != "completed":
        print("status 확인 중", run.status)
        time.sleep(1)
        run = client.beta.threads.runs.retrieve(
            thread_id=thread_id,
            run_id=run.id
        )

    # while문을 빠져나왔다는 것은 완료됐다는 것이니 메세지 불러오기
    messages = client.beta.threads.messages.list(
        thread_id=thread_id
    )
    # 마지막 메세지 UI에 추가하기
    with st.chat_message(messages.data[0].role):
        st.write(messages.data[0].content[0].text.value)
