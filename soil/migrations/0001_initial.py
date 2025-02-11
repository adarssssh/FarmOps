# Generated by Django 4.2.15 on 2024-08-10 09:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="SoilTest",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("ph", models.DecimalField(decimal_places=2, max_digits=4)),
                ("nitrogen", models.DecimalField(decimal_places=2, max_digits=6)),
                ("phosphorus", models.DecimalField(decimal_places=2, max_digits=6)),
                ("potassium", models.DecimalField(decimal_places=2, max_digits=6)),
                ("organic_matter", models.DecimalField(decimal_places=2, max_digits=6)),
                ("soil_type", models.CharField(max_length=100)),
                ("date_tested", models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="SoilImprovementRecommendation",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "lime_required",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=6, null=True
                    ),
                ),
                (
                    "nitrogen_needed",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=6, null=True
                    ),
                ),
                (
                    "phosphorus_needed",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=6, null=True
                    ),
                ),
                (
                    "potassium_needed",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=6, null=True
                    ),
                ),
                ("organic_matter_suggestion", models.TextField(blank=True, null=True)),
                (
                    "soil_test",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE, to="soil.soiltest"
                    ),
                ),
            ],
        ),
    ]
