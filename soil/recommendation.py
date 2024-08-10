# soil_analysis/recommendations.py

from .models import SoilImprovementRecommendation

def generate_recommendation(soil_test):
    lime_required = None
    nitrogen_needed = None
    phosphorus_needed = None
    potassium_needed = None
    organic_matter_suggestion = None

    # Example logic for pH adjustment
    if float(soil_test.ph) < 6.0:
        lime_required = (6.5 - float(soil_test.ph)) * 1.5  # Simplified formula
    
    # Logic for nitrogen recommendation
    if float(soil_test.nitrogen) < 10:
        nitrogen_needed = 50 - float(soil_test.nitrogen ) # Example logic
    
    # Logic for phosphorus recommendation
    if float(soil_test.phosphorus) < 30:
        phosphorus_needed = 30 - float(soil_test.phosphorus)
    
    # Logic for potassium recommendation
    if float(soil_test.potassium) < 100:
        potassium_needed = 100 - float(soil_test.potassium)

    # Logic for organic matter suggestion
    if float(soil_test.organic_matter) < 2:
        organic_matter_suggestion = "Add compost or organic fertilizers to improve soil organic matter."

    # Save the recommendation
    recommendation = SoilImprovementRecommendation.objects.create(
        soil_test=soil_test,
        lime_required=lime_required,
        nitrogen_needed=nitrogen_needed,
        phosphorus_needed=phosphorus_needed,
        potassium_needed=potassium_needed,
        organic_matter_suggestion=organic_matter_suggestion
    )

    return recommendation
