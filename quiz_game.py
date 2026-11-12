from quiz import get_categories, get_quizzes_by_category


class QuizGame:
    def __init__(self):
        self.score = 0
        self.high_score = 0

    def select_category(self):
        """카테고리 선택"""
        categories = get_categories()

        print("\n카테고리를 선택하세요:")
        for i, category in enumerate(categories, 1):
            print(f"  {i}. {category}")
        print(f"  {len(categories) + 1}. 전체")

        while True:
            choice = input("선택: ").strip()
            if choice.isdigit():
                choice = int(choice)
                if 1 <= choice <= len(categories):
                    return categories[choice - 1]
                elif choice == len(categories) + 1:
                    return "전체"
            print("올바른 번호를 입력해주세요.")

    def play(self):
        """퀴즈 게임 실행"""
        category = self.select_category()
        quizzes = get_quizzes_by_category(category)

        print(f"\n[{category}] 카테고리 시작!\n")

        self.score = 0
        for i, quiz in enumerate(quizzes, 1):
            print(f"Q{i}. {quiz.question}")
            user_answer = input("정답: ").strip()

            if quiz.check_answer(user_answer):
                print("✅ 정답!\n")
                self.score += 1
            else:
                print(f"❌ 오답! 정답은 [{quiz.answer}]\n")

        print(f"최종 점수: {self.score} / {len(quizzes)}")

        if self.score > self.high_score:
            self.high_score = self.score
            print("🏆 새로운 최고 점수!\n")
        else:
            print(f"최고 점수는 {self.high_score}점\n")

    def show_high_score(self):
        """최고 점수 출력"""
        if self.high_score == 0:
            print("\n저장된 기록이 없습니다.\n")
        else:
            print(f"\n🏆 최고 점수: {self.high_score}점\n")