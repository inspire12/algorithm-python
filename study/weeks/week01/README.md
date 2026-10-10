# 1주차: 배열·문자열·해시

## 이번 주의 목표

- 값의 존재 여부, 개수, 그룹을 보고 `set`과 `dict`를 구분한다.
- 이중 루프 `O(n²)`를 해시 탐색 `O(n)` 기대 시간으로 바꾼다.
- 원본 배열과 정렬된 배열을 구분하고 Python 슬라이스 경계를 다룬다.
- 다중 정렬 기준을 튜플 `key`로 표현한다.
- 동일한 패턴을 48시간·7일 후 검색 없이 재구현한다.

## 정석 카드

문제를 풀기 전에 완성 코드를 보지 말고, 풀이 후에 [1주차 정석 카드](standard-cards.md)의 빈칸을 채웁니다.

## 필수 3문제

| 구분 | 플랫폼 | 문제 | 제한 | 학습 포인트 |
|---|---|---|---:|---|
| 기본 정석 | 프로그래머스 | [완주하지 못한 선수](https://school.programmers.co.kr/learn/courses/30/lessons/42576) | 40분 | 빈도 차이, 동명이인, `Counter`와 일반 `dict` |
| 패턴 변형 | LeetCode | [217. Contains Duplicate](https://leetcode.com/problems/contains-duplicate/) | 30분 | 존재 여부에는 개수가 필요 없음, `set` |
| 기본 구현 | 프로그래머스 | [K번째수](https://school.programmers.co.kr/learn/courses/30/lessons/42748) | 40분 | 1-based 조건을 Python 슬라이스로 변환, 부분 정렬 |

### 필수 문제 완료 조건

- [ ] 코드 전에 [문제 분석지](../../templates/problem-analysis.md)를 작성했다.
- [ ] 첫 시도에서 완전탐색의 복잡도를 적었다.
- [ ] 정답 풀이와 자신의 풀이를 비교했다.
- [ ] 핵심 반례를 하나 이상 추가했다.

## 선택 2문제

| 구분 | 플랫폼 | 문제 | 제한 | 학습 포인트 |
|---|---|---|---:|---|
| 고난도 변형 | LeetCode | [49. Group Anagrams](https://leetcode.com/problems/group-anagrams/) | 50분 | 같은 그룹을 나타내는 해시 가능한 표준 형태 |
| 복합 문제 | 프로그래머스 | [베스트앨범](https://school.programmers.co.kr/learn/courses/30/lessons/42579) | 60분 | 그룹별 합계, 그룹 내 정렬, 다중 정렬 기준 |

`Group Anagrams`는 정렬된 문자열과 문자 빈도 튜플 두 방식의 복잡도를 비교합니다. `베스트앨범`은 40분 내에 구조가 잡히지 않으면 보류하고, 어떤 정보를 그룹별로 저장해야 하는지만 기록합니다.

## 주간 모의고사

- 시간: 90분
- 규칙: 검색·AI·정석 카드 열람 금지
- 시작 5분 안에 세 문제의 풀이 순서를 정합니다.

| 순번 | 플랫폼 | 문제 | 확인할 판단 |
|---:|---|---|---|
| 1 | 프로그래머스 | [폰켓몬](https://school.programmers.co.kr/learn/courses/30/lessons/1845) | 선택 개수와 서로 다른 값의 개수 중 어느 것이 상한인가? |
| 2 | LeetCode | [242. Valid Anagram](https://leetcode.com/problems/valid-anagram/) | 두 문자열의 빈도를 어떻게 비교할 것인가? |
| 3 | 프로그래머스 | [같은 숫자는 싫어](https://school.programmers.co.kr/learn/courses/30/lessons/12906) | 전체 중복 제거와 연속 중복 제거를 구분했는가? |

모의고사 후 [모의고사 회고지](../../templates/mock-exam.md)를 작성합니다. 빨리 끝났다면 남은 시간에 각 풀이의 시간·공간 복잡도와 추가 반례를 적습니다.

## 재풀이 일정

| 문제 | 첫 시도 | 48시간 재구현 | 7일 재구현 | 완료 |
|---|---|---|---|---|
| 완주하지 못한 선수 | | | | [ ] |
| Contains Duplicate | | | | [ ] |
| K번째수 | | | | [ ] |
| Group Anagrams | | | | [ ] |
| 베스트앨범 | | | | [ ] |

## 주간 성공 기준

- [ ] 존재 여부는 `set`, 개수·그룹은 `dict`를 먼저 후보로 올린다.
- [ ] `sorted(items, key=lambda x: (...))`의 오름차순·내림차순 조합을 설명할 수 있다.
- [ ] 동명이인, 빈 문자열, 단일 원소, 모두 같음을 테스트했다.
- [ ] 필수 3문제의 48시간·7일 재구현을 완료했다.
