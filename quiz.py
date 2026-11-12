class Quiz:
    def __init__(self, question, answer, category):
        self.question = question
        self.answer = answer
        self.category = category

    def check_answer(self, user_answer):
        return self.answer.strip().lower() == user_answer.strip().lower()


# 퀴즈 데이터
QUIZ_DATA = [
    Quiz("Python에서 리스트를 만드는 기호는?", "[]", "Python 기초"),
    Quiz("Python에서 주석을 달 때 사용하는 기호는?", "#", "Python 기초"),
    Quiz("Python에서 출력 함수는?", "print", "Python 기초"),
    Quiz("스택(Stack)의 특징은? (LIFO/FIFO)", "LIFO", "자료구조"),
    Quiz("큐(Queue)의 특징은? (LIFO/FIFO)", "FIFO", "자료구조"),
    Quiz("탐색 시간이 O(1)인 자료구조는?", "해시테이블", "자료구조"),
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
    return [quiz for quiz in QUIZ_DATA if quiz.category == category]