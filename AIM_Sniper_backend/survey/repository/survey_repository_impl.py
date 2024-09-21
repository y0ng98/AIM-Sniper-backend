from survey.entity.survey import Survey
from survey.repository.survey_repository import SurveyRepository


class SurveyRepositoryImpl(SurveyRepository):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def getMaxId(self):
        survey = Survey.objects.all()
        surveyMaxId = len(survey)
        return surveyMaxId

    def registerSurvey(self, surveyId):
        Survey.objects.create(survey=surveyId)
        return surveyId

    def findSurvey(self, surveyId):
        survey = Survey.objects.get(survey=surveyId)
        return survey

