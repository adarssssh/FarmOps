

# Create your views here.
# soil_analysis/views.py

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import SoilTest, SoilImprovementRecommendation
from .recommendation import generate_recommendation

def input_soil_test(request):
    if request.method == 'POST':
        ph = request.POST['ph']
        nitrogen = request.POST['nitrogen']
        phosphorus = request.POST['phosphorus']
        potassium = request.POST['potassium']
        organic_matter = request.POST['organic_matter']
        soil_type = request.POST['soil_type']

        soil_test = SoilTest.objects.create(
            ph=ph,
            nitrogen=nitrogen,
            phosphorus=phosphorus,
            potassium=potassium,
            organic_matter=organic_matter,
            soil_type=soil_type,
        )
        
        generate_recommendation(soil_test)
        
        return HttpResponse(f'Soil Test {soil_test.id} saved and recommendation generated!')
    return render(request, 'input_soil_test.html')

def view_recommendation(request, test_id):
    soil_test = get_object_or_404(SoilTest, id=test_id)
    recommendation = get_object_or_404(SoilImprovementRecommendation, soil_test=soil_test)
    
    return render(request, 'view_recommendation.html', {'soil_test': soil_test, 'recommendation': recommendation})
