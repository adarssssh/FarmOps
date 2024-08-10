from django.db import models

# Create your models here.
class SoilTest(models.Model):
    PH_LEVEL_CHOICES = [(i, f'{i}') for i in range(1, 15)]
    
    ph = models.DecimalField(max_digits=4, decimal_places=2)
    nitrogen = models.DecimalField(max_digits=6, decimal_places=2)
    phosphorus = models.DecimalField(max_digits=6, decimal_places=2)
    potassium = models.DecimalField(max_digits=6, decimal_places=2)
    organic_matter = models.DecimalField(max_digits=6, decimal_places=2)
    soil_type = models.CharField(max_length=100)
    date_tested = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f"Soil Test {self.id} - {self.date_tested}"

class SoilImprovementRecommendation(models.Model):
    soil_test = models.OneToOneField(SoilTest, on_delete=models.CASCADE)
    lime_required = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    nitrogen_needed = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    phosphorus_needed = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    potassium_needed = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    organic_matter_suggestion = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Recommendation for Soil Test {self.soil_test.id}"