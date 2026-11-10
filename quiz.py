class Quiz:
    def __init__(self, question, choices, answer):
        self.question = question    # 문제
        self.choices = choices      # 선택지 4개 (리스트)
        self.answer = answer        # 정답 번호 (1~4)

    def display(self):
        # 문제와 선택지를 출력하는 함수
        print(f"\n{self.question}")
        for i, choice in enumerate(self.choices, 1):
            print(f"  {i}. {choice}")

    def check(self, user_answer):
        # 정답 확인 함수
        return self.answer == user_answer