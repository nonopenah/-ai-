from flask import Flask, render_template_string
import subprocess

app = Flask(__name__)

# Streamlit을 서브프로세스로 실행
# 챗봇을 만든 python 파일의 이름을 'ongi_bot.py'의 위치에 넣어야 파일이 연결되어 로컬로 열림.
def run_streamlit():
    subprocess.Popen(['streamlit', 'run', 'ongi_bot.py'])

@app.route('/') # 이 경로로 접근하면 아래의 index 함수가 호출
def index(): #  HTML 문자열을 반환
    return render_template_string('''
        <h1>Flask에서 Streamlit 실행하기</h1>
        <iframe src="http://localhost:8501" width="100%" height="800"></iframe>
    ''') # iframe 태그는 위 링크에 있는 streamlit 애플리케이션을 내장

if __name__ == '__main__':
    run_streamlit() # streamlit 애플리케이션 실행
    app.run(port=5000) # flask 애플리케이션을 5000번 포트에서 실행
