from flask import Flask, request, jsonify, render_template_string
import pandas as pd

app = Flask(__name__)

# 로컬 경로 설정 (절대 경로를 사용하세요)
training_data_path = '/Users/dain/Downloads/data/trainingdata.csv'
wellness_data_path = '/Users/dain/Downloads/data/wellness_dataset_original.csv'
shelter_data_path = '/Users/dain/Downloads/data/shelter.csv'

# 인코딩 형식을 시도해볼 리스트
encodings = ['utf-8-sig', 'utf-8', 'cp949', 'euc-kr']

def try_read_csv(path, encodings):
    for encoding in encodings:
        try:
            data = pd.read_csv(path, encoding=encoding)
            print(f"Successfully loaded with encoding: {encoding}")
            print(data.head())  # 첫 몇 줄 출력하여 확인
            return data
        except Exception as e:
            print(f"Error loading with encoding {encoding}: {e}")
    return None

# 데이터 로드
training_data = try_read_csv(training_data_path, encodings)
wellness_data = try_read_csv(wellness_data_path, encodings)
shelter_data = try_read_csv(shelter_data_path, encodings)

# 챗봇 클래스 정의
class ForestWarmthChatbot:
    def __init__(self, training_data, wellness_data, shelter_data):
        self.training_data = training_data
        self.wellness_data = wellness_data
        self.shelter_data = shelter_data
    
    def provide_empathy(self, user_input):
        # 간단한 공감 메시지 생성
        response = "그렇게 느낄 수 있어요. 조금 더 이야기해줄래요?"
        return response

    def provide_shelter_info(self, location=None):
        if location:
            filtered_shelters = self.shelter_data[self.shelter_data['시도'] == location]
            if not filtered_shelters.empty:
                return filtered_shelters.to_dict('records')
            else:
                return "해당 지역에 대한 쉼터 정보를 찾을 수 없습니다."
        else:
            return "위치를 알려주시면 가까운 쉼터 정보를 제공해드릴 수 있습니다."
    
    def check_emergency(self, user_input):
        # 간단한 위급 상황 체크 (예시: 특정 키워드가 포함된 경우)
        emergency_keywords = ['도움', '위험', '신고']
        for keyword in emergency_keywords:
            if keyword in user_input:
                return True
        return False

    def handle_emergency(self):
        return "위급 상황으로 판단됩니다. 즉시 112에 연락하시거나, 가까운 사람에게 도움을 요청하세요."

    def chat(self, user_input):
        if self.check_emergency(user_input):
            return self.handle_emergency()
        
        if "쉼터" in user_input:
            return self.provide_shelter_info()

        return self.provide_empathy(user_input)

# 챗봇 인스턴스 생성
if training_data is not None and wellness_data is not None and shelter_data is not None:
    forest_warmth_bot = ForestWarmthChatbot(training_data, wellness_data, shelter_data)
else:
    print("데이터를 불러오지 못했습니다. 경로를 확인해주세요.")

@app.route('/')
def index():
    return render_template_string('''
        <!DOCTYPE html>
        <html>
        <head>
            <title>Forest Warmth Chatbot</title>
        </head>
        <body>
            <h1>Forest Warmth Chatbot</h1>
            <form method="POST" action="/chat">
                <label for="message">Enter your message:</label>
                <input type="text" id="message" name="message" required>
                <button type="submit">Send</button>
            </form>
            {% if response %}
                <h2>Response:</h2>
                <p>{{ response }}</p>
            {% endif %}
        </body>
        </html>
    ''')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form.get('message')
    response = forest_warmth_bot.chat(user_input)
    return render_template_string('''
        <!DOCTYPE html>
        <html>
        <head>
            <title>Forest Warmth Chatbot</title>
        </head>
        <body>
            <h1>Forest Warmth Chatbot</h1>
            <form method="POST" action="/chat">
                <label for="message">Enter your message:</label>
                <input type="text" id="message" name="message" required>
                <button type="submit">Send</button>
            </form>
            <h2>Response:</h2>
            <p>{{ response }}</p>
        </body>
        </html>
    ''', response=response)

if __name__ == '__main__':
    app.run(debug=True)
