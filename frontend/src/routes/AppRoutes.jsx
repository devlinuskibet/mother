import React from 'react';
import { Routes, Route } from 'react-router-dom';
import Login from '../pages/Login';
import MotherDashboard from '../pages/MotherDashboard';

const AppRoutes = () => {
    return (
        <Routes>
            <Route path="/login" element={<Login />} />
            <Route path="/dashboard" element={<MotherDashboard />} />
        </Routes>
    );
};

export default AppRoutes;
