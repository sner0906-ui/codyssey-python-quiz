from quiz import QUIZ_DATA

class QuizGame:
    def __init__(self):
        self.score = 0          # 점수
        self.total = len(QUIZ_DATA)  # 전체 문제 수

    def run(self):
        print("\n🎯 퀴즈를 시작합니다!")
        print(f"총 {self.total}문제입니다.\n")

        for quiz in QUIZ_DATA:
            quiz.display()      # 문제 출력

            # 답 입력받기
            while True:
                try:
                    user_input = int(input("\n  정답 번호 입력 (1~4): "))
                    if 1 <= user_input <= 4:
                        break
                    print("  ⚠️ 1~4 사이 숫자를 입력해주세요!")
                except ValueError:
                    print("  ⚠️ 숫자만 입력해주세요!")

            # 정답 체크
            if quiz.check(user_input):
                print("  ✅ 정답입니다!")
                self.score += 1
            else:
                print(f"  ❌ 오답입니다! 정답은 {quiz.answer}번이에요.")

        self.show_result()      # 결과 출력

    def show_result(self):
        print("\n" + "="*30)
        print(f"🏆 최종 점수: {self.score} / {self.total}")
        print(f"📊 정답률: {self.score / self.total * 100:.1f}%")
        print("="*30)