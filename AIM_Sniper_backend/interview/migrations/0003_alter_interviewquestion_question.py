# Generated by Django 5.1.1 on 2024-10-04 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interview', '0002_alter_interviewquestion_question'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interviewquestion',
            name='question',
            field=models.CharField(max_length=255),
        ),
    ]
