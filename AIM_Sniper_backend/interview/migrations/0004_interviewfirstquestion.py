# Generated by Django 5.1.1 on 2024-10-31 07:36

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("interview", "0003_alter_interviewquestion_question"),
    ]

    operations = [
        migrations.CreateModel(
            name="InterviewFirstQuestion",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("question", models.CharField(max_length=255)),
            ],
            options={
                "db_table": "interview_first_question",
            },
        ),
    ]