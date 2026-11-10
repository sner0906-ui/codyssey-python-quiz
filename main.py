from quiz_game import QuizGame

def show_menu():
    print("\n=== 🐍 Python 퀴즈 게임 ===")
    print("1. 게임 시작")
    print("2. 점수 기록 보기")
    print("3. 종료")

def main():
    game = QuizGame()

    while True:
        show_menu()
        choice = input("메뉴를 선택하세요 (1~3): ").strip()

        if choice == "1":
            game.start()
        elif choice == "2":
            game.score_manager.show_scores()
        elif choice == "3":
            print("👋 게임을 종료합니다. 수고하셨습니다!")
            break
        else:
            print("⚠️ 1~3 중에서 선택해주세요!")

if __name__ == "__main__":
    main()