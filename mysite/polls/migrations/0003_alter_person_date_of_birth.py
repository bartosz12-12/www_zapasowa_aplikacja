# Generated by Django 4.1.12 on 2023-10-25 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_question_choice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='date_of_birth',
            field=models.DateTimeField(auto_created=True, auto_now=True),
        ),
    ]
