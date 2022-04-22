from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from .models import Choice, Criteria

class IndexView(generic.ListView):
    template_name = 'entries/index.html'
    context_object_name = 'latest_scores_list'

    def get_queryset(self):
        """Return the last five published Criterias."""
        return Criteria.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Criteria
    template_name = 'entries/detail.html'

class ResultsView(generic.DetailView):
    model = Criteria
    template_name = 'entries/results.html'

def score(request, criteria_id):
    criteria = get_object_or_404(Choice, pk=criteria_id)
    try:
        selected_choice = criteria.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the Criteria voting form.
        return render(request, 'entries/detail.html', {
            'criteria': criteria,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.score += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('entries:results', args=(criteria.id,)))
