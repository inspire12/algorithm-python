# 라이브 코딩 오답노트

이 문서는 틀린 문제의 정답 코드를 모으는 곳이 아니라, 반복해서 틀릴 수 있는 **판단과 구현 습관**을 기록하는 곳입니다.

## 분류 기준

오답은 발생한 문제의 유형이 아니라 **실패한 사고 단계**를 기준으로 분류합니다. 같은 실수가 다른 알고리즘에서도 반복될 수 있기 때문입니다.

| 코드 | 분류 | 판단 기준 |
|---|---|---|
| `REQ` | 요구사항 해석 | 반환값, 비교 조건, 고정·가변 길이를 잘못 읽음 |
| `DESIGN` | 풀이 설계 | 알고리즘의 사용 조건이나 완전탐색에서 최적화되는 지점을 놓침 |
| `STATE` | 상태·불변식 | 필요한 상태, 현재 구간, 갱신 순서, 포인터 이동을 잘못 정의함 |
| `BOUNDARY` | 인덱스·경계 | 포함 범위, 구간 길이, 누적합, 초기값을 잘못 계산함 |
| `DS` | 자료구조 | 스택·큐·해시 등 자료구조의 역할이나 저장 정보를 혼동함 |
| `PYTHON` | Python 구현 | API, 문법, 불필요한 복사 등 언어 구현에서 실수함 |
| `COMPLEXITY` | 복잡도 | 시간·보조 공간·빅오 표기를 잘못 계산함 |
| `COMM` | 라이브 설명 | 단순 풀이, 선택 근거, 복잡도 설명 순서를 건너뜀 |

## 우선순위 기준

| 우선순위 | 의미 | 복습 규칙 |
|---|---|---|
| `P0` | 오답이나 예외를 직접 만드는 실수 | 다음 문제 전에 반례로 다시 확인 |
| `P1` | 시간·공간 초과 또는 구현 불안정을 만드는 실수 | 같은 유형을 풀기 전에 스니펫 재현 |
| `P2` | 답은 맞아도 면접 설명의 정확도를 낮추는 실수 | 주간 라이브 연습 전에 구두 복습 |

## 분류별 색인

| 번호 | 핵심 실수 | 주 분류 | 우선순위 | 재확인 조건 |
|---:|---|---|---|---|
| 1 | 반환할 대상을 다르게 이해함 | `REQ` | `P0` | 문제를 읽고 입출력을 한 문장으로 말하기 |
| 2 | 입력 공간과 보조 공간 혼동 | `COMPLEXITY` | `P2` | 새 자료구조에 최대 몇 개가 저장되는지 계산 |
| 3 | 빅오에 상수 배수를 남김 | `COMPLEXITY` | `P2` | 지배항만 남겨 다시 표현 |
| 4 | 정렬 조건과 원본 인덱스 누락 | `DESIGN` | `P0` | 정렬 전제와 원본 순서 필요 여부 확인 |
| 5 | 큐와 스택 명칭 혼동 | `DS` | `P1` | FIFO·LIFO와 꺼내는 대상을 설명 |
| 6 | Python API·문법 혼동 | `PYTHON` | `P1` | 빈 파일에서 리스트 스택 재현 |
| 7 | 딕셔너리 키·값 방향 반전 | `DS` | `P0` | 키로 무엇을 조회해 어떤 값을 얻는지 말하기 |
| 8 | 스택 제거에 슬라이싱 사용 | `PYTHON` | `P1` | 반복문 안의 복사 연산 확인 |
| 9 | 완전탐색 설명 생략 | `COMM` | `P2` | 단순 풀이 → 병목 → 최적화 순서로 설명 |
| 10 | 상태를 구현 불가능하게 정의 | `STATE` | `P0` | 상태를 실제 변수 단위로 작성 |
| 11 | 중복 시 구간을 지나치게 제거 | `STATE` | `P0` | 제거해야 할 최소 경계를 계산 |
| 12 | 전체 기록과 현재 윈도우 혼동 | `STATE` | `P0` | 이전 위치가 현재 구간 안인지 확인 |
| 13 | `정확히 k` 조건 누락 | `REQ` | `P0` | 비교 조건을 연산자로 옮기기 |
| 14 | 누적합에서 시작 원소까지 제거 | `BOUNDARY` | `P0` | `[left, right]`를 작은 배열로 직접 계산 |
| 15 | 정답 가능한 값을 실패 상태로 사용 | `BOUNDARY` | `P0` | 초기값이 실제 정답이 될 수 있는지 확인 |
| 16 | 가변 윈도우 이동 방향 반전 | `STATE` | `P0` | 각 포인터 이동이 상태를 증감시키는지 설명 |
| 17 | 슬라이스 순회 인덱스를 원본 인덱스로 사용 | `BOUNDARY` | `P0` | 슬라이스·enumerate의 인덱스 기준 확인 |
| 18 | 현재 값을 반영하기 전에 유효성 검사 | `STATE` | `P0` | 추가 → 복구 → 답 갱신 순서 확인 |
| 19 | 제거할 종류를 윈도우 첫 값으로 고정 | `STATE` | `P0` | 저장한 상태로 제거 경계를 증명 |
| 20 | 자료구조 선언과 API가 불일치 | `PYTHON` | `P0` | 변수 타입과 사용 연산을 함께 확인 |
| 21 | 최댓값을 현재 구간 길이처럼 변경 | `STATE` | `P0` | 현재 상태와 누적 정답 변수를 분리 |
| 22 | 허용되는 0도 연속 구간에서 제외 | `REQ` | `P0` | 문제 조건을 윈도우 유효식으로 변환 |
| 23 | 실제 변경 대상을 직접 선택하려 함 | `DESIGN` | `P0` | 행동을 필요한 최소 작업 횟수로 변환 |
| 24 | 윈도우 위반 조건을 식으로 만들지 못함 | `STATE` | `P0` | 목표 상태에서 벗어난 원소 수 계산 |
| 25 | 필요한 문자 종류와 개수를 혼동함 | `STATE` | `P0` | `required`, `window`, `formed`의 역할을 구분 |
| 26 | 연속 부분 문자열의 후보 수와 풀이 단계의 복잡도를 혼동함 | `COMPLEXITY` | `P1` | 후보 수 × 후보당 검사 비용으로 분리 계산 |
| 27 | `정확히 K`를 직접 관리하려 하고 단조로운 `최대 K` 조건으로 변환하지 못함 | `DESIGN` | `P1` | `atMost(K) - atMost(K-1)` 적용 조건 확인 |
| 28 | 2차원 배열에서 행·열 인덱스와 길이를 반대로 비교함 | `BOUNDARY` | `P0` | `grid[row][column]`, `rows`, `columns`를 먼저 선언 |
| 29 | 그래프 문제의 인접 리스트·상태 배열·큐 순회 뼈대를 재현하지 못함 | `DS` | `P1` | 간선 의미를 말한 뒤 `graph`, 상태 배열, 시작 큐 선언 |

## 상황별 복습 경로

### 문제를 읽은 직후

`1 → 13 → 4 → 9` 순서로 확인합니다.

```text
무엇을 반환하는가?
조건은 ==, >=, <= 중 무엇인가?
선택한 알고리즘의 전제는 성립하는가?
단순 풀이에서 무엇을 줄였는가?
```

### 구간·포인터 문제를 구현하기 전

`10 → 11 → 12 → 14 → 15 → 16` 순서로 확인합니다.

```text
현재 구간은 정확히 [left, right] 중 어디인가?
포인터는 왜 그 위치로 이동하는가?
상태가 유효해진 뒤 답을 갱신하는가?
경계와 초기값이 실제 정답과 충돌하지 않는가?
```

### Python 코드를 제출하기 전

`5 → 6 → 7 → 8 → 2 → 3` 순서로 확인합니다.

