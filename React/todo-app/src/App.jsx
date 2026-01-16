import { useState } from 'react'
import './App.css'

function App() {
  const [todos, setTodos] = useState([])
  const [inputValue, setInputValue] = useState('')

  const addTodo = () => {
    if (inputValue.trim() === '') return
    const newTodo = {
      id: Date.now(),
      text: inputValue,
      completed: false
    }
    setTodos([newTodo, ...todos])
    setInputValue('')
  }

  const toggleTodo = (id) => {
    setTodos(todos.map(todo =>
      todo.id === id ? { ...todo, completed: !todo.completed } : todo
    ))
  }

  const deleteTodo = (id) => {
    setTodos(todos.filter(todo => todo.id !== id))
  }

  const handleKeyDown = (e) => {
    if (e.key === 'Enter') addTodo()
  }

  return (
    <div className="app">
      <div className="container">
        <h1>Todo List</h1>
        <p className="subtitle">일정을 체계적으로 관리하세요</p>

        <div className="input-section">
          <input
            type="text"
            placeholder="새로운 할 일을 입력하세요..."
            value={inputValue}
            onChange={(e) => setInputValue(e.target.value)}
            onKeyDown={handleKeyDown}
          />
          <button className="add-btn" onClick={addTodo}>추가</button>
        </div>

        <ul className="todo-list">
          {todos.map(todo => (
            <li key={todo.id} className={todo.completed ? 'completed' : ''}>
              <label className="todo-checkbox">
                <input
                  type="checkbox"
                  checked={todo.completed}
                  onChange={() => toggleTodo(todo.id)}
                />
                <span className="todo-text">{todo.text}</span>
              </label>
              <button
                className="delete-btn"
                onClick={() => deleteTodo(todo.id)}
              >
                🗑
              </button>
            </li>
          ))}
        </ul>
      </div>
    </div>
  )
}

export default App
