# 윈도우 함수(Window Function)

## 1. 윈도우 함수란?

**기존 행을 유지하면서 각 행에 계산 결과를 추가하는 함수**

`GROUP BY`처럼 여러 행을 하나로 합치지 않고, **각 행에 계산된 값을 추가**할 수 있다.

대표적인 윈도우 함수:

* `RANK()`
* `DENSE_RANK()`
* `ROW_NUMBER()`
* `SUM()`
* `AVG()`
* `COUNT()`
* `MAX()`
* `MIN()`

---

## 2. 기본 문법

```sql
함수() OVER (
    ORDER BY 정렬할_컬럼
)
```

예를 들어 점수가 높은 순서대로 순위를 매기려면:

```sql
RANK() OVER (ORDER BY SCORE DESC)
```

→ **SCORE가 높은 순으로 각 행에 순위를 부여**

---

## 3. `ORDER BY`와 윈도우 함수의 `ORDER BY` 차이

일반적인 `ORDER BY`:

```sql
SELECT *
FROM EMPLOYEE
ORDER BY SCORE DESC;
```

→ **조회 결과 자체의 순서를 변경**

반면 윈도우 함수의 `ORDER BY`:

```sql
SELECT
    EMP_NAME,
    SCORE,
    RANK() OVER (ORDER BY SCORE DESC) AS RK
FROM EMPLOYEE;
```

→ 결과의 행은 유지하면서 **각 행에 순위 값을 추가**

예를 들어:

| EMP_NAME | SCORE | RK |
| -------- | ----: | -: |
| A        |   100 |  1 |
| B        |    90 |  2 |
| C        |    90 |  2 |
| D        |    80 |  4 |

---

# 4. GROUP BY와 윈도우 함수의 차이

### GROUP BY

```sql
SELECT DEPT_ID, AVG(SAL)
FROM EMPLOYEE
GROUP BY DEPT_ID;
```

여러 행을 그룹으로 묶어 **하나의 행으로 집계**한다.

```text
D001 → 5000
D002 → 4500
D003 → 5200
```

### 윈도우 함수

```sql
SELECT
    EMP_NAME,
    SAL,
    AVG(SAL) OVER () AS AVG_SAL
FROM EMPLOYEE;
```

기존 행을 유지하면서 **계산 결과를 각 행에 추가**한다.

```text
김철수  5000  4500
이영희  4500  4500
박민수  4000  4500
```

### 핵심

> **GROUP BY → 행을 합친다.**
> **윈도우 함수 → 행을 유지한다.**

---

# 5. RANK()

순위를 매기는 윈도우 함수

```sql
RANK() OVER (ORDER BY SCORE DESC)
```

점수가:

```text
100
90
90
80
```

이라면:

| SCORE | RANK |
| ----: | ---: |
|   100 |    1 |
|    90 |    2 |
|    90 |    2 |
|    80 |    4 |

**동점자는 같은 순위**를 부여하고, 그다음 순위는 건너뛴다.

> `1 → 2 → 2 → 4`

---

# 6. DENSE_RANK()

`RANK()`와 비슷하지만 **동점 이후 순위를 건너뛰지 않는다.**

```sql
DENSE_RANK() OVER (ORDER BY SCORE DESC)
```

| SCORE | DENSE_RANK |
| ----: | ---------: |
|   100 |          1 |
|    90 |          2 |
|    90 |          2 |
|    80 |          3 |

> `1 → 2 → 2 → 3`

---

# 7. ROW_NUMBER()

각 행에 **고유한 순번**을 부여한다.

```sql
ROW_NUMBER() OVER (ORDER BY SCORE DESC)
```

| SCORE | ROW_NUMBER |
| ----: | ---------: |
|   100 |          1 |
|    90 |          2 |
|    90 |          3 |
|    80 |          4 |

동점이어도 같은 순위를 부여하지 않는다.

> `1 → 2 → 3 → 4`

---

## 8. 세 함수 비교

점수가 다음과 같을 때:

```text
100
90
90
80
```

| 함수             | 결과           | 특징           |
| -------------- | ------------ | ------------ |
| `RANK()`       | `1, 2, 2, 4` | 동점 이후 순위 건너뜀 |
| `DENSE_RANK()` | `1, 2, 2, 3` | 동점 이후 순위 유지  |
| `ROW_NUMBER()` | `1, 2, 3, 4` | 모든 행에 고유 번호  |

### 기억하기

