import React, { useState } from 'react';
import Input from '../components/common/Input';
import Button from '../components/common/Button';

const Register = () => {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');

    const handleRegister = (e) => {
        e.preventDefault();
        // Register logic
    };

    return (
        <div className="register-page">
            <h2>Register</h2>
            <form onSubmit={handleRegister}>
                <Input label="Email" value={email} onChange={(e) => setEmail(e.target.value)} />
                <Input label="Password" type="password" value={password} onChange={(e) => setPassword(e.target.value)} />
                <Button type="submit">Register</Button>
            </form>
        </div>
    );
};

export default Register;
