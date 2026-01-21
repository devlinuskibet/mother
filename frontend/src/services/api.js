const API_URL = 'http://localhost:5000/api';

export const get = async (endpoint) => {
    const res = await fetch(`${API_URL}${endpoint}`);
    return res.json();
};

export const post = async (endpoint, data) => {
    const res = await fetch(`${API_URL}${endpoint}`, {
        method: 'POST',
        body: JSON.stringify(data),
        headers: { 'Content-Type': 'application/json' },
    });
    return res.json();
};
