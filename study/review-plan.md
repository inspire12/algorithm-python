# 푼 문제 복습 계획

> 참고용 계획 뷰입니다. 실제 이해도와 다음 행동의 유일한 기준은 `study/problem-registry.json`입니다.

- 기준일: 2026-08-27
- 복습 대상: 완료가 확인됐거나 정답 확인 후 재구현 중인 10문제
- 완료 미확인 학습 이력: 9문제
- 목표: 정답 기억이 아니라 문제 계약, 최적화 근거, 불변식, 무참조 구현을 다시 확인한다.

## 상태 기준

| 상태 | 판정 | 복습 방법 |
|---|---|---|
| `A` | 무참조로 설명·구현 가능 | 7일 후 한 번 재확인 |
| `B` | 아이디어는 설명하지만 구현이 불안정 | 48시간 후 재구현 |
| `C` | 정답 코드를 본 뒤 아직 재구현하지 않음 | 이번 회차에 최우선 재구현 |

현재 `C` 상태로 시작한 문제는 다음 세 문제다.

- `Container With Most Water`
- `Remove Duplicates from Sorted Array`
- `Trapping Rain Water`

과거 오답노트에만 등장하고 완료 표시가 없는 문제는 푼 문제로 간주하지 않는다. 별도의 `U` 상태로 두고 사용자가 실제 풀이 완료를 확인하거나 다시 풀기 전까지 정규 복습 일정에서 제외한다.

| 상태 | 판정 | 처리 |
|---|---|---|
| `U` | 학습·오답 이력은 있으나 풀이 완료를 확인할 수 없음 | 복습이 아니라 신규/재풀이 대상으로 관리 |

## 세션 시작 복습 게이트

새 알고리즘 학습 세션에서는 다음 순서를 따른다.

```text
1. 오늘 날짜 이전까지의 미완료 복습을 찾는다.
2. C 상태 → 기한이 지난 B 상태 → 오늘 예정 B 상태 순으로 우선순위를 정한다.
3. 가장 먼저 할 문제와 예상 분량을 제시한다.
4. "오늘 복습부터 진행할까요?"라고 묻는다.
5. 사용자가 복습을 선택하면 이 문서의 일정과 다음 질문을 우선한다.
6. 사용자가 진도를 선택하면 current-progress.md의 현재 문제를 이어간다.
```

사용자가 요청에서 이미 복습 또는 새 진도를 명시했다면 선택을 다시 묻지 않는다.

## 문제별 이해도와 오답노트

오답 번호를 누르면 해당 상세 기록과 반례로 이동한다. `—`는 아직 그 문제 전용 오답 기록이 없다는 뜻이지, 이해도 `A`를 뜻하지 않는다.

