import React from 'react';
import { Link } from 'react-router-dom';
import Button from '../components/common/Button';

const Welcome = () => {
    return (
        <div className="welcome-page">
            <h1>Welcome to MamaCare</h1>
            <Link to="/login"><Button>Login</Button></Link>
            <Link to="/register"><Button>Register</Button></Link>
        </div>
    );
};

export default Welcome;
