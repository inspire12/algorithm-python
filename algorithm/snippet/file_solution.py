from pathlib import Path

root = Path(__file__).parent          # 스크립트 기준 루트 경로
data = root / "users.csv"   # OS 상관없이 경로 합침
text = data.read_text(encoding="utf-8")  # 한 번에 읽기
print(text.splitlines()[:5])         # 처음 5줄 미리보기