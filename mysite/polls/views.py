from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def detail(request, question_id):
    return HttpResponse("Você esta vendo uma pergunta %s." % question_id)


def results(request, question_id):
    response = "Vc esta vendo o resultado %s."
    return HttpResponse(response %question_id)


def vote(request, question_id):
	return HttpResponse("Vc esta vendo o voto em uma pergunta %s." % question_id)
