from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePageView.as_view()),

    # API
    path('api/work-history/', WorkHistoryAPIView.as_view()),
]
