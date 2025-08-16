#!/bin/bash

default_platform="baekjoon"
default_level="easy"

echo "🧑‍💻 알고리즘 문제 파일 생성기 🧑‍💻"

# 사용자 입력받기
read -p "파일 이름을 입력하세요 (예: problem): " filename
read -p "문제 플랫폼을 입력하세요 (예: baekjoon, programmers) [${default_platform}]: " platform
platform=${platform:-$default_platform}
read -p "제목: " title
read -p "번호 or 출처: " source_input
read -p "풀이 아이디어: " idea
read -p "난이도(easy/medium/hard/expert) [${default_level}]: " level
level=${level:-$default_level}

# 출처 자동 처리
if [ ${#source_input} -le 10 ]; then
  case "$platform" in
    baekjoon)
      source="https://www.acmicpc.net/problem/$source_input"
      ;;
    programmers)
      source="https://school.programmers.co.kr/learn/courses/30/lessons/$source_input"
      ;;
    leetcode)
      source="https://leetcode.com/problems/$source_input"
      ;;
    *)
      source="$source_input"
      ;;
  esac
else
  source="$source_input"
fi



# 디렉터리 생성 및 기본 파일 작성
mkdir -p tried/$platform
cat << EOF > tried/$platform/$filename.py
'''
제목: $title
출처: $source
idea: $idea
난이도: $level
'''
import sys

def solution(a):
    return a

if __name__ == '__main__':
    a = map(int, sys.stdin.readline().split())
    print(solution(a))


EOF

# 플랫폼별 테스트 코드 생성
if [ "$platform" = "baekjoon" ]; then
cat << EOF >> tried/$platform/${filename}.py
import io
import unittest
import sys

class TestSolution(unittest.TestCase):
    def test_example_1(self):
        test_input = ""
        expected_output = ""
        sys.stdin = io.StringIO(test_input)
        sys.stdout = io.StringIO()
        main()
        self.assertEqual(sys.stdout.getvalue(), expected_output)
EOF
else
cat << EOF >> tried/$platform/${filename}.py
import unittest

class TestSolution(unittest.TestCase):
    def test_example_1(self):
        input_data = None
        expected = None
        self.assertEqual(solution(input_data), expected)
EOF
fi

echo "✅ 'tried/$platform/$filename.py'와 테스트 파일 생성 완료!"