from quiz_game import QuizGame

def main():
    game = QuizGame()

    while True:
        print("=" * 30)
        print("    🏆 Python 퀴즈 게임")
        print("=" * 30)
        print("  1. 퀴즈 시작")
        print("  2. 최고 점수 보기")
        print("  3. 종료")
        print("=" * 30)

        choice = input("메뉴를 선택하세요 (1-3): ").strip()

        if choice == "1":
            game.play()
        elif choice == "2":
            game.show_high_score()
        elif choice == "3":
            print("\n👋 게임을 종료합니다. 수고하셨습니다!\n")
            break
        else:
            print("\n⚠️ 1, 2, 3 중에서 선택해주세요!\n")

if __name__ == "__main__":
    main()