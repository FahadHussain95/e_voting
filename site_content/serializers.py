from rest_framework import serializers

from site_content.models import Candidate, Party


class PartySerializer(serializers.ModelSerializer):
    class Meta:
        model = Party
        fields = '__all__'


class CandidateSerializer(serializers.ModelSerializer):
    candidate_party = PartySerializer(many=False, read_only=True)

    class Meta:
        model = Candidate
        fields = '__all__'