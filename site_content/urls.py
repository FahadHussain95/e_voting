from django.urls import path
from site_content.views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('candidates/', ShowCandidates.as_view(), name='candidates'),
    path('vote/', RegisterVote.as_view(), name='vote')
]