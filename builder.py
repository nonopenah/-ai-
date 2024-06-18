import openai

# OpenAI API 키 설정
openai.api_key = 'API_KEY'  # 여기에 실제 OpenAI API 키를 입력하세요

def generate_response(user_input):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant named 온기."},
            {"role": "user", "content": user_input}
        ]
    )
    return response.choices[0].message['content'].strip()

def main():
    print("안녕하세요, 저는 온기입니다. 무엇을 도와드릴까요?")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() in ["exit", "quit", "종료"]:
            print("온기: 대화를 종료합니다. 좋은 하루 보내세요!")
            break
        
        # 사용자 입력에 따른 프롬프트 설정
        if "상담" in user_input:
            prompt = f"심리 상담 대상과 대화합니다. {user_input}에 어떻게 응답해야 할까요?"
        elif "자살" in user_input:
            prompt = f"자살 예방 대상과 대화합니다. {user_input}에 어떻게 응답해야 할까요?"
        elif "쉼터" in user_input:
            prompt = f"기관 소개 대상과 대화합니다. {user_input}에 어떻게 응답해야 할까요?"
        else:
            prompt = f"{user_input}에 어떻게 응답해야 할까요?"

        response = generate_response(prompt)
        print(f"온기: {response}")

if __name__ == "__main__":
    main()
