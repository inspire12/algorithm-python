# 현재 학습 체크포인트

> 참고용 이전 뷰입니다. 문제 상태와 다음 행동의 기준은 `study/problem-registry.json`이며, 이 문서로 상태를 결정하지 않습니다.

- 마지막 갱신: 2026-08-27
- 학습 목표: 알고리즘 풀이뿐 아니라 라이브 코딩·기술 면접에서 아이디어와 최적화 근거를 조리 있게 설명하기

## 최근 완료

1. [Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/)
   - 필요 빈도와 현재 빈도 분리
   - `have/need` 도출 과정
   - 문자별 위치 큐 방식과 일반 투 포인터 방식 비교
2. [Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/)
   - 최대 힙과 단조 감소 큐 비교
   - `deque`에 값과 인덱스를 저장하는 방식의 차이
   - 만료된 후보와 새 값보다 열등한 후보의 제거 조건
3. [Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit](https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/)
   - 최댓값 단조 감소 큐와 최솟값 단조 증가 큐 동시 관리
   - 유효 조건 `window_max - window_min <= limit`
4. [Subarrays with K Different Integers](https://leetcode.com/problems/subarrays-with-k-different-integers/)
   - `exactly(k) = atMost(k) - atMost(k - 1)` 변환
   - 고정된 `right`에서 유효한 시작점의 수 `right - left + 1`
   - 빈도 딕셔너리와 `distinct`를 분리하는 방식 및 0인 키를 삭제하고 `len(counts)`를 쓰는 방식 비교
   - 최대 조건을 슬라이딩 윈도우로 관리할 수 있는 단조성 확인
5. [Binary Search](https://leetcode.com/problems/binary-search/)
   - 닫힌 탐색 구간 `[left, right]`와 종료 조건 `left <= right`
   - `mid`가 정답이 아닐 때 `mid + 1`, `mid - 1`로 후보에서 제외
   - 정렬 조건을 근거로 target이 될 수 없는 절반을 제거
   - Python 정수 중간 인덱스 계산 `(left + right) // 2`
6. [Two Sum II - Input Array Is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)
   - 정렬된 배열의 양끝에서 시작하는 투 포인터
   - 합이 작으면 `left += 1`, 크면 `right -= 1`
   - 현재 최소·최대 후보로도 조건을 만족하지 못한다는 근거로 한쪽 값 제거
   - 내부 인덱스는 0-based로 관리하고 반환할 때 1-based로 변환
7. [3Sum](https://leetcode.com/problems/3sum/)
   - 완전탐색 `O(N³)`에서 첫 값을 고정하고 Two Sum II를 적용해 `O(N²)`로 개선
   - 원본 인덱스가 아니라 값 조합을 반환하므로 정렬 가능
   - `i < left < right`로 서로 다른 세 위치 유지
   - 사후 `set` 중복 제거와 탐색 중 같은 값을 건너뛰는 기준 풀이 비교

## 현재 문제

- 복습 문제: [Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/)
- 플랫폼과 번호: LeetCode 76
- 현재 단계: 2026-08-27 복습 일정의 상태와 유효 조건 구두 점검
- 보류 문제: [Find First and Last Position of Element in Sorted Array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/) (LeetCode 34)
- 보류 문제: [Find First and Last Position of Element in Sorted Array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/) (LeetCode 34)

## 재구현 대기

- [Container With Most Water](https://leetcode.com/problems/container-with-most-water/) (LeetCode 11)
  - 2026-08-27 포인터 이동 힌트 후 단일 `while`문 구현 및 통과
  - 2026-08-29 힌트 없이 다시 구현해야 완료
- [Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/) (LeetCode 26)
  - 새 배열이 아니라 원본 `nums[:k]`를 수정해야 하는 계약 재확인
  - `nums[:write]`에 고유 값이 저장된다는 불변식으로 무참조 재구현
- [Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/) (LeetCode 42)
  - 표준 양끝 투 포인터와 사용자가 설계한 정방향·역방향 2단계 풀이를 이해함
  - 기존 코드 없이 위치별 경계 불변식을 세우고 재구현해야 완료

## 현재까지 이해한 내용

- 푼 문제 19개를 5일 동안 진단하고, 실패 문제를 48시간·7일 후 재확인하기로 했다.

## 아직 확인할 내용

- `required`, `window`, `formed`의 역할 구분
- 윈도우 유효 조건과 오른쪽 추가·왼쪽 제거 시 `formed` 갱신
- 완전탐색의 병목과 슬라이딩 윈도우 최적화 근거
- 시간 `O(N)`, 보조 공간 `O(U)`의 근거

## 복습 계획

전체 19문제의 최신 일정과 실행 기록은 [푼 문제 복습 계획](review-plan.md)에서 관리한다. 아래 기존 일정은 2026-08-27 계획으로 대체되었다.

### 2026-08-26: 최근 문제 진단 복습

- `Minimum Window Substring`: 필요 빈도·현재 빈도·`formed`의 불변식을 말하고 빈 파일에서 재구현
- `Sliding Window Maximum`: deque에 인덱스를 저장하는 이유와 앞·뒤 제거 조건을 코드 없이 설명
- `Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit`: 두 단조 큐의 불변식과 `left` 이동 조건을 코드 없이 설명
- 각 문제는 정답을 읽지 않고 시작하며, 막힌 지점을 다음 재구현 대상으로 기록

### 2026-08-27: 이전 P0 문제 압축 복습 1

- `Two Sum`
- `Valid Parentheses`
- `Longest Substring Without Repeating Characters`
- `Maximum Average Subarray I`
- `Minimum Size Subarray Sum`
- 문제별로 문제 계약, 핵심 상태, 대표 반례를 말하고 가장 불안한 한 문제만 재구현

### 2026-08-28: 이전 P0 문제 압축 복습 2

- `Fruit Into Baskets`
- `Permutation in String`
- `Max Consecutive Ones III`
- `Longest Repeating Character Replacement`
- 문제별로 윈도우 유효식과 `추가 → 복구 → 답 갱신` 순서를 말하고 가장 불안한 한 문제만 재구현

### 2026-09-02: 최근 문제 7일 재확인

- 최근 완료한 세 문제를 AI와 기존 코드 없이 다시 설명
- 2026-08-26에 막혔던 문제를 빈 파일에서 재구현
- 성공 여부와 새 반례를 `study/notes/live-coding-mistakes.md`의 재연습 기록에 반영

### 완료 판정

- 문제 계약을 한 문장으로 정확히 설명한다.
- 기준 풀이의 병목과 최적화 근거를 설명한다.
- 상태와 불변식, 갱신 순서를 구현 가능한 문장으로 말한다.
- 시간·보조 공간 복잡도를 근거와 함께 말한다.
- 지정된 재구현 문제는 힌트와 기존 코드 없이 통과한다.

## 다음 질문

```text
Minimum Window Substring에서 required, window, formed가 각각 무엇을 뜻하고,
윈도우가 유효한 조건을 식으로 설명해보자.
```

## 세션 재개 문구

새 세션에서는 다음처럼 요청하면 된다.

```text
학습 체크포인트를 읽고 다음 질문부터 이어서 진행해줘.
```
