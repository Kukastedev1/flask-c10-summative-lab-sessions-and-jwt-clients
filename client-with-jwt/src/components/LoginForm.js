import React, { useState } from "react";
import { Button, Error, Input, FormField, Label } from "../styles";

function LoginForm({ onLogin }) {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [errors, setErrors] = useState([]);
  const [isLoading, setIsLoading] = useState(false);

  function handleSubmit(e) {
    e.preventDefault();
    setIsLoading(true);
    setErrors([]);

    fetch("/login", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ username, password }),
    })
      .then((r) => {
        setIsLoading(false);

        if (r.ok) {
          r.json().then((data) => {
            console.log("LOGIN RESPONSE:", data); // debug

            if (data.access_token) {
              onLogin(data.access_token, data.user); // FIXED
            } else {
              setErrors(["Login failed: No token returned"]);
            }
          });
        } else {
          r.json().then((err) => {
            setErrors(err.errors || ["Login failed"]);
          });
        }
      })
      .catch(() => {
        setIsLoading(false);
        setErrors(["Network error"]);
      });
  }

  return (
    <form onSubmit={handleSubmit}>
      <FormField>
        <Label htmlFor="username">Username</Label>
        <Input
          type="text"
          id="username"
          autoComplete="off"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
        />
      </FormField>

      <FormField>
        <Label htmlFor="password">Password</Label>
        <Input
          type="password"
          id="password"
          autoComplete="current-password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />
      </FormField>

      <FormField>
        <Button type="submit">
          {isLoading ? "Loading..." : "Login"}
        </Button>
      </FormField>

      <FormField>
        {errors.map((err, index) => (
          <Error key={index}>{err}</Error>
        ))}
      </FormField>
    </form>
  );
}

export default LoginForm;