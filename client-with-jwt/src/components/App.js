import React, { useEffect, useState } from "react";
import NavBar from "./NavBar";
import Login from "../pages/Login";

function App() {
  const [user, setUser] = useState(null);
  const [notes, setNotes] = useState([]);

  // 🔐 Auto-login using stored token
  useEffect(() => {
    const token = localStorage.getItem("token");

    if (token && token !== "undefined") {
      fetch("/me", {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      }).then((r) => {
        if (r.ok) {
          r.json().then((user) => setUser(user));
        } else {
          localStorage.removeItem("token");
        }
      });
    }
  }, []);

  // 🔑 After login/signup
  const onLogin = (token, user) => {
    console.log("STORING TOKEN:", token); // debug
    localStorage.setItem("token", token);
    setUser(user);
  };

  // 🔥 Fetch notes (used by "Do Something")
  const handleFetchNotes = () => {
    fetch("/notes", {
      headers: {
        Authorization: `Bearer ${localStorage.getItem("token")}`,
      },
    })
      .then((r) => r.json())
      .then((data) => {
        setNotes(data.data || data);
      });
  };

  if (!user) return <Login onLogin={onLogin} />;

  return (
    <>
      <NavBar setUser={setUser} onDoSomething={handleFetchNotes} />

      <main style={{ padding: "20px" }}>
        <p>You are logged in!</p>

        {notes.length === 0 ? (
          <p>No notes yet. Click "Do Something".</p>
        ) : (
          notes.map((note) => (
            <div key={note.id}>
              <h3>{note.title}</h3>
              <p>{note.content}</p>
              <hr />
            </div>
          ))
        )}
      </main>
    </>
  );
}

export default App;