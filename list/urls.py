from django.urls import path
from .import views
from django.views.generic.base import RedirectView

urlpatterns = [
    path('notice/',views.NoticeListView.as_view(), name='notice'),
    path('notice/<int:pk>', views.NoticeDetailView.as_view()),
    path('', RedirectView.as_view(url='notice/'))
]