| 문제 | 유형 | 오답노트 | 이해도 | 1차 진단 | 다음 복습 |
|---|---|---|---|---|---|
| [Two Sum](https://leetcode.com/problems/two-sum/) | 해시·정렬+투 포인터 | [1](notes/live-coding-mistakes.md#mistake-1) · [2](notes/live-coding-mistakes.md#mistake-2) · [3](notes/live-coding-mistakes.md#mistake-3) · [4](notes/live-coding-mistakes.md#mistake-4) | `C` 해시 정답 확인·재구현 대기 | 2026-08-27 | 2026-08-29 |
| [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) | 스택 | [5](notes/live-coding-mistakes.md#mistake-5) · [6](notes/live-coding-mistakes.md#mistake-6) · [7](notes/live-coding-mistakes.md#mistake-7) · [8](notes/live-coding-mistakes.md#mistake-8) | `U` 완료 미확인 | 일정 제외 | 다시 풀 때 결정 |
| [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | 슬라이딩 윈도우 | [9](notes/live-coding-mistakes.md#mistake-9) · [10](notes/live-coding-mistakes.md#mistake-10) · [11](notes/live-coding-mistakes.md#mistake-11) · [12](notes/live-coding-mistakes.md#mistake-12) | `U` 완료 미확인 | 일정 제외 | 다시 풀 때 결정 |
| [Container With Most Water](https://leetcode.com/problems/container-with-most-water/) | 양끝 투 포인터 | [4](notes/live-coding-mistakes.md#mistake-4) · [16](notes/live-coding-mistakes.md#mistake-16) · [21](notes/live-coding-mistakes.md#mistake-21) | `B` 힌트 후 구현·통과 | 2026-08-27 | 2026-08-29 |
| [Maximum Average Subarray I](https://leetcode.com/problems/maximum-average-subarray-i/) | 고정 윈도우 | [13](notes/live-coding-mistakes.md#mistake-13) | `U` 완료 미확인 | 일정 제외 | 다시 풀 때 결정 |
| [Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/) | 가변 윈도우 | [14](notes/live-coding-mistakes.md#mistake-14) · [15](notes/live-coding-mistakes.md#mistake-15) · [16](notes/live-coding-mistakes.md#mistake-16) | `U` 완료 미확인 | 일정 제외 | 다시 풀 때 결정 |
| [Fruit Into Baskets](https://leetcode.com/problems/fruit-into-baskets/) | 가변 윈도우 | [17](notes/live-coding-mistakes.md#mistake-17) · [18](notes/live-coding-mistakes.md#mistake-18) · [19](notes/live-coding-mistakes.md#mistake-19) | `U` 완료 미확인 | 일정 제외 | 다시 풀 때 결정 |
| [Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/) | 읽기·쓰기 포인터 | [1](notes/live-coding-mistakes.md#mistake-1) · [17](notes/live-coding-mistakes.md#mistake-17) | `C` 무참조 재구현 대기 | 2026-08-28 | 2026-08-30 |
| [Permutation in String](https://leetcode.com/problems/permutation-in-string/) | 고정 윈도우 | [3](notes/live-coding-mistakes.md#mistake-3) · [10](notes/live-coding-mistakes.md#mistake-10) · [13](notes/live-coding-mistakes.md#mistake-13) · [18](notes/live-coding-mistakes.md#mistake-18) | `U` 완료 미확인 | 일정 제외 | 다시 풀 때 결정 |
| [Max Consecutive Ones III](https://leetcode.com/problems/max-consecutive-ones-iii/) | 가변 윈도우 | [18](notes/live-coding-mistakes.md#mistake-18) · [20](notes/live-coding-mistakes.md#mistake-20) · [21](notes/live-coding-mistakes.md#mistake-21) · [22](notes/live-coding-mistakes.md#mistake-22) | `U` 완료 미확인 | 일정 제외 | 다시 풀 때 결정 |
| [Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/) | 가변 윈도우 | [23](notes/live-coding-mistakes.md#mistake-23) · [24](notes/live-coding-mistakes.md#mistake-24) | `U` 완료 미확인 | 일정 제외 | 다시 풀 때 결정 |
| [Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/) | 양끝 투 포인터 | [10](notes/live-coding-mistakes.md#mistake-10) | `C` 무참조 재구현 대기 | 2026-08-29 | 2026-08-31 |
| [Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/) | 가변 윈도우 | [25](notes/live-coding-mistakes.md#mistake-25) · [26](notes/live-coding-mistakes.md#mistake-26) | `B` 진단 대기 | 2026-08-30 | 진단 후 결정 |
| [Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/) | 단조 큐 | — | `B` 진단 대기 | 2026-08-30 | 진단 후 결정 |
| [Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit](https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/) | 단조 큐 | — | `B` 진단 대기 | 2026-08-30 | 진단 후 결정 |
| [Subarrays with K Different Integers](https://leetcode.com/problems/subarrays-with-k-different-integers/) | 가변 윈도우 | [26](notes/live-coding-mistakes.md#mistake-26) · [27](notes/live-coding-mistakes.md#mistake-27) | `B` 진단 대기 | 2026-08-31 | 진단 후 결정 |
| [Binary Search](https://leetcode.com/problems/binary-search/) | 이분 탐색 | — | `B` 진단 대기 | 2026-08-31 | 진단 후 결정 |
| [Two Sum II](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) | 양끝 투 포인터 | [16](notes/live-coding-mistakes.md#mistake-16) | `B` 진단 대기 | 2026-08-31 | 진단 후 결정 |
| [3Sum](https://leetcode.com/problems/3sum/) | 고정값+투 포인터 | [6](notes/live-coding-mistakes.md#mistake-6) · [10](notes/live-coding-mistakes.md#mistake-10) · [11](notes/live-coding-mistakes.md#mistake-11) | `B` 진단 대기 | 2026-08-31 | 진단 후 결정 |

### 표 갱신 규칙

- 구두 설명과 무참조 구현을 모두 통과하면 `A`로 변경하고 7일 뒤를 다음 복습일로 적는다.
- 아이디어는 설명했지만 구현 또는 반례 검증에 실패하면 `B`로 유지하고 48시간 뒤를 적는다.
- 정답이나 기존 코드를 확인하면 `C`로 변경하고 48시간 안에 무참조 재구현 일정을 잡는다.
- 새 실수가 기존 번호와 같은 원인이면 해당 번호 링크를 문제 행에 추가한다.
- 새 번호가 생기면 `mistake-N` 고정 앵커를 추가한 뒤 링크한다.

## 한 문제 복습 절차

```text
1. 문제 계약을 한 문장으로 설명한다.
2. 기준 풀이와 병목을 설명한다.
3. 최적화에 필요한 상태와 반복 불변식을 말한다.
4. 시간·보조 공간 복잡도의 근거를 말한다.
5. 지정된 문제만 기존 코드 없이 구현하고 반례로 검증한다.
```

- 구두 점검: 문제당 최대 7분
- 무참조 구현: 문제당 최대 20분
- 막히면 정답을 보지 않고 비어 있는 논리 한 단계만 기록한다.
- 실패한 문제만 48시간 일정으로 넘긴다.

## 1차 진단 일정

완료가 확인된 7문제와 재구현 중인 3문제만 일정에 포함한다.

| 날짜 | 구두 점검 | 무참조 구현 |
|---|---|---|
| 2026-08-27 | `Minimum Window Substring` | `Container With Most Water` |
| 2026-08-28 | `Sliding Window Maximum` | `Remove Duplicates from Sorted Array` |
| 2026-08-29 | `Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit` | `Trapping Rain Water` |
| 2026-08-30 | `Subarrays with K Different Integers`, `Binary Search` | 가장 불안한 문제 1개 |
| 2026-08-31 | `Two Sum II`, `3Sum` | 가장 불안한 문제 1개 |

## 48시간 재확인

1차 진단에서 `B` 또는 `C`로 판정된 문제만 기존 코드 없이 다시 구현한다.

| 1차 진단일 | 48시간 재확인일 |
|---|---|
| 2026-08-27 | 2026-08-29 |
| 2026-08-28 | 2026-08-30 |
| 2026-08-29 | 2026-08-31 |
| 2026-08-30 | 2026-09-01 |
| 2026-08-31 | 2026-09-02 |

## 7일 재확인

48시간 재확인에 성공한 문제도 7일 뒤 문제명과 기존 코드를 보지 않고 다시 설명한다. 구현이 흔들린 문제만 재구현한다.

| 1차 진단일 | 7일 재확인일 |
|---|---|
| 2026-08-27 | 2026-09-03 |
| 2026-08-28 | 2026-09-04 |
| 2026-08-29 | 2026-09-05 |
| 2026-08-30 | 2026-09-06 |
| 2026-08-31 | 2026-09-07 |

## 실행 기록

| 날짜 | 문제 | 계약 | 불변식 | 복잡도 | 무참조 구현 | 상태 | 다음 확인일 |
|---|---|---|---|---|---|---|---|
| 2026-08-27 | `Container With Most Water` | [x] | [x] | [x] | [ ] 포인터 이동 힌트 사용 | `B` | 2026-08-29 |
| 2026-08-27 | `Two Sum` | [x] | [x] 조회 후 저장 | [x] 완전탐색 O(N²), 해시 기대 O(N) | [ ] 해시 정답 확인 | `C` | 2026-08-29 |

## 오늘의 시작점

2026-08-27에는 `Container With Most Water` 재구현 후 `Minimum Window Substring` 구두 점검을 진행한다.

첫 질문:

```text
Minimum Window Substring에서 required, window, formed가 각각 무엇을 뜻하고,
윈도우가 유효한 조건을 식으로 설명한다.
```
