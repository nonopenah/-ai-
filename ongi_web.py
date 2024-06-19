from flask import Flask, render_template_string
import subprocess

app = Flask(__name__)

# Streamlit을 서브프로세스로 실행
# 챗봇을 만들어든 python 파일의 이름을 "챗봇.py"에 넣어야 파일이 연걸되어 로컬로 열림.
def run_streamlit():
    subprocess.Popen(['streamlit', 'run', '챗봇.py'])

@app.route('/')
def index():
    return render_template_string('''
        <h1>Flask에서 Streamlit 실행하기</h1>
        <iframe src="http://localhost:8501" width="100%" height="800"></iframe>
    ''')

if __name__ == '__main__':
    run_streamlit()
    app.run(port=5000)
