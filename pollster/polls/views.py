from django.shortcuts import render

# Create your views here.
from .models import Questions,Choice

def index(request):
    latest_question_list = Questions.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list':latest_question_list}
    return render(request,'polls/index.html',context)

def detail(request,question_id):
    try:
        question = Questions.objects.get(pk=question_id)
    except Questions.DoesNotExist:
        raise Http404("Question DOes NOt Exist")

    return render(request,'polls/results.html',{'question':question})

def results(request,question_id):
    question = get_object_or_404(Questions,pk=question_id)
    return render(request,'polls/results.html',{'question':question})