try:
    import numpy as np
except ImportError:
    np = None

class AnalyticsService:
    def analyze_trend(self, data_points):
        # Placeholder linear regression
        if len(data_points) < 2:
            return {"trend": "stable", "slope": 0.0}
        
        x = np.arange(len(data_points))
        y = np.array(data_points)
        slope, _ = np.polyfit(x, y, 1)
        
        trend = "stable"
        if slope > 0.1:
            trend = "increasing"
        elif slope < -0.1:
            trend = "decreasing"
            
        return {"trend": trend, "slope": slope}

analytics_service = AnalyticsService()
