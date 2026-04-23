import React from "react";
import { Link } from "react-router-dom";
import styled from "styled-components";
import { Button } from "../styles";

function NavBar({ setUser, onDoSomething }) {
  function handleLogoutClick() {
    localStorage.removeItem("token");
    setUser(null);
  }

  function handleDoSomethingClick() {
    if (onDoSomething) {
      onDoSomething();
    } else {
      console.warn("onDoSomething not provided");
    }
  }

  return (
    <Wrapper>
      <Logo>
        <Link to="/">My App</Link>
      </Logo>

      <Nav>
        <Button onClick={handleDoSomethingClick}>
          Do Something
        </Button>

        <Button variant="outline" onClick={handleLogoutClick}>
          Logout
        </Button>
      </Nav>
    </Wrapper>
  );
}

const Wrapper = styled.header`
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 8px;
  position: relative;
`;

const Logo = styled.h1`
  font-family: "Permanent Marker", cursive;
  font-size: 3rem;
  color: deeppink;
  margin: 0;
  line-height: 1;

  a {
    color: inherit;
    text-decoration: none;
  }
`;

const Nav = styled.nav`
  display: flex;
  gap: 8px;
  position: absolute;
  right: 12px;
`;

export default NavBar;