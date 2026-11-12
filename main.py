
from quiz_game import QuizGame


def main():
    game = QuizGame()

    try:
        while True:
            game.show_menu()

            choice = input("메뉴를 선택하세요 (1-5): ").strip()

            if choice == "1":
                game.play()

            elif choice == "2":
                game.add_quiz()

            elif choice == "3":
                game.show_list()

            elif choice == "4":
                game.show_high_score()

            elif choice == "5":
                game.save_data()
                print("\n👋 게임을 종료합니다!")
                break

            else:
                print("\n⚠️ 1~5 중에서 선택해주세요.")

    except (KeyboardInterrupt, EOFError):
        print("\n⚠️ 입력이 중단되었습니다. 안전하게 종료합니다.")
        game.save_data()


if __name__ == "__main__":
    main()
