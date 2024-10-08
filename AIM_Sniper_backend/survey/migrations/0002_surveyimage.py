# Generated by Django 5.1.1 on 2024-10-07 06:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SurveyImage',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('image', models.CharField(max_length=50)),
                ('question_id', models.OneToOneField(db_column='question_id', on_delete=django.db.models.deletion.CASCADE, to='survey.surveyquestion')),
            ],
            options={
                'db_table': 'survey_image',
            },
        ),
    ]
