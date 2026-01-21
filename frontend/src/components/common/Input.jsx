import React from 'react';
import styled from 'styled-components';

const Wrapper = styled.div`
  margin-bottom: 15px;
`;

const StyledInput = styled.input`
  width: 100%;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 5px;
`;

const Label = styled.label`
  display: block;
  margin-bottom: 5px;
`;

const Input = ({ label, type = 'text', value, onChange, placeholder }) => {
  return (
    <Wrapper>
      {label && <Label>{label}</Label>}
      <StyledInput
        type={type}
        value={value}
        onChange={onChange}
        placeholder={placeholder}
      />
    </Wrapper>
  );
};

export default Input;
