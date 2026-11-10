from quiz_game import QuizGame

def main():
    while True:
        print("\n" + "="*30)
        print("   🐍 Python 퀴즈 게임")
        print("="*30)
        print("  1. 퀴즈 시작")
        print("  2. 종료")
        print("="*30)

        choice = input("\n  메뉴를 선택하세요 (1~2): ")

        if choice == "1":
            game = QuizGame()
            game.run()
        elif choice == "2":
            print("\n  👋 게임을 종료합니다. 수고하셨어요!")
            break
        else:
            print("\n  ⚠️ 1 또는 2를 입력해주세요!")

if __name__ == "__main__":
    main()