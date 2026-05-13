import React, { useEffect, useState } from "react";
import { createRoot } from "react-dom/client";
import "./style.css";

const API_URL = import.meta.env.VITE_API_URL || "http://localhost:5000";

function App() {
  const [tasks, setTasks] = useState([]);
  const [title, setTitle] = useState("");
  const [error, setError] = useState("");

  async function loadTasks() {
    try {
      const response = await fetch(`${API_URL}/api/data`);
      const data = await response.json();
      setTasks(data);
      setError("");
    } catch (err) {
      setError("Не удалось загрузить данные. Проверь VITE_API_URL и backend.");
    }
  }

  async function addTask(event) {
    event.preventDefault();
    if (!title.trim()) return;

    await fetch(`${API_URL}/api/data`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ title })
    });

    setTitle("");
    loadTasks();
  }

  async function deleteTask(id) {
    await fetch(`${API_URL}/api/data/${id}`, { method: "DELETE" });
    loadTasks();
  }

  useEffect(() => {
    loadTasks();
  }, []);

  return (
    <main className="container">
      <section className="card">
        <h1>DevOps CI/CD Lab</h1>
        <p className="student">Student: YOUR_NAME | ID: YOUR_ID</p>
        <p className="api">Backend API: {API_URL}</p>

        <form onSubmit={addTask} className="form">
          <input
            value={title}
            onChange={(e) => setTitle(e.target.value)}
            placeholder="Введите задачу"
          />
          <button type="submit">Добавить</button>
        </form>

        {error && <p className="error">{error}</p>}

        <ul className="list">
          {tasks.map((task) => (
            <li key={task.id}>
              <span>{task.title}</span>
              <button onClick={() => deleteTask(task.id)}>Удалить</button>
            </li>
          ))}
        </ul>

        {tasks.length === 0 && <p className="empty">Пока записей нет</p>}
      </section>
    </main>
  );
}

createRoot(document.getElementById("root")).render(<App />);
