
import json
import random
from pathlib import Path
from quiz import Quiz, QUIZ_DATA


class QuizGame:
    def __init__(self):
        self.state_file = Path(__file__).resolve().parent / "state.json"
        self.quizzes = list(QUIZ_DATA)
        self.high_score = 0
        self.score = 0
        self.load_data()

    def load_data(self):
        """저장된 퀴즈와 최고 점수 불러오기"""
        try:
            with open(self.state_file, "r", encoding="utf-8") as file:
                data = json.load(file)

            if not isinstance(data, dict):
                raise ValueError("데이터 형식 오류")

            score = data.get("best_score", 0)
            if type(score) is not int or score < 0:
                raise ValueError("최고 점수 형식 오류")

            saved_quizzes = data.get("quizzes")

            if saved_quizzes is not None:
                if not isinstance(saved_quizzes, list):
                    raise ValueError("퀴즈 목록 형식 오류")

                loaded = []

                for item in saved_quizzes:
                    question = item["question"]
                    choices = item["choices"]
                    answer = item["answer"]
                    category = item.get("category", "Python 기초")

                    if (
                        not isinstance(question, str)
                        or not question.strip()
                        or not isinstance(choices, list)
                        or len(choices) != 4
                        or any(
                            not isinstance(c, str) or not c.strip()
                            for c in choices
                        )
                        or type(answer) is not int
                        or not 1 <= answer <= 4
                        or not isinstance(category, str)
                        or not category.strip()
                    ):
                        raise ValueError("퀴즈 데이터 오류")

                    loaded.append(
                        Quiz(question, choices, answer, category)
                    )

                self.quizzes = loaded

            self.high_score = score

        except FileNotFoundError:
            print("📂 기본 퀴즈 데이터로 시작합니다.")

        except (OSError, ValueError, TypeError, KeyError):
            print("⚠️ 저장 파일에 문제가 있어 기본 데이터로 시작합니다.")

    def save_data(self):
        """퀴즈와 최고 점수를 JSON 파일로 저장"""
        data = {
            "quizzes": [
                {
                    "question": quiz.question,
                    "choices": quiz.choices,
                    "answer": quiz.answer,
                    "category": quiz.category
                }
                for quiz in self.quizzes
            ],
            "best_score": self.high_score
        }

        temp_file = self.state_file.with_suffix(".tmp")

        try:
            with open(temp_file, "w", encoding="utf-8") as file:
                json.dump(
                    data,
                    file,
                    ensure_ascii=False,
                    indent=4
                )

            temp_file.replace(self.state_file)
            return True

        except OSError:
            print("⚠️ 데이터를 저장하지 못했습니다.")
            return False

    def show_menu(self):
        print("\n" + "=" * 35)
        print("       🏆 Python 퀴즈 게임")
        print("=" * 35)
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 목록")
        print("4. 최고 점수 확인")
        print("5. 종료")
        print("=" * 35)

    def read_number(self, message, minimum, maximum):
        """숫자를 안전하게 입력받기"""
        while True:
            value = input(message).strip()

            try:
                number = int(value)

            except ValueError:
                print("⚠️ 숫자를 입력해주세요.")
                continue

            if minimum <= number <= maximum:
                return number

            print(
                f"⚠️ {minimum}~{maximum} 사이의 숫자를 입력하세요."
            )

    def select_category(self):
        """카테고리 선택"""
        categories = sorted(
            set(quiz.category for quiz in self.quizzes)
        )

        print("\n카테고리를 선택하세요:")

        for i, category in enumerate(categories, 1):
            print(f"{i}. {category}")

        print(f"{len(categories) + 1}. 전체")

        number = self.read_number(
            "선택: ", 1, len(categories) + 1
        )

        if number == len(categories) + 1:
            return "전체"

        return categories[number - 1]

    def play(self):
        """객관식 퀴즈를 랜덤 순서로 출제"""
        if not self.quizzes:
            print("⚠️ 등록된 퀴즈가 없습니다.")
            return

        category = self.select_category()

        if category == "전체":
            quizzes = list(self.quizzes)

        else:
            quizzes = [
                quiz for quiz in self.quizzes
                if quiz.category == category
            ]

        # 보너스 과제: 문제 출제 순서를 무작위로 섞기
        random.shuffle(quizzes)

        self.score = 0

        print(f"\n🎮 퀴즈 시작! 총 {len(quizzes)}문제")
        print("🎲 보너스 기능: 랜덤 출제가 적용되었습니다!")

        for i, quiz in enumerate(quizzes, 1):
            print(f"\n[문제 {i}]")
            quiz.display()

            answer = self.read_number(
                "정답 번호 (1-4): ", 1, 4
            )

            if quiz.check_answer(answer):
                print("✅ 정답입니다!")
                self.score += 1

            else:
                correct = quiz.choices[quiz.answer - 1]
                print(
                    f"❌ 오답! 정답은 "
                    f"{quiz.answer}번 ({correct})"
                )

        print(f"\n🏆 최종 점수: {self.score} / {len(quizzes)}")

        if self.score > self.high_score:
            self.high_score = self.score

            if self.save_data():
                print("🎉 새로운 최고 점수가 저장되었습니다!")

        else:
            print(f"최고 점수는 {self.high_score}점")

    def add_quiz(self):
        """새로운 객관식 퀴즈 추가"""
        print("\n📌 새로운 퀴즈 추가")

        while True:
            question = input("문제: ").strip()

            if question:
                break

            print("⚠️ 문제를 입력하세요.")

        choices = []

        for i in range(1, 5):
            while True:
                choice = input(f"선택지 {i}: ").strip()

                if choice:
                    choices.append(choice)
                    break

                print("⚠️ 선택지를 입력하세요.")

        answer = self.read_number(
            "정답 번호 (1-4): ", 1, 4
        )

        category = input(
            "카테고리 (Enter: Python 기초): "
        ).strip() or "Python 기초"

        self.quizzes.append(
            Quiz(question, choices, answer, category)
        )

        if self.save_data():
            print("✅ 퀴즈가 추가되고 저장되었습니다!")

        else:
            print("⚠️ 퀴즈가 메모리에만 추가되었습니다.")

    def show_list(self):
        """전체 퀴즈 목록 출력"""
        if not self.quizzes:
            print("\n📭 등록된 퀴즈가 없습니다.")
            return

        print(f"\n📋 퀴즈 목록 (총 {len(self.quizzes)}개)")

        for i, quiz in enumerate(self.quizzes, 1):
            print(
                f"{i}. [{quiz.category}] {quiz.question}"
            )

    def show_high_score(self):
        """최고 점수 확인"""
        if self.high_score == 0:
            print("\n📭 아직 최고 점수 기록이 없습니다.")

        else:
            print(f"\n🏆 최고 점수: {self.high_score}점")
