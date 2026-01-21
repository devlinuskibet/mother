class AlertService:
    def check_alert(self, health_data):
        alerts = []
        if health_data.get("systolic_bp", 0) > 140:
            alerts.append("High Blood Pressure detected")
        if health_data.get("glucose_level", 0) > 140:
            alerts.append("High Glucose level detected")
        return alerts

alert_service = AlertService()
