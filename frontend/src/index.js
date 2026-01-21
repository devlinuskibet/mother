import React from 'react';
import ReactDOM from 'react-dom/client';
import './styles/global.css';
import App from './App';
import { AuthProvider } from './contexts/AuthContext';
import { UserProvider } from './contexts/UserContext';
import { AlertProvider } from './contexts/AlertContext';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
    <React.StrictMode>
        <AuthProvider>
            <UserProvider>
                <AlertProvider>
                    <App />
                </AlertProvider>
            </UserProvider>
        </AuthProvider>
    </React.StrictMode>
);
