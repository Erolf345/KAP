from survey.models import TextQuestion


def survey_count(request):
    count = TextQuestion.objects.count()
    return {"survey_count": count}

