class Quiz:
    def __init__(self, question, choices, answer, category):
        self.question = question
        self.choices = choices
        self.answer = answer
        self.category = category

    def display(self):
        print(f"\n{self.question}")

        for i, choice in enumerate(self.choices, 1):
            print(f"  {i}. {choice}")

    def check_answer(self, user_answer):
        try:
            return int(user_answer) == self.answer
        except (ValueError, TypeError):
            return False


# 기본 퀴즈 데이터 6개
QUIZ_DATA = [
    Quiz(
        "Python에서 리스트를 만드는 기호는?",
        ["()", "[]", "{}", "<>"],
        2,
        "Python 기초"
    ),
    Quiz(
        "Python에서 주석을 달 때 사용하는 기호는?",
        ["//", "#", "/*", "--"],
        2,
        "Python 기초"
    ),
    Quiz(
        "Python에서 출력 함수는?",
        ["input()", "open()", "print()", "len()"],
        3,
        "Python 기초"
    ),
    Quiz(
        "스택(Stack)의 특징은?",
        ["FIFO", "LIFO", "정렬", "랜덤"],
        2,
        "자료구조"
    ),
    Quiz(
        "큐(Queue)의 특징은?",
        ["LIFO", "랜덤", "FIFO", "역순 정렬"],
        3,
        "자료구조"
    ),
    Quiz(
        "평균적으로 키 조회가 O(1)인 자료구조는?",
        ["연결 리스트", "이진 탐색 트리", "배열 순차 탐색", "해시 테이블"],
        4,
        "자료구조"
    )
]


def get_categories():
    """카테고리 목록 반환"""
    categories = list(set(quiz.category for quiz in QUIZ_DATA))
    categories.sort()
    return categories


def get_quizzes_by_category(category):
    """카테고리별 퀴즈 반환"""
    if category == "전체":
        return QUIZ_DATA

    return [
        quiz for quiz in QUIZ_DATA
        if quiz.category == category
    ]