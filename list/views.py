from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Notice
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


# Create your views here.

class NoticeListView(ListView):
    model = Notice

@method_decorator(login_required,name='dispatch')
class NoticeDetailView(DetailView):
    model = Notice
