# Flask Authentication and JWT Client Lab

## Overview

This project demonstrates a full-stack authentication system using a Flask backend and a React frontend. It implements user authentication with JSON Web Tokens (JWT) and protected routes, allowing users to securely sign up, log in, and access restricted resources.

The frontend communicates with the backend using relative URLs and stores authentication tokens in localStorage.

---

## Features

* User sign up
* User login
* JWT-based authentication
* Persistent login using stored token
* Protected backend routes
* Logout functionality
* Fetching protected resources (`/notes`)
* Separation of frontend and backend

---

## Tech Stack

### Backend

* Flask
* Flask-JWT-Extended
* Flask-SQLAlchemy
* SQLite

### Frontend

* React
* Styled Components
* Fetch API

---

## Project Structure

```id="structure"
flask-c10-summative-lab-sessions-and-jwt-clients/
│
├── server/                # Flask backend
│   ├── app.py
│   ├── models.py
│   ├── routes/
│   │   ├── auth_routes.py
│   │   └── resource_routes.py
│   └── extensions.py
│
├── client-with-jwt/       # React frontend
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   └── App.js
│   └── package.json
│
└── README.md
```

---

## Setup Instructions

### Backend Setup

```bash id="backend"
cd server
pipenv install
pipenv shell
python app.py
```

Backend runs on:

```id="backend_url"
http://localhost:5555
```

---

### Frontend Setup

```bash id="frontend"
cd client-with-jwt
npm install
npm start
```

Frontend runs on:

```id="frontend_url"
http://localhost:4000
```

---

## Authentication Flow

1. User signs up or logs in
2. Backend returns a JWT:

```json id="jwt"
{
  "access_token": "your_token_here"
}
```

3. Token is stored in localStorage
4. Token is sent in headers for protected routes:

```js id="auth_header"
Authorization: Bearer <token>
```

---

## Protected Routes

### GET /me

Returns the currently logged-in user

### GET /notes

Returns notes belonging to the logged-in user

---

## Testing the Application

### Login

* Enter username and password
* Token is stored in localStorage
* User is redirected to the home page

### Sign Up

* Create a new account
* User is automatically logged in
* Token is stored

### Session Persistence

* Refreshing the page keeps the user logged in
* The `/me` endpoint verifies the token

### Protected Requests

* Clicking "Do Something" triggers a request to:

  ```
  GET /notes
  ```
* This only works when a valid token is present

### Logout

* Removes token from localStorage
* Returns user to login page

---

## Common Issues and Fixes

### Token shows undefined

Ensure the frontend reads `access_token` instead of `token`

### "Not enough segments"

Occurs when the token is invalid
Fix by clearing localStorage and logging in again

### "Subject must be a string"

Ensure the backend sets identity as a string:

```python id="identity"
identity=str(user.id)
```

---

## Demo Video

The recorded demonstration shows:

* User signup
* User login
* Token storage in the browser
* Accessing protected routes
* Logout functionality

---

## Key Concepts Learned

* JWT authentication
* Client-server communication
* Protected routes in Flask
* React state management
* Handling authentication tokens

---

## Author

Engine Kukaste

---

## Submission Notes

* Fully functional authentication system
* Frontend connected to backend using proxy
* Demonstrates secure session handling using JWT
