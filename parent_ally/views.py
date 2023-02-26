from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic

from .distance_utility import distance
from .models import Posting
from .forms import PostingForm


# Create your views here.
def index(request):
    return render(request, 'parent_ally/dummy_index.html')


class ListView(generic.ListView):
    template_name = 'parent_ally/dummy_list.html'
    context_object_name = 'postings_list'

    def get_queryset(self):
        # Sort by recency
        return Posting.objects.order_by('-create_date')[:5]


class ListViewNoImages(generic.ListView):
    template_name = 'parent_ally/dummy_list.html'
    context_object_name = 'postings_list'


class DetailView(generic.DetailView):
    model = Posting
    template_name = 'parent_ally/dummy_detail.html'
    context_object_name = 'posting'


@login_required(login_url='common:login')
def delete_posting(request, pk):
    posting = get_object_or_404(Posting, pk=pk)
    if request.user == posting.author.user:
        posting.delete()

    return redirect('/')


def create_posting(request):
    form = PostingForm()
    return render(request, 'parent_ally/posting_form.html', {'form': form})
