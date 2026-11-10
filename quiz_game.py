from quiz import Quiz
from score_manager import ScoreManager

class QuizGame:
    def __init__(self):
        self.score_manager = ScoreManager()
        self.quizzes = [
            Quiz("파이썬에서 주석을 작성할 때 사용하는 기호는?",
                 ["1) //", "2) #", "3) --", "4) **"], "2"),
            Quiz("리스트에서 마지막 요소를 제거하는 메서드는?",
                 ["1) remove()", "2) delete()", "3) pop()", "4) clear()"], "3"),
            Quiz("파이썬에서 정수형 타입을 나타내는 키워드는?",
                 ["1) integer", "2) int", "3) num", "4) digit"], "2"),
            Quiz("다음 중 반복문이 아닌 것은?",
                 ["1) for", "2) while", "3) loop", "4) 모두 반복문"], "3"),
            Quiz("파이썬에서 아무것도 없음을 나타내는 값은?",
                 ["1) null", "2) undefined", "3) None", "4) empty"], "3"),
        ]

    def start(self):
        print("\n🎮 퀴즈 게임을 시작합니다!\n")
        score = 0

        for i, quiz in enumerate(self.quizzes, 1):
            print(f"Q{i}. {quiz.question}")
            for choice in quiz.choices:
                print(f"  {choice}")

            answer = input("정답 입력 (1~4): ").strip()

            if quiz.check_answer(answer):
                print("✅ 정답입니다!\n")
                score += 1
            else:
                print(f"❌ 오답입니다! 정답은 {quiz.answer}번이에요.\n")

        total = len(self.quizzes)
        rate = round(score / total * 100, 1)

        print(f"🏆 최종 점수: {score}/{total} | 정답률: {rate}%")

        # 점수 저장
        self.score_manager.save_score(score, total)