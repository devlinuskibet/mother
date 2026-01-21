import React from 'react';
import VitalCard from '../components/dashboard/VitalCard';
import RiskStatusCard from '../components/dashboard/RiskStatusCard';

const MotherDashboard = () => {
    return (
        <div className="mother-dashboard">
            <h1>Dashboard</h1>
            <RiskStatusCard riskLevel="low" />
            <div className="vitals-grid">
                <VitalCard label="Heart Rate" value="75" unit="bpm" />
                <VitalCard label="Blood Pressure" value="120/80" unit="mmHg" />
            </div>
        </div>
    );
};

export default MotherDashboard;
