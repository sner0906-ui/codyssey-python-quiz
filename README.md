# 🎯 나만의 Python 퀴즈 게임

Python 기초 개념을 복습할 수 있는 퀴즈 게임입니다.  
문제를 풀고, 직접 퀴즈를 추가하고, 점수를 기록할 수 있습니다.

---

## 📌 프로젝트 개요

| 항목 | 내용 |
|------|------|
| 프로젝트명 | 나만의 Python 퀴즈 게임 |
| 개발 언어 | Python 3.10+ |
| 개발 목적 | Python 기초 학습 및 Git 포트폴리오 제작 |
| 개발 기간 | 2025년 |

---

## 🛠️ 기술 스택

- **언어**: Python 3.10+
- **버전 관리**: Git / GitHub
- **개발 환경**: Visual Studio Code

---

## 📁 파일 구조

```
codyssey-python-quiz/
├── main.py          # 프로그램 시작점
├── quiz.py          # Quiz 클래스 (문제 1개 표현)
├── quiz_game.py     # QuizGame 클래스 (게임 전체 관리)
├── state.json       # 퀴즈 데이터 및 점수 저장
├── README.md        # 프로젝트 설명서
└── .gitignore       # Git 제외 파일 목록
```

---

## ⚙️ 실행 방법

### 1. 저장소 클론

```bash
git clone https://github.com/본인계정명/codyssey-python-quiz.git
```

### 2. 폴더 이동

```bash
cd codyssey-python-quiz
```

### 3. 프로그램 실행

```bash
python main.py
```

---

## 🎮 주요 기능

| 기능 | 설명 |
|------|------|
| 퀴즈 풀기 | 저장된 퀴즈를 순서대로 풀고 결과를 확인합니다 |
| 퀴즈 추가 | 새로운 문제와 선택지를 직접 입력해 추가합니다 |
| 퀴즈 목록 | 저장된 퀴즈 전체 목록을 확인합니다 |
| 점수 확인 | 최고 점수와 최근 점수를 확인합니다 |
| 데이터 저장 | 퀴즈와 점수를 state.json 파일에 저장합니다 |

---

## 🌿 브랜치 전략

| 브랜치 | 역할 |
|--------|------|
| `main` | 최종 배포용 브랜치 |
| `feature/quiz-play` | 퀴즈 풀기 및 점수 계산 기능 개발 |

---

## 📝 커밋 내역 요약

| 순서 | 커밋 메시지 | 설명 |
|------|-------------|------|
| 1 | Docs: README 작성 | 프로젝트 설명서 초안 작성 |
| 2 | Feat: 기본 클래스 및 메뉴 뼈대 생성 | main.py, quiz.py, quiz_game.py 생성 |
| 3 | Feat: 기본 퀴즈 데이터 5개 추가 | Python 기초 퀴즈 5문제 등록 |
| 4 | Feat: 퀴즈 풀기 기능 구현 | feature/quiz-play 브랜치에서 개발 |
| 5 | Feat: 점수 계산 기능 구현 | feature/quiz-play 브랜치에서 개발 |
| 6 | Merge: feature/quiz-play → main | 퀴즈 풀기 기능 main에 병합 |
| 7 | Feat: 퀴즈 추가 기능 구현 | 사용자 직접 퀴즈 추가 |
| 8 | Feat: state.json 저장 및 불러오기 구현 | 데이터 영구 저장 |
| 9 | Feat: 퀴즈 목록 보기 기능 구현 | 전체 퀴즈 목록 출력 |
| 10 | Fix: 전체 테스트 및 오류 수정 | 버그 수정 및 예외 처리 |
| 11 | Docs: README 최종 업데이트 | 완성된 내용으로 README 업데이트 |

---

## 👤 개발자 정보

- **GitHub**: [본인 GitHub 주소 입력]