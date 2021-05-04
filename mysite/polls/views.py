"""
Poll view - CRUD operations
"""
import logging as logger
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.contrib import messages
from django.urls import reverse_lazy
from utility.util import AppUtil
from .forms import QuestionAddForm
from .models import Choice, Question, UserQuestion, Vote


class IndexView(generic.ListView):
    """
    list polls
    """
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    """
    show poll details
    """
    model = Question
    template_name = 'polls/detail.html'

    def get_uservoted(self):
        """
        Checks if the current user already voted
        """
        return UserQuestion.objects.filter(question=self.kwargs['pk'], user=self.request.user)

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        question = Question.objects.filter(pub_date__lte=timezone.now())

        return question


class CreateView(generic.CreateView):
    """
    create poll
    """
    def form_valid(self, form):
        """
        Create Questions using choices and store ip using a util file
        """
        app_util = AppUtil()
        ip_address = app_util.get_client_ip(self.request)
        del app_util
        poll = form.save()
        poll.ip_address = ip_address
        poll.pub_date = timezone.now()
        poll.save()

        logger.info("creating a new poll question %d", poll.id)
        for index in range(1, 11):
            if form.cleaned_data['choice' + str(index)] != "":
                Choice(question=poll, choice_text=form.cleaned_data['choice' + str(index)]).save()

        return HttpResponseRedirect(reverse_lazy('polls:detail', args=[poll.id]))

    form_class = QuestionAddForm
    template_name = 'polls/add_poll.html'


class ResultsView(generic.DetailView):
    """
    view poll details
    """
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    """
    vote poll
    """
    question = get_object_or_404(Question, pk=question_id)

    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
        if not question.user_can_vote(request.user):
            messages.error(
                request, "You already voted this poll",
                extra_tags='alert alert-warning alert-dismissible fade show'
            )
            return redirect("polls:index")

        if selected_choice:
            choice = Choice.objects.get(id=selected_choice.id)
            Vote(user=request.user, question=question, choice=choice).save()
            logger.info("voted for a question %d by %s", question.id, str(request.user))
            UserQuestion(question=question, user=request.user).save()
            choice.votes += 1
            choice.save()

            return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })

    return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
