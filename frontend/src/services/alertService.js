import { post } from './api';

export const sendAlert = (data) => post('/alerts', data);