```text
자료구조의 동작과 이름이 일치하는가?
사용한 API가 Python 문법에 맞는가?
키와 값의 방향이 맞는가?
반복문 안에 불필요한 복사가 있는가?
최종 시간·보조 공간 복잡도는 무엇인가?
```

## 기록 방식

새 오답은 아래 형식으로 추가합니다.

```text
번호와 제목:
문제:
플랫폼과 번호:
링크:
분류 코드:
우선순위:
발견한 문제와 반례:
실수한 판단:
교정할 불변식 또는 공식:
48시간 재확인:
7일 재확인:
```

상세 기록은 발생 순서를 유지합니다. 같은 원인의 실수가 다시 나오면 새 번호를 만들지 않고 기존 항목의 반례와 재연습 기록에 누적합니다.

<a id="mistake-1"></a>

## 1. 문제에서 요구한 반환값을 바꿔 이해함

### 실수

`Two Sum`에서 인덱스 쌍 하나를 반환하는 문제를 인덱스 쌍의 개수를 구하는 문제로 설명했습니다.

### 교정

문제를 읽은 직후 다음을 분리해서 말합니다.

```text
입력:
반환값:
정답이 여러 개일 때의 조건:
같은 원소를 다시 사용할 수 있는지:
```

### 라이브 코테 답변

> 서로 다른 두 인덱스의 값의 합이 target이 되는 인덱스 한 쌍을 반환하는 문제입니다.

### 재확인

- [ ] 문제의 목표를 동사 하나로 말했다: `반환 / 판정 / 개수 / 최소 / 최대`
- [ ] 값과 인덱스 중 무엇을 반환하는지 확인했다.

### Remove Duplicates from Sorted Array에서 재발

고유 값을 새 리스트 `answer`에 저장하고 `len(answer)`만 반환했습니다. 이 문제는 `k`만 맞추는 것이 아니라 입력 배열 `nums`를 제자리에서 수정하여 `nums[:k]`에 고유 값들이 정렬 순서대로 들어 있게 해야 합니다.

```text
nums = [1, 1, 2]
반환 k = 2
필수 상태: nums[:2] == [1, 2]
```

새 리스트만 `[1, 2]`가 되고 원본이 `[1, 1, 2]`로 남으면 반환값이 `2`여도 오답입니다. 또한 새 리스트는 `O(N)` 보조 공간을 사용하므로 제자리 `O(1)` 공간 조건도 만족하지 않습니다.

---

<a id="mistake-2"></a>

## 2. 입력 공간과 추가 공간을 혼동함

### 실수

입력 배열 `numbers`의 저장 공간까지 포함하여 완전탐색의 공간 복잡도를 `O(N)`이라고 판단했습니다.

### 교정

별도 설명이 없으면 일반적으로 알고리즘이 입력 외에 사용하는 **보조 공간**을 답합니다.

```text
이중 반복문: 추가 변수만 사용 → O(1)
해시 풀이: 최대 N개의 값과 인덱스 저장 → O(N)
```

### 주의

면접관이 입력을 포함한 전체 메모리를 묻는다면 입력 공간과 보조 공간을 나누어 설명합니다.

### 재확인

- [ ] 입력 자체를 제외한 보조 공간을 계산했는가?
- [ ] 재귀 호출 스택도 포함했는가?
- [ ] 새 배열, 해시맵, 큐에 최대 몇 개가 저장되는가?

---

<a id="mistake-3"></a>

## 3. 빅오에서 상수 배수를 남김

### 실수

이중 반복문의 실행 횟수를 `O(N² / 2)`, 값과 인덱스 저장 공간을 `O(2N)`으로 표현했습니다.

### 교정

빅오는 입력이 커질 때의 증가율을 표현하므로 상수 배수를 제거합니다.

```text
O(N² / 2) = O(N²)
O(2N) = O(N)
O(N) + O(N log N) = O(N log N)
```

실제 연산량을 설명할 때는 “약 `N(N-1)/2`회”라고 말할 수 있지만, 복잡도 표기는 `O(N²)`입니다.

---

<a id="mistake-4"></a>

## 4. 투 포인터의 정렬 조건과 원본 인덱스를 놓침

### 실수

정렬되지 않은 `Two Sum` 입력에 양쪽 투 포인터를 바로 적용하려 했습니다. 제자리 정렬을 사용하면 추가 공간을 `O(1)`로 만들 수 있다고 판단했지만, 원래 인덱스를 반환해야 한다는 조건을 놓쳤습니다.

### 교정

합의 크기에 따라 양쪽 포인터를 이동하려면 값이 정렬되어 있어야 합니다.

```text
값과 원래 인덱스 묶기: O(N) 공간
정렬: O(N log N)
투 포인터 탐색: O(N)
전체: 시간 O(N log N), 추가 공간 O(N)
```

정렬 자체를 제자리에서 수행할 수 있더라도, 이 문제에서는 원래 인덱스를 보존할 정보가 필요합니다.

### 적용 전 질문

- [ ] 포인터를 움직여도 되는 단조성이 있는가?
- [ ] 입력이 이미 정렬되어 있는가?
- [ ] 정렬하면 원래 순서나 인덱스가 필요한가?

### Container With Most Water 재연습에서 추가된 반례

넓이 `(right - left) * min(height[left], height[right])`를 최적화하기 위해 높이를 큰 순서로 정렬하려 했습니다. 그러나 이 문제의 너비는 두 높이의 **원래 인덱스 차이**이므로 높이만 정렬하면 넓이 계산에 필요한 위치 관계가 깨집니다.

```text
height = [1, 100, 1, 100]
```

높이 `100` 두 개의 원래 거리는 `2`이지만, 높이만 정렬한 배열에서의 거리는 원래 너비를 나타내지 않습니다. `(높이, 원래 인덱스)`를 보존하더라도 높이순 탐색만으로 어떤 쌍을 안전하게 제외할지 단조적인 종료 조건이 바로 생기지 않습니다.

이 문제에서는 원래 순서를 유지한 채 최대 너비인 양끝에서 시작하고, 현재 넓이를 제한하는 더 낮은 벽을 이동합니다.

### Two Sum 복습에서 추가된 가지치기 오류

정렬할 때 `(값, 원래 인덱스)`를 함께 저장하여 반환 계약은 보존했지만, `target`보다 큰 값을 미리 제거하려 했습니다. 입력에 음수가 있으므로 값 하나만 target과 비교해서는 후보를 제거할 수 없습니다.

```text
nums = [-5, 10], target = 5
```

`10 > target`이지만 `-5 + 10 = 5`이므로 `10`은 정답에 필요합니다. 음수 target에서도 같은 문제가 발생합니다.

정렬된 배열의 양끝 투 포인터에서는 현재 두 값의 **합**을 target과 비교해서만 한쪽 후보를 제거합니다. 또한 `left`를 이동할 때 `right`를 배열 끝으로 복구하면 같은 후보를 반복 검사하여 최악 `O(N²)`이 됩니다. 두 포인터는 되돌리지 않고 각각 한 방향으로만 이동해야 `O(N)` 탐색이 됩니다.

---

<a id="mistake-5"></a>

## 5. 큐와 스택의 이름을 혼동함

### 실수

괄호 검사에서 동작은 후입선출로 설명했지만 자료구조를 큐라고 불렀습니다.

### 교정

```text
큐:   FIFO, 먼저 넣은 값을 먼저 꺼냄
스택: LIFO, 나중에 넣은 값을 먼저 꺼냄
```

괄호는 가장 최근에 열린 괄호부터 닫혀야 하므로 스택을 사용합니다.

### 불변식

> 스택에는 아직 닫히지 않은 여는 괄호가 등장 순서대로 저장되어 있다.

---

<a id="mistake-6"></a>

## 6. Python 리스트와 문자열 API를 혼동함

### 실수

```python
stack.push(value)
stack.isEmpty()
return false
if !stack:
substring.indexOf(char)
```

### 교정

