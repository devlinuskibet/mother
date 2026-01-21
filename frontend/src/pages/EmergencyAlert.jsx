import React from 'react';
import Button from '../components/common/Button';

const EmergencyAlert = () => {
    const handleEmergency = () => {
        alert('Emergency Alert Sent!');
    };

    return (
        <div className="emergency-alert">
            <h1>EMERGENCY</h1>
            <Button onClick={handleEmergency}>SOS</Button>
        </div>
    );
};

export default EmergencyAlert;
