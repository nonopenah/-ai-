# /mnt/data/chatbot.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn.metrics import accuracy_score
import random

# CSV 파일 읽기
emotion_data = pd.read_csv(r'C:\Users\82104\osp\project_chatbot\emotion_Training.csv')
shelter_data = pd.read_csv(r'C:\Users\82104\osp\project_chatbot\shelter_info.csv')


# 감정 인식 모델 구축
X = emotion_data['talk']
y = emotion_data['profile']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = make_pipeline(TfidfVectorizer(), MultinomialNB())
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print(f"Model accuracy: {accuracy_score(y_test, y_pred):.2f}")

# 쉼터 정보 컬럼 이름 확인 후 수정
print(shelter_data.columns)

# 챗봇 함수 정의
def get_shelter_info():
    shelter = shelter_data.sample(n=1).iloc[0]
    return f"이용 가능한 쉼터 정보:\n시설명: {shelter['시설명']}\n주소: {shelter['시설주소']}\n전화번호: {shelter['대표전화']}"

def provide_comfort():
    comforts = [
        "힘든 상황이네요. 당신의 이야기를 들어줘서 고마워요.",
        "당신은 혼자가 아니에요. 필요한 도움을 받으실 수 있습니다.",
        "잠시 쉬어가도 괜찮아요. 우리는 당신을 위해 여기 있어요."
    ]
    return random.choice(comforts)

def chatbot():
    print("안녕하세요! 저는 당신을 돕기 위한 챗봇입니다. 무엇을 도와드릴까요?")
    while True:
        user_input = input("당신의 고민을 말씀해 주세요: ")
        if user_input.lower() in ['그만', '종료', '끝']:
            print("챗봇을 종료합니다. 힘내세요!")
            break
        emotion = model.predict([user_input])[0]
        print(f"감지된 감정: {emotion}")
        print(provide_comfort())
        print(get_shelter_info())

# 챗봇 실행
if __name__ == "__main__":
    chatbot()