```python
stack.append(value)
stack.pop()
if not stack:
return False
substring.index(char)
```

문자열은 불변 객체이므로 리스트처럼 `append()`할 수 없습니다.

### 최소 스택 스니펫

```python
stack = []
stack.append(value)
last_value = stack[-1]
popped_value = stack.pop()
is_empty = not stack
```

### Daily Temperatures에서 추가된 중첩 인덱싱

`temperatures[pending_indices[-1]]`는 두 번의 조회를 합친 표현입니다. 먼저 `pending_indices[-1]`로 스택 맨 위에 저장된 원본 배열의 인덱스를 얻고, 그 결과를 `temperatures[...]`에 넣어 해당 온도를 조회합니다.

```python
previous_index = pending_indices[-1]
previous_temperature = temperatures[previous_index]
```

스택이 비어 있을 때 `pending_indices[-1]`를 실행하면 `IndexError`가 발생하므로 반드시 `pending_indices and ...`처럼 비어 있지 않음을 먼저 확인합니다.

### 3Sum에서 리스트를 집합 원소로 사용

3Sum 결과를 `list[list[int]]`로 만든 뒤 `set(answer)`를 반환하려 했습니다. 내부 리스트는 변경 가능한 객체라 해시할 수 없으므로 `TypeError: unhashable type: 'list'`가 발생합니다.

튜플로 변환하면 집합에 넣을 수 있지만, 문제의 반환 계약은 리스트이며 결과를 만든 뒤 집합으로 중복 제거하기보다 정렬된 입력에서 같은 `i`, `left`, `right` 값을 건너뛰는 것이 기준 풀이입니다.

```python
tuple_value = tuple(list_value)  # 해시 가능
```

---

<a id="mistake-7"></a>

## 7. 딕셔너리의 키와 값 방향을 반대로 조회함

### 실수

괄호 딕셔너리를 다음처럼 정의한 뒤 여는 괄호로 조회하려 했습니다.

```python
pairs = {
    ")": "(",
    "]": "[",
    "}": "{",
}

pairs[stack.pop()]  # stack에서는 "("가 나오므로 KeyError
```

### 교정

현재 닫는 괄호가 키이고, 기대하는 여는 괄호가 값입니다.

```python
if not stack or stack.pop() != pairs[char]:
    return False
```

### 재확인

- [ ] 이 딕셔너리의 키는 무엇인가?
- [ ] 조회 결과로 어떤 값을 얻는가?
- [ ] 현재 가지고 있는 값으로 실제 조회할 수 있는가?

---

<a id="mistake-8"></a>

## 8. 슬라이싱으로 스택을 제거하려 함

### 실수

```python
stack = stack[0:-2]
```

마지막 한 원소를 제거하려 했지만 마지막 두 원소를 제외했고, 매번 새 리스트를 만들었습니다.

### 교정

```python
stack.pop()
```

슬라이싱을 반복문 안에서 사용하면 매번 복사가 발생하여 의도한 `O(N)` 풀이가 `O(N²)`이 될 수 있습니다.

---

<a id="mistake-9"></a>

## 9. 완전탐색 설명을 건너뛰고 최적 풀이부터 말함

### 실수

중복 없는 가장 긴 부분 문자열 문제에서 완전탐색을 묻는 질문에 바로 해시맵 풀이를 설명했습니다.

### 교정

라이브 코테에서는 다음 순서를 지킵니다.

```text
정확한 단순 풀이
→ 단순 풀이의 복잡도
→ 반복되는 계산
→ 제거할 방법
→ 최적 풀이와 복잡도
```

최적 풀이를 알고 있더라도 완전탐색을 짧게 설명하면 정확성 근거와 최적화 이유를 전달할 수 있습니다.

---

<a id="mistake-10"></a>

## 10. 슬라이딩 윈도우의 상태를 추상적으로 정의함

### 실수

필요한 상태를 “연속이 이어지고 있는지 판단”이라고만 표현했습니다.

### 교정

구현 가능한 변수 단위로 상태를 정의합니다.

```text
left: 현재 유효 구간의 시작 인덱스
right: 현재 처리 중인 인덱스
last_seen: 문자별 마지막 등장 위치
max_length: 지금까지의 최대 유효 구간 길이
```

### 불변식

> 반복이 끝났을 때 `text[left:right + 1]`은 중복 문자가 없는 구간이다.

### 3Sum 재연습에서 재발

정렬 후 “음수와 양수로 나누고 세 번째 값을 이분 탐색한 다음 `left`, `right`를 좁힌다”고 설명하여, 무엇을 고정하고 어떤 합을 비교하는지 구현 가능한 상태가 정해지지 않았습니다.

3Sum의 정석 투 포인터 상태는 다음과 같습니다.

```text
i: 첫 번째 값으로 고정한 인덱스
left = i + 1: 두 번째 값 후보
right = len(nums) - 1: 세 번째 값 후보
current_sum = nums[i] + nums[left] + nums[right]
```

```text
current_sum < 0 → left += 1
current_sum > 0 → right -= 1
current_sum == 0 → 조합 기록 후 양쪽의 중복 값 건너뛰기
```

별도의 이분 탐색은 필요하지 않습니다. 두 인덱스를 고정하고 남은 값을 이분 탐색하면 `O(N² log N)` 방식은 가능하지만, 이를 투 포인터와 동시에 섞지 않습니다.

### Trapping Rain Water에서 재발

왼쪽 벽이 더 높은 채 배열 끝에 도달하는 경우를 “윈도우의 max를 후보군으로 설정하고 계산한다”고 표현했지만, 후보의 인덱스·갱신 조건·어느 범위의 물을 언제 확정하는지가 정해지지 않았습니다.

```text
height = [5, 4, 1, 2]
```

인덱스 2에서 왼쪽 최고 벽은 `5`, 오른쪽 최고 벽은 `2`이므로 물은 `min(5, 2) - 1 = 1`입니다. 왼쪽 벽만 기준으로 `5 - 1 = 4`를 더하면 과대 계산합니다.

위치별 상태를 다음처럼 구현 가능한 변수로 먼저 고정합니다.

```text
left_max: 현재 위치까지 왼쪽에서 본 최고 높이
right_max: 현재 위치까지 오른쪽에서 본 최고 높이
water_at_i = max(0, min(left_max, right_max) - height[i])
```

투 포인터 풀이에서는 `left_max <= right_max`일 때 왼쪽 위치의 물을 확정하고, 반대일 때 오른쪽 위치의 물을 확정합니다.

### Median of Two Sorted Arrays 병합 기준 풀이에서 재발

`nums1_index`, `nums2_index`, `len(sort_merged)`, 반복 변수 `i`가 각각 무엇을 뜻하는지 고정하지 않은 채 서로 계산에 사용했습니다. 배열 하나가 소진된 분기에서는 남은 배열의 값을 결과에 추가하지 않고 인덱스만 증가시켰고, 중앙값 판정에는 전체 길이 대신 반복 변수 `i`의 홀짝을 사용했습니다.

병합 기준 풀이의 반복 시작 상태는 다음처럼 고정합니다.

```text
i: nums1에서 다음에 읽을 인덱스
j: nums2에서 다음에 읽을 인덱스
merged: 두 배열에서 이미 소비한 값들이 정렬된 상태로 저장된 결과
len(merged) == i + j
```

중앙값의 홀짝은 반복 횟수가 아니라 전체 길이 `m + n`으로 판단합니다.

직접 구현에서는 미완성 구간의 최대 높이 `max_in_window`를 그 구간의 모든 위치에 대한 오른쪽 벽으로 사용했습니다.

```text
height = [5, 2, 4, 1, 2]
```

구간 최대 높이 `4`는 인덱스 3과 4의 왼쪽에 있으므로 두 위치의 오른쪽 벽이 될 수 없습니다. 이 방식은 `7`을 계산하지만 실제 물의 양은 `3`입니다.

