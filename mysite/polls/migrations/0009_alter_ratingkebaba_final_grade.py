# Generated by Django 4.1.12 on 2023-11-24 21:02

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0008_ratingkebaba_final_grade_ratingzapiekanka'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ratingkebaba',
            name='final_grade',
            field=models.FloatField(default=0.0, editable=False, help_text='Ostateczna ocena', validators=[django.core.validators.validate_integer]),
        ),
    ]
