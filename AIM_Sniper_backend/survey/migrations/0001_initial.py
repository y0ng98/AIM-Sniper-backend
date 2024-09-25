# Generated by Django 5.1.1 on 2024-09-25 01:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("account", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Survey",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("survey", models.CharField(max_length=128)),
            ],
            options={
                "db_table": "survey",
            },
        ),
        migrations.CreateModel(
            name="SurveyDescription",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("description", models.CharField(max_length=255)),
                (
                    "survey_id",
                    models.OneToOneField(
                        db_column="survey_id",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="survey.survey",
                    ),
                ),
            ],
            options={
                "db_table": "survey_description",
            },
        ),
        migrations.CreateModel(
            name="SurveyQuestion",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("question", models.CharField(max_length=128)),
                ("question_type", models.CharField(max_length=10)),
                ("essential", models.BooleanField()),
                (
                    "survey_id",
                    models.ForeignKey(
                        db_column="survey_id",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="survey.survey",
                    ),
                ),
            ],
            options={
                "db_table": "survey_question",
            },
        ),
        migrations.CreateModel(
            name="SurveySelection",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("selection", models.CharField(max_length=50)),
                (
                    "survey_question_id",
                    models.ForeignKey(
                        db_column="survey_question_id",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="survey.surveyquestion",
                    ),
                ),
            ],
            options={
                "db_table": "survey_selection",
            },
        ),
        migrations.CreateModel(
            name="SurveyAnswer",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("answer", models.CharField(max_length=128, null=True)),
                (
                    "account",
                    models.ForeignKey(
                        db_column="account_id",
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="account.account",
                    ),
                ),
                (
                    "survey_question_id",
                    models.ForeignKey(
                        db_column="survey_question_id",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="survey.surveyquestion",
                    ),
                ),
                (
                    "survey_selection_id",
                    models.ForeignKey(
                        db_column="survey_selection_id",
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="survey.surveyselection",
                    ),
                ),
            ],
            options={
                "db_table": "survey_answer",
            },
        ),
        migrations.CreateModel(
            name="SurveyTitle",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("title", models.CharField(max_length=64)),
                (
                    "survey_id",
                    models.ForeignKey(
                        db_column="survey_id",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="survey.survey",
                    ),
                ),
            ],
            options={
                "db_table": "survey_title",
            },
        ),
    ]
