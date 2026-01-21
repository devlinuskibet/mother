import React from 'react';
import styled from 'styled-components';

const StyledButton = styled.button`
  padding: 10px 20px;
  background-color: var(--primary-color);
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  
  &:hover {
    opacity: 0.9;
  }
`;

const Button = ({ children, onClick, type = 'button' }) => {
    return (
        <StyledButton type={type} onClick={onClick}>
            {children}
        </StyledButton>
    );
};

export default Button;
