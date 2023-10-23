from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.utils import timezone
from django.views import generic
from .models import Question
from .models import Choice
# Create your views here.


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        q_list = Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[:5]
        return q_list
        # return Question.objects.order_by('-pub_date')[:5]
    
class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
    model = Question 
    template_name = 'polls/results.html'


def index(request):
    # query the db for data and save.
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    template = loader.get_template("polls/index.html")
    context = {
        "latest_question_list":latest_question_list,
    }
    return HttpResponse(template.render(context,request))

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("question does not exist")
    return render(request, 'polls/detail.html', {'question':question})

def results(request, question_id):

    # renders a view the shows the votes for the choice. 
    question = get_object_or_404(Question, pk = question_id)

    return(render(request, "polls/results.html", {"question": question}))

def vote(request, question_id):
    # I need a function that creates a vote for the particular choice submitted.
    # this requires getting the choice object and incrementing its vote count
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except(KeyError, Choice.DoesNotExist):
        return render(request, "polls/detail/html", { "question":question, "error_message": "You didnt select a choice"})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results", args = [question.id,]))

