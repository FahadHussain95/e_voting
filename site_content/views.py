from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
from site_content.models import Candidate
from site_content.serializers import CandidateSerializer


class HomeView(TemplateView):
    template_name = 'landing_page.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(HomeView, self).dispatch(*args, **kwargs)


class ShowCandidates(APIView):
    permission_classes = [AllowAny]
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'show_candidates.html'

    def get(self, request):
        candidate_obj = Candidate.objects.all()
        if len(candidate_obj) > 0:
            serialized_candidates = CandidateSerializer(candidate_obj, many=True)
            if serialized_candidates:
                return Response(data={'candidates': serialized_candidates.data}, status=status.HTTP_200_OK)
        else:
            return HttpResponse(status=status.HTTP_401_UNAUTHORIZED)


class RegisterVote(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        if request.data:
            candidate_id = request.data.get('candidate_id')
            party_name = request.data.get('party_name')
            vote_count = request.data.get('vote_count')
            candidate_obj = Candidate.objects.filter(id=candidate_id, vote_count=vote_count, candidate_party__party_name=party_name).first()
            if candidate_obj:
                candidate_obj.vote_count += 1
                candidate_obj.save()
                # serialized_candidates = CandidateSerializer(candidate_obj, many=True)
                # if serialized_candidates:
                return render(request, 'show_candidates.html')
            else:
                return HttpResponse(status=status.HTTP_401_UNAUTHORIZED)
