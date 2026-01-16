# React

### React 기초 익히기

[React 기초 2시간 무료 강의 - 웹 인터페이스 개발 실습까지 | "유퀴즈 출연/코로나맵 2천만 유저" 이동훈 개발자](https://www.youtube.com/watch?v=P2cEUrtl75k)

### React

- 사용자 인터페이스를 구축하기 위한 JS 패키지
- Facebook에서 개발, 2013년 오픈소스 공개
- 선언적 프로그래밍 패러다임
- 단방향 데이터흐름으로 예측가능한 상태관리

### 컴포넌트 기반의 아키텍처

- 재사용 가능한 독립적인 UI 조각들
- 코드 재사용성, 유지 보수성 높임
- 관심사 분리를 통한 개발 효율성 증대

### 함수형 컴포넌트

```jsx
function Welcome(props) {
	return <h1>Hellow, {prpos.name}!</h1>;
}

const Welcome = (props) => P
	return <h1>Hello, {prpos.name}!</h1>;
};
```

### JSX (javaScript XML)

```jsx
function Welcome(props) {
  return <h1>Hello, {props.name}!</h1>;
}

function Welcome(props) {
  return React.createElement('h1', null, `Hello, ${props.name}!`);
}
```

### Props (Properties)

```jsx
function Welcome(props) {
  return <h1>Hello, {props.name}!</h1>;
}

function App() {
  return <Welcome name="동훈" />;
}
```

### State (상태)

- 컴포넌트의 내부 데이터
- useState Hook을 사용하여 관리

```jsx
const [value, setValue] = useState(initialValue);

· value: 현재 상태 값  
· setValue: 상태를 바꾸는 함수  
· initialValue: 초기값  

useState는 React 함수형 컴포넌트에서 상태를 쓸 수 있게 해주는 훅(Hook)입니다.
```

```jsx
import React, { useState } from 'react';

function Counter() {
  const [count, setCount] = useState(0);

  return (
    <div>
      <p>You clicked {count} times</p>
      <button onClick={() => setCount(count + 1)}>
        Click me
      </button>
    </div>
  );
}
```

### props vs state 차이

| 항목 | props | state |
| --- | --- | --- |
| 정의 | 부모 컴포넌트에서 자식 컴포넌트로 전달되는 데이터 | 컴포넌트 내부에서 관리되는 데이터 |
| 변경 여부 | 자식이 직접 변경할 수 없음 (읽기 전용) | setState()를 통해 변경 가능 |
| 역할 | 외부에서 주어진 값 | 내부에서 변하는 값 |
| 사용 목적 | 컴포넌트 재사용, 외부 데이터 전달 | 사용자 입력 처리, 인터랙션 처리 등 |

### Vite

- Vue 창시자가 만든 빌드 도구
- CRA보다 빠른 속도 제공 