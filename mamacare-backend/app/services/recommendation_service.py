class RecommendationService:
    def get_recommendations(self, risk_level):
        if risk_level == "high":
            return ["Consult a doctor immediately", "Monitor BP every 4 hours"]
        else:
            return ["Maintain healthy diet", "Daily light exercise"]

recommendation_service = RecommendationService()