```text
인덱스 1: min(5, 4) - 2 = 2
인덱스 3: min(5, 2) - 1 = 1
합계 = 3
```

미완성 오른쪽 구간을 별도로 처리하려면 배열 끝에서 왼쪽으로 이동하며 `right_max`를 갱신해야 합니다. 또는 처음부터 양끝 투 포인터로 각 위치에서 실제로 그 위치의 왼쪽과 오른쪽에 존재하는 경계를 사용합니다.


### 2026-10-08 히스토그램 재연습: 후보 상태 부족

- 문제: [Largest Rectangle in Histogram — LeetCode 84](https://leetcode.com/problems/largest-rectangle-in-histogram/)
- 잘못된 판단: 하나의 left와 최소 높이만 관리하면서 높아지면 이전 구간을 버리고, 낮아지면 최소 높이를 갱신하지 않았다.
- 반례: [2,3]에서 넓이 4 후보를 버려 3만 계산한다. [3,2]에서는 불가능한 넓이 6을 계산한다.
- 교정할 불변식: (높이,start) 후보를 비감소 높이 스택에 보존한다. 반복 시작 시 각 후보는 start부터 right-1까지 해당 높이로 유효하다. 낮은 막대를 만나면 높은 후보를 pop하여 height*(right-start)를 확정하고 시작 위치를 상속한다.
- 전체 정답과 불변식을 설명한 뒤 사용자가 이해했다고 응답했다. 독립 재구현은 미확인이다.
- 재확인 일정: 2026-10-10.

---

<a id="mistake-11"></a>

## 11. 중복을 만나면 현재 구간을 지나치게 많이 버림

### 실수

중복 문자를 만나면 `left = right`로 이동하려 했습니다.

### 교정

이전 중복 문자만 제외하면 되므로 이전 위치의 다음 칸으로 이동합니다.

```python
left = last_seen[char] + 1
```

현재 문자도 새로운 유효 구간에 포함되므로 중복 처리 후 `continue`하지 않고 위치와 답을 갱신합니다.

### 3Sum에서 첫 정답 뒤 나머지 후보를 버림

합이 0인 조합 하나를 찾은 직후 `break`하여 같은 고정값 `nums[i]`로 만들 수 있는 다른 조합을 전부 버렸습니다.

```text
nums = [-2, 0, 1, 1, 2]
```

`i = 0`에서 `[-2, 0, 2]`를 찾은 뒤에도 `[-2, 1, 1]`이 남아 있습니다. 따라서 정답을 기록한 뒤 `left += 1`, `right -= 1`로 탐색을 계속하고, 양쪽에서 같은 값만 건너뛰어야 합니다.

---

<a id="mistake-12"></a>

## 12. 전체 과거 기록과 현재 윈도우를 혼동함

### 실수

`last_seen`에 문자가 존재하면 항상 현재 구간의 중복이라고 판단했고, 다음처럼 `left`를 뒤로 이동시켰습니다.

```python
left = last_seen[char] + 1
```

`"abba"`의 마지막 `a`에서 기존 `left=2`가 `1`로 후퇴하여 중복이 있는 `"bba"`를 유효한 구간으로 계산합니다.

### 교정

딕셔너리에는 현재 구간 밖의 오래된 기록도 남아 있습니다.

```python
if char in last_seen:
    left = max(left, last_seen[char] + 1)
```

또는 현재 구간 안에 이전 문자가 있는지 명시적으로 검사합니다.

```python
if char in last_seen and last_seen[char] >= left:
    left = last_seen[char] + 1
```

### 핵심 문장

> 전체 입력에서 이전에 본 적이 있는 것과 현재 윈도우 안에 존재하는 것은 다르다.

### 필수 반례

```python
"abba"    # 정답 2, left가 뒤로 가면 안 됨
"tmmzuxt" # 정답 5, 이전 t는 현재 구간 밖
"dvdf"    # 정답 3
```

---

<a id="mistake-13"></a>

## 13. 고정 길이 조건을 놓치고 가변 윈도우로 해석함

### 실수

`길이가 정확히 k인 연속 구간` 문제에서 구간 길이를 선택할 수 있다고 생각했습니다.

### 교정

```text
정확히 k개 → 고정 윈도우
최대·최소 k개 또는 합 조건 → 가변 윈도우 가능성 검토
```

고정 윈도우에서는 오른쪽 값 하나가 들어오면 왼쪽 값 하나가 나갑니다.

```python
window_sum += numbers[right] - numbers[right - k]
```

### 재확인

- [ ] `정확히 / 이상 / 이하 / 초과 / 미만`을 비교 연산자로 옮겼는가?
- [ ] 윈도우 길이가 고정인지 조건에 따라 변하는지 확인했는가?

---

<a id="mistake-14"></a>

## 14. 누적합에서 시작 원소까지 빼버림

### 실수

인덱스 `i`까지 포함하는 누적합에서 다음 식으로 `[left, right]`를 구하려 했습니다.

```python
prefix[right] - prefix[left]
```

이 식은 `nums[left]`까지 제거하므로 실제 범위는 `[left + 1, right]`입니다.

### 교정

포함형 누적합에서는 시작점 직전까지만 뺍니다.

```python
if left == 0:
    window_sum = prefix[right]
else:
    window_sum = prefix[right] - prefix[left - 1]
```

앞에 `0`을 둔 누적합을 사용하면 경계 처리가 단순합니다.

```python
prefix = [0]
for number in numbers:
    prefix.append(prefix[-1] + number)

window_sum = prefix[right + 1] - prefix[left]
```

### 핵심 문장

> `left`를 포함하려면 `left` 바로 앞까지의 합만 뺀다.

### Median of Two Sorted Arrays에서 배열 소진 경계 오류

다음 미처리 인덱스가 배열 길이와 같으면 이미 소진된 상태인데 `index > len(array)`로 검사했습니다.

```text
유효 인덱스: 0 .. len(array)-1
소진 조건: index >= len(array)
```

`index == len(array)`인 상태에서 `array[index]`를 읽으면 `IndexError`가 발생합니다. 배열이 소진된 분기에서는 인덱스만 증가시키는 것이 아니라 반대 배열의 다음 값을 병합 결과에 추가해야 합니다.

---

<a id="mistake-15"></a>

## 15. 실제 정답이 될 수 있는 값을 실패 상태로 사용함

### 실수

```python
min_length = len(numbers)

if min_length == len(numbers):
    return 0
```

전체 배열만 조건을 만족하면 실제 정답도 `len(numbers)`이므로 실패 상태와 구분되지 않습니다.

```python
numbers = [1, 2, 3, 4, 5]
target = 15
# 정답: 5
```

### 교정

실제 정답으로 나올 수 없는 값을 초기값으로 사용합니다.

```python
min_length = float("inf")
return 0 if min_length == float("inf") else min_length
```

또는 가능한 최대 길이보다 큰 값을 사용합니다.

```python
min_length = len(numbers) + 1
```

### 추가 재연습: Minimum Window Substring (2026-09-01)

최소 시작 인덱스를 구할 때 `left = 1000`으로 초기화했습니다. 문자열 길이가 1000을 넘고 필요한 문자가 그 뒤에만 있으면 실제 시작 인덱스보다 작은 `1000`이 그대로 남습니다.

```python
s = "x" * 1001 + "a"
t = "a"

# 기대 정답: "a"
# left = 1000을 사용한 결과: "xa"
```

인덱스 최솟값은 실제 후보에서 직접 구합니다.

```python
left = min(
    positions[0]
    for positions in window_index.values()
)
```

또는 고정 숫자 대신 `float("inf")`나 입력 길이에서 유도한 값을 사용합니다.

---

<a id="mistake-16"></a>

## 16. 양수 가변 윈도우의 포인터 이동 방향을 반대로 잡음

### 실수

전체 배열에서 시작하여 합이 부족할 때 `right`를 왼쪽으로 줄였습니다.

### 교정

모든 원소가 양수라면 다음 단조성이 성립합니다.

```text
right를 오른쪽으로 이동해 값을 추가 → 합 증가
left를 오른쪽으로 이동해 값을 제거 → 합 감소
```

따라서 최소 길이 문제의 흐름은 다음과 같습니다.

```text
합이 부족함 → right를 확장
합이 충분함 → 답을 기록하고 left를 축소
```

```python
for right, number in enumerate(numbers):
    window_sum += number

    while window_sum >= target:
        min_length = min(min_length, right - left + 1)
        window_sum -= numbers[left]
        left += 1
```

### 재확인

- [ ] 포인터를 움직이면 관리하는 값이 증가하는가, 감소하는가?
- [ ] 조건이 유효할 때 답을 기록한 뒤 상태를 변경하는가?
- [ ] 양수라는 조건이 없다면 같은 단조성이 유지되는가?

### 양끝 투 포인터 재연습에서 추가된 표현 오류

`Two Sum II` 복습에서 “합이 target보다 작으면 왼쪽으로, 크면 오른쪽으로 이동한다”고 표현해 포인터 이름과 실제 이동 방향이 불분명했습니다.

정렬된 배열의 양끝 포인터에서는 다음처럼 구현 가능한 문장으로 말합니다.

```text
현재 합 < target → 작은 값을 키워야 하므로 left를 오른쪽으로 한 칸 이동
현재 합 > target → 큰 값을 줄여야 하므로 right를 왼쪽으로 한 칸 이동
```

예를 들어 `[2, 7, 11, 15]`에서 `2 + 15 > 9`이면 `15`를 유지한 채 `left`를 오른쪽으로 옮기면 합이 더 커지거나 같아집니다. 따라서 `right`가 가리키는 `15`는 어떤 현재 후보와도 정답을 만들 수 없으므로 `right -= 1`로 제외합니다.

### Two Sum II 구현에서 재발

`numbers = [5, 25, 75]`, `target = 100`에서 `left = 0`, `right = 1`로 인접한 두 위치에서 시작하고, 합이 작을 때 `right += 1`, 합이 클 때 `left += 1`로 구현했습니다.

이 방식은 양끝 후보 제거가 아닙니다. `5 + 75 = 80`에서 합이 작다는 이유로 `right`를 배열 밖으로 이동하여, 실제 정답인 `25 + 75`를 검사하지 못하고 `IndexError`가 발생합니다.

```text
초기 상태: left = 0, right = len(numbers) - 1
합 < target: left += 1
합 > target: right -= 1
```

경계를 이동한 직후 인덱싱하는 코드에서는 새 인덱스가 유효한지도 확인해야 합니다. 양끝 투 포인터의 위 갱신 규칙과 `while left < right`를 사용하면 두 포인터가 배열 안에서 서로를 향해 이동합니다.

### Container With Most Water 구현에서 재발

낮은 벽 하나만 이동해야 하는 문제에서 왼쪽과 오른쪽을 각각 내부 `while`로 탐색하고, `left = max_left`로 포인터를 과거 위치로 되돌렸습니다. 이 때문에 각 포인터가 한 방향으로만 이동한다는 불변식과 `O(N)` 근거가 모두 깨집니다.

또한 다음 조건은 현재 제한 높이보다 높은 벽을 계속 건너뛰므로 이동 조건의 방향이 반대입니다.

```python
while current_height <= height[left]:
    left += 1
```

각 반복에서는 현재 두 벽의 넓이를 갱신한 다음, 두 벽 중 더 낮은 쪽 하나만 안쪽으로 한 칸 이동해야 합니다. 포인터를 이전 위치로 복구하지 않습니다.


### 2026-10-09 이진 탐색에서 경계 이동 방향 재발

- 문제: [Search in Rotated Sorted Array — LeetCode 33](https://leetcode.com/problems/search-in-rotated-sorted-array/)
- 잘못된 판단: 오른쪽을 남길 때 left=mid-1, 왼쪽을 남길 때 right=mid+1로 이동했다.
- 반례: [3,1], target=1에서 left가 -1이 된 후 mid=0, left=-1 상태가 반복되어 시간 초과가 발생한다.
- 교정할 불변식: 정답 후보는 닫힌 구간 [left,right]에 남고, 이미 불일치한 mid는 제외한다. 오른쪽 유지 시 left=mid+1, 왼쪽 유지 시 right=mid-1로 구간이 반드시 줄어든다.
- 재확인 일정: 2026-10-10. 수정 후 실행 결과는 아직 미확인이다.

---

<a id="mistake-17"></a>

## 17. 슬라이스 순회 인덱스를 원본 인덱스로 사용함

### 실수

```python
for right, fruit in enumerate(fruits[1:]):
```

`fruits[1:]`은 새 배열이므로 `right`가 다시 `0`부터 시작하지만, 이를 원본 배열의 인덱스로 사용했습니다. 슬라이스 자체도 `O(N)` 추가 공간을 만듭니다.

### 교정

원본 인덱스가 상태에 필요하면 원본 배열을 그대로 순회합니다.

```python
for right, fruit in enumerate(fruits):
    ...
```

일부 구간부터 시작해야 한다면 슬라이스 없이 원본 인덱스를 순회합니다.

```python
for right in range(1, len(fruits)):
    fruit = fruits[right]
```

### 재확인

- [ ] 현재 인덱스는 원본 배열 기준인가, 잘라낸 배열 기준인가?
- [ ] 슬라이스가 시간·공간 복사를 만들지 않는가?

### `enumerate(..., start=1)`의 반복 시작 위치를 오해함

`enumerate(nums, start=1)`을 사용하면 `nums[1]`부터 순회한다고 생각할 수 있지만, 실제로는 첫 원소 `nums[0]`부터 모두 순회하면서 반환하는 번호만 1부터 시작합니다.

```python
for index, value in enumerate(nums, start=1):
    # 첫 반복: index == 1, value == nums[0]
```

실제로 두 번째 원소부터 읽으려면 원본 인덱스를 유지하는 `range(1, len(nums))`를 사용합니다.

---

<a id="mistake-18"></a>

## 18. 현재 값을 반영하기 전에 유효성을 검사함

### 실수

새 과일을 딕셔너리에 넣기 전에 `len(last_fruit_index) > 2`를 검사했습니다. 기존 종류가 두 개일 때 세 번째 종류가 들어와도 검사 시점에는 길이가 아직 `2`이므로 위반을 발견하지 못했습니다.

### 교정

슬라이딩 윈도우의 한 반복은 다음 순서로 처리합니다.

```text
1. right의 현재 값을 상태에 추가
2. 조건을 위반하는 동안 left를 이동해 복구
3. 유효한 상태에서 답 갱신
```

```python
last_seen[fruit] = right

if len(last_seen) > 2:
    # 제거할 종류와 새로운 left 결정
    ...

max_length = max(max_length, right - left + 1)
```

### 핵심 문장

> 이번 원소까지 포함한 윈도우가 유효한지를 검사한다.

---

<a id="mistake-19"></a>

## 19. 제거할 종류를 윈도우의 첫 값으로 고정함

### 실수

세 번째 과일 종류가 들어오면 `fruits[left]`의 종류를 제거하려 했습니다. 마지막 위치 방식에서는 윈도우의 첫 값이 아니라 **마지막 등장 위치가 가장 작은 종류**를 제거해야 합니다.

```python
fruits = [1, 2, 1, 3]
last_seen = {1: 2, 2: 1, 3: 3}
```

여기서는 종류 `1`이 아니라 마지막 위치가 `1`인 종류 `2`를 제거합니다.

### 교정

```python
fruit_to_remove = min(last_seen, key=last_seen.get)
left = last_seen[fruit_to_remove] + 1
del last_seen[fruit_to_remove]
```

### 불변식

> 답을 갱신할 때 `last_seen`에는 현재 윈도우의 최대 두 종류와 각 종류의 마지막 위치만 저장되어 있다.

### 재확인

- [ ] 제거 대상을 직감으로 고르지 않고 저장한 상태로 증명했는가?
- [ ] 제거 후 `left` 오른쪽에 삭제한 종류가 남아 있지 않은가?

---

<a id="mistake-20"></a>

## 20. 자료구조 선언과 사용한 API가 불일치함

### 실수

```python
change_histories = []
min(change_histories, key=change_histories.get)
```

리스트로 선언한 뒤 딕셔너리의 `get()` API를 사용했습니다.

### 교정

상태를 정의할 때 타입과 필요한 연산을 함께 적습니다.

```text
zero_positions: 오래된 위치부터 제거 → deque
counts: 값별 개수 조회·수정 → dict
stack: 마지막 값 추가·제거 → list
```

---

<a id="mistake-21"></a>

## 21. 누적 정답을 현재 구간 길이처럼 변경함

### 실수

```python
max_length = max_length + 1
```

`max_length`는 지금까지 발견한 최대값인데 현재 구간 길이처럼 직접 증가시켰습니다.

### 교정

현재 상태와 누적 정답을 분리합니다.

```python
current_length = right - left + 1
max_length = max(max_length, current_length)
```

### 핵심 문장

> 현재 상태는 매 반복 바뀌고, 누적 정답은 유효한 현재 상태와 비교해서만 갱신한다.

### Container With Most Water에서 재발

`current_height`를 현재 `(left, right)` 쌍의 제한 높이로 사용하면서, `current_area > max_area`일 때만 갱신했습니다. 그 결과 포인터가 바뀐 뒤에도 이전 쌍의 높이를 이동 조건에 사용했습니다.

```text
current_height = min(height[left], height[right])  # 매 반복의 현재 상태
current_area = (right - left) * current_height     # 매 반복의 현재 상태
max_area = max(max_area, current_area)             # 지금까지의 누적 정답
```

현재 쌍의 상태는 매 반복 다시 계산하고, `max_area`만 과거의 최댓값을 유지해야 합니다. 오른쪽 포인터를 이동한 루프에서는 `max_area` 자체를 갱신하지 않아 더 큰 넓이를 발견해도 반환값에 반영되지 않는 오류도 있었습니다.

---

<a id="mistake-22"></a>

## 22. 변경 가능한 0을 연속 구간에서 제외함

### 실수

`0`을 만나면 `is_straight = False`로 두어 연속 구간을 끊었습니다. 하지만 문제에서는 최대 `k`개의 0을 1로 간주할 수 있습니다.

### 교정

문제의 행동을 실제 배열 변경이 아니라 윈도우의 유효 조건으로 바꿉니다.

```text
0을 최대 k개 바꿀 수 있다
→ 현재 구간의 0 개수가 k개 이하다
→ zero_count <= k
```

```python
if number == 0:
    zero_count += 1

while zero_count > k:
    if numbers[left] == 0:
        zero_count -= 1
    left += 1
```

---

<a id="mistake-23"></a>

## 23. 실제 변경 대상을 직접 선택하려 함

### 실수

`최대 k개의 문자를 바꿀 수 있다`는 표현을 보고 목표 문자와 변경할 위치의 조합을 직접 선택하려 했습니다.

### 교정

작업을 실제로 수행하지 않고, 현재 구간을 목표 상태로 만드는 데 필요한 **최소 작업 횟수**를 계산합니다.

```text
목표: 구간을 같은 문자로 통일
가장 유리한 선택: 최대 빈도 문자를 유지
필요한 변경: 구간 길이 - 최대 빈도
```

### 알아볼 단서

```text
최대 k개 변경·삭제·수정·예외 허용
→ 무엇을 고를지보다 현재 상태의 위반 개수를 먼저 계산
```

---

<a id="mistake-24"></a>

## 24. 윈도우의 위반 조건을 식으로 만들지 못함

### 실수

문자 교체 문제에서 목표 문자를 정하지 못해 윈도우의 유효성을 판정할 수 없었습니다.

### 교정

문제의 자연어 조건을 부등식으로 변환합니다.

```python
window_length = right - left + 1
required_changes = window_length - max_frequency
is_valid = required_changes <= k
```

조건을 위반하면:

```python
while right - left + 1 - max_frequency > k:
    counts[text[left]] -= 1
    left += 1
```

### 떠올리는 질문

```text
1. 현재 구간의 목표 상태는 무엇인가?
2. 무엇을 최대한 남기는 것이 유리한가?
3. 목표에서 벗어난 원소는 몇 개인가?
4. 그 개수가 허용치 k 이하인가?
```

---

<a id="mistake-25"></a>

## 25. 필요한 문자 종류와 개수를 혼동함

### 발견한 문제

- 문제: `Minimum Window Substring`
- 플랫폼과 번호: LeetCode 76
- 링크: https://leetcode.com/problems/minimum-window-substring/

### 실수

현재 윈도우가 `t`를 포함하는지 확인하기 위해 문자별 마지막 위치를 저장하고, 저장된 키의 수를 `len(t)`와 비교하려 했습니다.

```python
location[char] = right

if len(location) == len(t):
    ...
```

하지만 마지막 위치만 저장하면 같은 문자가 몇 개 있는지 알 수 없습니다. 또한 `len(location)`은 서로 다른 문자 종류의 수이고 `len(t)`는 중복을 포함한 전체 문자 수이므로 비교 기준이 다릅니다.

```text
t = "AABC"
서로 다른 문자 종류 = 3
필요한 전체 문자 수 = 4
```

`window["B"] = 4`처럼 윈도우에 들어온 전체 순서를 문자별 개수로 오해하기도 했습니다. `window`는 각 문자가 현재 구간에 몇 번 포함됐는지를 저장해야 합니다.

### 교정

중복 문자를 요구하는 포함 관계는 위치가 아니라 두 개의 빈도표로 관리합니다.

```python
required[char]  # t에서 필요한 개수
window[char]    # 현재 윈도우에 들어 있는 개수
```

`formed`는 포함된 전체 문자 수가 아니라, 필요한 개수를 모두 충족한 **문자 종류의 수**입니다.

```python
window[char] += 1

if char in required and window[char] == required[char]:
    formed += 1
```

필요 개수를 초과한 문자가 추가될 때는 이미 충족한 종류이므로 `formed`를 다시 증가시키지 않습니다.

```text
t = "AABC"
A 1개 → 부족, formed 변화 없음
A 2개 → A 충족, formed += 1
A 3개 → 이미 충족, formed 변화 없음
```

윈도우가 유효한 조건은 다음과 같습니다.

```python
formed == len(required)
```

왼쪽 문자를 제거한 뒤 필요한 개수보다 부족해지는 순간에만 충족 상태를 해제합니다.

```python
window[left_char] -= 1

if left_char in required and window[left_char] < required[left_char]:
    formed -= 1
```

### 불변식

> `required`는 목표 빈도, `window`는 현재 구간의 빈도이며, `formed`는 현재 구간에서 목표 빈도를 충족한 문자 종류의 수이다.

### 재확인

- [ ] 존재 여부가 아니라 필요한 중복 개수까지 확인했는가?
- [ ] 문자 위치와 문자 빈도 중 문제에 필요한 상태를 구분했는가?
- [ ] `len(t)`와 `len(required)`의 의미를 구분했는가?
- [ ] 필요 개수에 정확히 도달할 때만 `formed`를 증가시키는가?
- [ ] 왼쪽 제거 후 필요 개수보다 부족해질 때만 `formed`를 감소시키는가?


### 2026-10-08 재연습

- 문제: [Minimum Window Substring — LeetCode 76](https://leetcode.com/problems/minimum-window-substring/)
- 잘못된 판단: 각 문자 위치 deque의 길이를 `check[char]` 대신 `len(check)`와 비교했다.
- 반례: `s="AB", t="AB"`에서 각 deque 길이는 1이지만 종류 수는 2이므로 `have`가 증가하지 않아 빈 문자열을 반환한다.
- 교정할 불변식: 각 deque는 해당 문자의 최근 위치를 최대 `check[char]`개 유지한다. `have`는 그 필요 개수를 충족한 종류 수이며 `len(check)`와 비교한다.
- 교정 내용을 확인한 후 다음 문제로 이동했다. 수정 코드 실행과 독립 설명은 미확인이다.
- 재확인 일정: 2026-10-10.

---

<a id="mistake-26"></a>

## 26. 연속 부분 문자열의 후보 수와 풀이 단계의 복잡도를 혼동함

### 발견한 문제

- 문제: `Minimum Window Substring`
- 플랫폼과 번호: LeetCode 76
- 링크: https://leetcode.com/problems/minimum-window-substring/
- 발견 단계: 완전탐색과 최적화 설명

### 실수

`s`의 모든 연속 부분 문자열 개수를 다음과 같이 조합의 합으로 계산했습니다.

```text
C(N, 1) + C(N, 2) + ... + C(N, N)
```

이는 위치를 자유롭게 고르는 부분수열에 가까운 계산입니다. 연속 부분 문자열은 시작점과 끝점으로 결정되므로 길이 `k`인 후보는 `N-k+1`개입니다.

또한 모든 후보를 만드는 완전탐색의 비용과, 오른쪽 경계를 확장하고 유효할 때 왼쪽을 줄이는 슬라이딩 윈도우의 비용을 섞어 `O(N * M)`으로 설명했습니다.

### 교정

연속 부분 문자열의 전체 후보 수는 다음과 같습니다.

```text
N + (N-1) + ... + 1
= N(N+1) / 2
= O(N²)
```

복잡도는 `후보 수 × 후보 하나를 처리하는 비용`으로 분리해서 계산합니다.

```text
부분 문자열 후보 생성: O(N²)개
각 후보의 빈도를 처음부터 계산: 최대 O(N)
단순 완전탐색: O(N³)
```

빈도표가 이미 있고 `t`의 문자 종류 `U`개만 검사한다면 검사는 `O(U)`이므로 `O(N²U)`로 구분해 설명할 수 있습니다.

슬라이딩 윈도우는 인접 구간이 대부분의 원소를 공유한다는 점을 이용합니다.

```text
[left, right] → [left, right + 1]
새로 들어온 문자 하나의 빈도만 증가

[left, right] → [left + 1, right]
빠져나간 문자 하나의 빈도만 감소
```

각 포인터가 한 방향으로 최대 `N`번 이동하므로, 유효성 상태를 상수 시간에 갱신하면 전체 윈도우 탐색은 `O(N)`입니다.

### 재연습에서 추가된 반례

`Subarrays with K Different Integers`에서 `nums = [1, 2, 1]`, `right = 2`일 때 현재 `right`에서 끝나는 후보를 묻는 질문에 `[1, 2]`, `[2]`도 포함했습니다. 두 구간은 유효한 부분 배열이지만 끝 인덱스가 `1`이므로 현재 단계에서 셀 후보가 아닙니다.

고정된 `right`에서 시작점만 `left..right` 중 하나로 고르면 후보는 다음 세 개입니다.

```text
start = 0: [1, 2, 1]
start = 1: [2, 1]
start = 2: [1]
```

따라서 현재 단계의 후보 범위는 “전체 배열의 모든 부분 배열”이 아니라 “끝점이 현재 `right`로 고정된 부분 배열”입니다.

### 라이브 코테 설명

> 연속 부분 문자열은 시작점과 끝점으로 결정되므로 후보가 `O(N²)`개입니다. 각 후보의 빈도를 처음부터 만들면 최대 `O(N)`이 추가되어 완전탐색은 `O(N³)`입니다. 인접한 두 구간은 대부분의 문자를 공유하므로, 오른쪽에서 들어온 문자와 왼쪽에서 나간 문자의 빈도만 갱신하면 중복 계산을 제거할 수 있습니다. 두 포인터가 각각 한 방향으로 최대 `N`번 이동하므로 윈도우 탐색은 `O(N)`입니다.

### 재확인

- [ ] 연속 부분 문자열과 부분수열의 후보 수를 구분했는가?
- [ ] 후보 수와 후보당 검사 비용을 곱해 계산했는가?
- [ ] 완전탐색과 최적화 풀이의 연산을 섞어 설명하지 않았는가?
- [ ] `while`이 중첩돼 보여도 각 포인터의 총 이동 횟수로 분석했는가?

---

<a id="mistake-27"></a>

## 27. `정확히 K`를 단조로운 `최대 K` 조건으로 변환하지 못함

### 발견한 문제

- 문제: `Subarrays with K Different Integers`
- 플랫폼과 번호: LeetCode 992
- 링크: https://leetcode.com/problems/subarrays-with-k-different-integers/
- 분류 코드: `DESIGN`
- 우선순위: `P1`

### 실수한 판단

서로 다른 값이 정확히 `K`종류가 되는 순간에 윈도우 하나를 직접 관리하고 개수를 세려 했습니다. 그러나 고정된 `right`에서 정확히 `K`종류인 시작점이 여러 개일 수 있고, 하나의 `left`만으로 그 범위를 바로 표현하기 어렵습니다.

### 교정할 변환

```text
exactly(K) = atMost(K) - atMost(K - 1)
```

`atMost(K)`에는 정확히 1종류부터 K종류까지인 구간이 포함되고, `atMost(K-1)`을 빼면 정확히 K종류인 구간만 남습니다.

고정된 `right`에서 `atMost(limit)`을 만족하도록 복구한 최소 `left`가 있다면, 가능한 시작점은 `left..right`이므로 다음 개수를 누적합니다.

```text
right - left + 1
```

### 다른 문제에 적용할 조건

```text
1. 정확히 K인 구간의 개수를 묻는다.
2. 최대 K라는 조건은 한 방향 슬라이딩 윈도우로 관리할 수 있다.
3. left를 오른쪽으로 이동할 때 측정값이 증가하지 않는 단조성이 있다.
```

적용 예시는 서로 다른 값의 종류, 홀수의 개수, 조건 위반 원소의 개수, 이진 배열의 합입니다. 음수가 포함된 일반 배열의 합처럼 `left` 이동에 따라 측정값이 단조롭게 변하지 않으면 이 방식 대신 누적합 등의 다른 방법을 검토합니다.

### 재확인

- [ ] `정확히 K`를 보자마자 `atMost(K) - atMost(K-1)` 후보를 검토했는가?
- [ ] `atMost` 조건이 슬라이딩 윈도우로 단조롭게 관리되는지 확인했는가?
- [ ] 고정된 `right`에서 유효한 시작점의 개수를 설명할 수 있는가?
- [ ] 음수가 있는 합 문제처럼 적용할 수 없는 반례를 구분했는가?
- 48시간 재확인: 2026-08-28
- 7일 재확인: 2026-09-02

---

<a id="mistake-28"></a>

## 28. 2차원 배열에서 행과 열의 경계를 반대로 사용함

### 발견한 문제

- 문제: `Number of Islands`
- 플랫폼과 번호: LeetCode 200
- 링크: https://leetcode.com/problems/number-of-islands/
- 분류 코드: `BOUNDARY`
- 우선순위: `P0`

### 반례

```python
grid = [
    ["1", "1", "1"],
    ["1", "0", "1"],
]
```

이 격자의 크기는 `2행 × 3열`입니다. 유효한 인덱스는 다음과 같습니다.

```text
row:    0 <= row < 2 == len(grid)
column: 0 <= column < 3 == len(grid[0])
```

### 실수한 판단

`xindex`, `yindex`라는 좌표 이름을 사용하면서 첫 번째 배열 인덱스를 열처럼, 두 번째 배열 인덱스를 행처럼 혼동했습니다. 그 결과 행 인덱스를 `len(grid[0])`과 비교하고 열 인덱스를 `len(grid)`과 비교했습니다.

```python
next_xindex >= len(grid[0])  # 잘못된 행 경계
next_yindex >= len(grid)     # 잘못된 열 경계
```

정사각형 격자에서는 두 길이가 같아 실수가 숨지만 직사각형 격자에서는 유효한 칸을 누락하거나 `IndexError`가 발생합니다.

### 교정할 불변식

```text
grid[row][column]
row_count = len(grid)
column_count = len(grid[0])
```

다음 칸을 읽기 전에 항상 이 조건을 확인합니다.

```python
0 <= next_row < row_count
0 <= next_column < column_count
```

좌표계의 `x`, `y`를 사용해야 한다면 배열 접근은 `grid[y][x]`가 되므로, 격자 문제에서는 `row`, `column` 이름을 우선 사용합니다.

### 재확인

- [ ] 반복 변수 이름을 `row`, `column`으로 선언했는가?
- [ ] `grid[row][column]` 순서로 접근하는가?
- [ ] 행은 `len(grid)`, 열은 `len(grid[0])`과 비교하는가?
- [ ] 정사각형이 아닌 `2 × 3` 반례로 경계를 확인했는가?
- 48시간 재확인: 2026-09-03
- 7일 재확인: 2026-09-08

---

<a id="mistake-29"></a>

## 29. 그래프 문제의 기본 답안 구조를 재현하지 못함

### 발견한 문제

- 문제: `Course Schedule`
- 플랫폼과 번호: LeetCode 207
- 링크: https://leetcode.com/problems/course-schedule/
- 분류 코드: `DS`
- 우선순위: `P1`

### 반례가 되는 입력

```python
num_courses = 4
prerequisites = [
    [1, 0],
    [2, 0],
    [3, 1],
    [3, 2],
]
```

관계 `[course, prerequisite]`를 읽고도 어떤 방향으로 인접 리스트를 만들고 어떤 상태를 배열에 저장해야 하는지 바로 코드로 옮기지 못했습니다.

### 실수한 판단

사이클 판별과 위상 정렬의 의미는 이해했지만, 그래프를 특별한 Python 자료구조로 만들어야 한다고 생각해 구현 시작점이 고정되지 않았습니다. 그 결과 다음 네 상태가 코드 단위로 연결되지 않았습니다.

```text
간선 방향
인접 리스트
진입차수 배열
진입차수 0인 시작 큐
```

### 교정할 최소 템플릿

정점 번호가 `0..node_count-1`이면 리스트의 리스트를 우선 사용합니다.

```python
graph = [[] for _ in range(node_count)]
state = [0] * node_count

for start, end in edges:
    graph[start].append(end)
    state[end] += 1
```

Course Schedule에서는:

```python
for course, prerequisite in prerequisites:
    next_courses[prerequisite].append(course)
    indegree[course] += 1
```

큐 순회 뼈대:

```python
queue = deque(initial_nodes)

while queue:
    current = queue.popleft()

    for neighbor in graph[current]:
        # neighbor 상태 갱신
        # 새로 처리 가능해지면 queue에 추가
```

### 교정할 불변식

> `graph[current]`에는 현재 정점 처리 후 영향을 받는 인접 정점들이 있고, 큐에는 현재 문제의 시작 조건을 만족해 즉시 처리할 수 있는 정점만 들어 있다.

Course Schedule에서는 큐에 남은 선수 조건이 `0`인 과목만 들어 있습니다.

### 재확인

- [ ] 입력 한 쌍의 의미를 방향 간선 한 문장으로 바꿨는가?
- [ ] `graph[node]`에 무엇이 저장되는지 말할 수 있는가?
- [ ] 정점별 상태 배열의 의미를 변수 단위로 정의했는가?
- [ ] 큐나 스택에 처음 들어갈 정점의 조건을 정의했는가?
- [ ] 정점과 간선을 각각 최대 몇 번 처리하는지 설명했는가?
- 48시간 재확인: 2026-09-04
- 7일 재확인: 2026-09-09

---

## 문제 풀이 전 30초 체크

```text
[ ] 반환해야 하는 것이 값, 인덱스, 개수, 길이 중 무엇인가?
[ ] 입력 크기가 허용하는 복잡도는?
[ ] 보조 공간에는 무엇이 최대 몇 개 저장되는가?
[ ] 자료구조의 불변식은 무엇인가?
[ ] 포인터는 왜, 정확히 어디로 이동하는가?
[ ] 상태를 읽는 순서와 갱신하는 순서는?
[ ] 답은 상태가 유효해진 뒤 갱신하는가?
[ ] 전체 기록과 현재 구간의 기록을 구분했는가?
```

## 재연습 기록

| 날짜 | 문제 | 실수 번호 | 분류 | 우선순위 | 힌트 없이 수정 | 다음 확인일 |
|---|---|---:|---|---|---|---|
| 2026-08-11 | [Two Sum](https://leetcode.com/problems/two-sum/) | 1~4 | `REQ`, `DESIGN`, `COMPLEXITY` | `P0` | [ ] | 2026-08-13 / 2026-08-18 |
| 2026-08-11 | [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) | 5~8 | `DS`, `PYTHON` | `P0` | [ ] | 2026-08-13 / 2026-08-18 |
| 2026-08-11 | [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | 9~12 | `STATE`, `COMM` | `P0` | [ ] | 2026-08-13 / 2026-08-18 |
| 2026-08-11 | [Maximum Average Subarray I](https://leetcode.com/problems/maximum-average-subarray-i/) | 13 | `REQ` | `P0` | [ ] | 2026-08-13 / 2026-08-18 |
| 2026-08-11 | [Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/) | 14~16 | `BOUNDARY`, `STATE` | `P0` | [ ] | 2026-08-13 / 2026-08-18 |
| 2026-08-11 | [Fruit Into Baskets](https://leetcode.com/problems/fruit-into-baskets/) | 17~19 | `BOUNDARY`, `STATE` | `P0` | [ ] | 2026-08-13 / 2026-08-18 |
| 2026-08-12 | [Permutation in String](https://leetcode.com/problems/permutation-in-string/) | 3, 10, 13, 18 | `COMPLEXITY`, `REQ`, `STATE` | `P0` | [ ] | 2026-08-14 / 2026-08-19 |
| 2026-08-12 | [Max Consecutive Ones III](https://leetcode.com/problems/max-consecutive-ones-iii/) | 18, 20~22 | `REQ`, `STATE`, `PYTHON` | `P0` | [ ] | 2026-08-14 / 2026-08-19 |
| 2026-08-13 | [Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/) | 23~24 | `DESIGN`, `STATE` | `P0` | [ ] | 2026-08-15 / 2026-08-20 |
| 2026-08-14 | [Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/) | 25 | `STATE` | `P0` | [ ] | 2026-08-16 / 2026-08-21 |
| 2026-08-18 | [Minimum Window Substring 설명 재연습](https://leetcode.com/problems/minimum-window-substring/) | 26 | `COMPLEXITY` | `P1` | [ ] | 2026-08-20 / 2026-08-25 |
| 2026-08-26 | [Subarrays with K Different Integers](https://leetcode.com/problems/subarrays-with-k-different-integers/) | 27 | `DESIGN` | `P1` | [ ] | 2026-08-28 / 2026-09-02 |
| 2026-09-01 | [Number of Islands](https://leetcode.com/problems/number-of-islands/) | 28 | `BOUNDARY` | `P0` | [ ] | 2026-09-03 / 2026-09-08 |
| 2026-09-02 | [Course Schedule](https://leetcode.com/problems/course-schedule/) | 29 | `DS` | `P1` | [ ] | 2026-09-04 / 2026-09-09 |
