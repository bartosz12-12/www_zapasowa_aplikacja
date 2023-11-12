# Generated by Django 4.1.12 on 2023-11-02 10:00

from django.db import migrations, models
import polls.models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_ratingkebaba_delete_ocenakebaba'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ratingkebaba',
            name='additions',
            field=models.IntegerField(default=0, help_text='Ocena dodatkow w skali od 1 do 10', validators=[polls.models.validate_rating]),
        ),
        migrations.AlterField(
            model_name='ratingkebaba',
            name='meat',
            field=models.IntegerField(default=0, help_text='Ocena miesa w skali od 1 do 10', validators=[polls.models.validate_rating]),
        ),
        migrations.AlterField(
            model_name='ratingkebaba',
            name='sauce',
            field=models.IntegerField(default=0, help_text='Ocena sosu w skali od 1 do 10', validators=[polls.models.validate_rating]),
        ),
        migrations.AlterField(
            model_name='ratingkebaba',
            name='vegetables',
            field=models.IntegerField(default=0, help_text='Ocena warzyw w skali od 1 do 10', validators=[polls.models.validate_rating]),
        ),
    ]