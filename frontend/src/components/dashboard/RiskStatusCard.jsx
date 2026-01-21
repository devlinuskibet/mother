import React from 'react';

const RiskStatusCard = ({ riskLevel }) => {
    const getColor = () => {
        switch (riskLevel) {
            case 'high': return 'red';
            case 'medium': return 'orange';
            default: return 'green';
        }
    };

    return (
        <div style={{ border: `1px solid ${getColor()}`, padding: '20px' }}>
            <h3>Risk Status</h3>
            <p>{riskLevel.toUpperCase()}</p>
        </div>
    );
};

export default RiskStatusCard;
