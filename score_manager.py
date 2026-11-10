import json
import os
from datetime import datetime

class ScoreManager:
    def __init__(self, filename="scores.json"):
        self.filename = filename
        self.scores = self._load_scores()

    def _load_scores(self):
        # 파일이 있으면 불러오고, 없으면 빈 리스트 반환
        if os.path.exists(self.filename):
            with open(self.filename, "r", encoding="utf-8") as f:
                return json.load(f)
        return []

    def save_score(self, score, total):
        # 점수 데이터 생성
        record = {
            "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "score": score,
            "total": total,
            "rate": round(score / total * 100, 1)
        }
        self.scores.append(record)

        # 파일에 저장
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(self.scores, f, ensure_ascii=False, indent=2)
        print("✅ 점수가 저장되었습니다!")

    def show_scores(self):
        # 저장된 점수가 없을 때
        if not self.scores:
            print("📭 저장된 점수가 없습니다.")
            return

        print("\n📊 점수 기록")
        print("-" * 40)
        for i, record in enumerate(self.scores, 1):
            print(f"{i}. {record['date']} | "
                  f"{record['score']}/{record['total']}점 | "
                  f"정답률: {record['rate']}%")
        print("-" * 40)