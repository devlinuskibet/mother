import React from 'react';

const VitalCard = ({ label, value, unit }) => {
    return (
        <div className="vital-card">
            <h4>{label}</h4>
            <p>{value} {unit}</p>
        </div>
    );
};

export default VitalCard;
