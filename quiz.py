class Quiz:
    def __init__(self, question, choices, answer):
        self.question = question    # 문제
        self.choices = choices      # 선택지 4개 (리스트)
        self.answer = answer        # 정답 번호 (1~4)

    def display(self):
        print(f"\n{self.question}")
        for i, choice in enumerate(self.choices, 1):
            print(f"  {i}. {choice}")

    def check(self, user_answer):
        return self.answer == user_answer


# 퀴즈 문제 목록
QUIZ_DATA = [
    Quiz(
        "Q1. 파이썬에서 주석을 작성할 때 사용하는 기호는?",
        ["//", "/*", "#", "--"],
        3
    ),
    Quiz(
        "Q2. 파이썬 리스트에서 마지막 요소를 가져오는 인덱스는?",
        ["0", "-1", "last", "end"],
        2
    ),
    Quiz(
        "Q3. 파이썬에서 함수를 정의할 때 사용하는 키워드는?",
        ["function", "def", "fun", "define"],
        2
    ),
    Quiz(
        "Q4. 다음 중 파이썬의 자료형이 아닌 것은?",
        ["int", "str", "char", "bool"],
        3
    ),
    Quiz(
        "Q5. 반복문에서 현재 순환을 건너뛸 때 사용하는 키워드는?",
        ["break", "pass", "continue", "skip"],
        3
    ),
]