```text
RANK        → 공동 순위 + 순위 건너뜀
DENSE_RANK  → 공동 순위 + 순위 안 건너뜀
ROW_NUMBER  → 무조건 각각 다른 번호
```

---

# 9. PARTITION BY

윈도우 함수에서 **그룹을 나누는 역할**

```sql
RANK() OVER (
    PARTITION BY DEPT_ID
    ORDER BY SCORE DESC
)
```

전체 직원의 순위를 매기는 것이 아니라 **부서별로 순위를 매긴다.**

예를 들어:

| DEPT_ID | NAME | SCORE | RANK |
| ------- | ---- | ----: | ---: |
| D001    | 김철수  |   100 |    1 |
| D001    | 이영희  |    90 |    2 |
| D002    | 박민수  |   100 |    1 |
| D002    | 최수진  |    80 |    2 |

`PARTITION BY DEPT_ID` 때문에 각 부서에서 **다시 1등부터 시작**한다.

### 해석하는 방법

```sql
RANK() OVER (
    PARTITION BY DEPT_ID
    ORDER BY SCORE DESC
)
```

> **DEPT_ID별로 나눈 다음 → SCORE 높은 순으로 → 순위를 매긴다.**

---

# 10. PARTITION BY와 GROUP BY의 차이

둘 다 그룹을 나눈다는 점 때문에 헷갈릴 수 있다.

### GROUP BY

```sql
SELECT DEPT_ID, AVG(SCORE)
FROM EMPLOYEE
GROUP BY DEPT_ID;
```

→ 부서별로 **행을 묶어서 집계**

### PARTITION BY

```sql
SELECT
    EMP_NAME,
    DEPT_ID,
    SCORE,
    AVG(SCORE) OVER (PARTITION BY DEPT_ID) AS DEPT_AVG
FROM EMPLOYEE;
```

→ 부서별로 계산하지만 **기존 행은 유지**

즉,

> `GROUP BY` → 그룹으로 묶어서 행을 줄임
> `PARTITION BY` → 그룹을 나누어서 계산하지만 행은 유지

---

# 11. 실전 예제

### 부서별 급여 순위

```sql
SELECT
    EMP_NAME,
    DEPT_ID,
    SAL,
    RANK() OVER (
        PARTITION BY DEPT_ID
        ORDER BY SAL DESC
    ) AS RK
FROM EMPLOYEE;
```

해석:

1. `DEPT_ID`별로 그룹을 나눈다.
2. 각 그룹에서 `SAL`을 높은 순으로 정렬한다.
3. `RANK()`로 순위를 매긴다.
4. 원래 직원 데이터는 그대로 유지한다.

---

# 12. 이번 문제에 적용

2022년 평가 점수의 상반기 + 하반기 합계를 구하고, 가장 높은 사원을 찾는 문제.

```sql
RANK() OVER (
    ORDER BY SUM(G.SCORE) DESC
) AS RK
```

먼저:

```sql
SUM(G.SCORE)
```

→ 사원별 2022년 평가 점수 합계

그다음:

```sql
RANK() OVER (
    ORDER BY SUM(G.SCORE) DESC
)
```

→ 합산 점수가 높은 순으로 순위 부여

마지막으로:

```sql
WHERE RK = 1
```

→ 가장 높은 점수를 받은 사원만 조회

### 전체 흐름

```text
2022년 데이터 필터링
        ↓
사원별 GROUP BY
        ↓
상·하반기 점수 SUM
        ↓
RANK()로 순위 부여
        ↓
RK = 1인 사원 조회
```

---

# ⭐ 핵심 정리

```sql
RANK() OVER (ORDER BY SCORE DESC)
```

를 보면

> **"SCORE 높은 순으로 각 행에 순위를 붙여줘."**

라고 이해하면 된다.

그리고

```sql
RANK() OVER (
    PARTITION BY DEPT_ID
    ORDER BY SCORE DESC
)
```

는

> **"DEPT_ID별로 나눈 다음, 각 부서 안에서 SCORE 높은 순으로 순위를 붙여줘."**

### 윈도우 함수 핵심 구조

```sql
함수() OVER (
    PARTITION BY 그룹을_나눌_컬럼
    ORDER BY 순위를_정할_컬럼
)
```

`PARTITION BY`는 **필요할 때만 사용**하면 된다.

> **윈도우 함수 = 행을 유지한 채, 행별 계산 결과를 추가하는 것**
