import React from 'react';

const AlertBanner = ({ message, type }) => {
    return (
        <div className={`alert-banner alert-${type}`}>
            {message}
        </div>
    );
};

export default AlertBanner;
