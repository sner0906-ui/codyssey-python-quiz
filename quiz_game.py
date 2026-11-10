from quiz import Quiz

class QuizGame:
    def __init__(self):
        self.quizzes = []       # 퀴즈 목록
        self.best_score = 0     # 최고 점수

    def show_menu(self):
        # 메뉴 출력 함수
        print("\n========================================")
        print("        🎯 나만의 퀴즈 게임 🎯")
        print("========================================")
        print("  1. 퀴즈 풀기")
        print("  2. 퀴즈 추가")
        print("  3. 퀴즈 목록")
        print("  4. 점수 확인")
        print("  5. 종료")
        print("========================================")

    def run(self):
        # 게임 실행 함수
        while True:
            self.show_menu()
            choice = input("  선택: ").strip()

            if choice == "1":
                print("퀴즈 풀기 - 준비 중")
            elif choice == "2":
                print("퀴즈 추가 - 준비 중")
            elif choice == "3":
                print("퀴즈 목록 - 준비 중")
            elif choice == "4":
                print("점수 확인 - 준비 중")
            elif choice == "5":
                print("게임을 종료합니다. 👋")
                break
            else:
                print("⚠️ 잘못된 입력입니다. 1-5 사이의 숫자를 입력하세요.")