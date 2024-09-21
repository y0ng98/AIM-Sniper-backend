from abc import ABC, abstractmethod


class SurveyTitleRepository(ABC):
    @abstractmethod
    def registerTitle(self, survey, surveyTitle):
        pass
