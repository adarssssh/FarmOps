from django.core.management.base import BaseCommand
import csv
from soil.models import SoilTest

class Command(BaseCommand):
    help = 'Load soil test data from a CSV file'

    def handle(self, *args, **kwargs):
        # Path to the CSV file
        csv_file_path = 'D:\Projects\FarmOps\Farmops\soil_test_data_large.csv'

        with open(csv_file_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                SoilTest.objects.create(
                    ph=row['ph'],
                    nitrogen=row['nitrogen'],
                    phosphorus=row['phosphorus'],
                    potassium=row['potassium'],
                    organic_matter=row['organic_matter'],
                    soil_type=row['soil_type']
                )
        self.stdout.write(self.style.SUCCESS('Successfully loaded soil test data'))
