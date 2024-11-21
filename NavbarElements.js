import styled from 'styled-components';
import { Link } from 'react-router-dom';

/* Styling options for the Navigation bar */
export const Nav = styled.nav`
  background: #282c34;
  padding: 1rem;
  display: flex;
  justify-content: center;
`;

export const NavLink = styled(Link)`
  color: white;
  margin: 0 1rem;
  text-decoration: none;
  font-size: 1.2rem;

  &:hover {
    color: #61dafb;
  }
`;

export const NavMenu = styled.div`
  display: flex;
  align-items: center;
`;