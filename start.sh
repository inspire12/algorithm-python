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

# 디렉터리 생성 및 파일 작성
mkdir -p solve/$platform
cat << EOF > solve/$platform/$filename.py
'''
제목: $title
출처: $source
idea: $idea
난이도: $level
'''
import unittest
import sys

def solution(a):
    return a

if __name__ == '__main__':
    a = map(int, sys.stdin.readline().split())
    print(solution(a))

class TestSolution(unittest.TestCase):
    def test_example_1(self):
        input_string = None
        expected = None
        self.assertEqual(expected, solution(input_string))

EOF

echo "✅ 'solve/$platform/$filename.py' 생성 완료!"