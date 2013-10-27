from rest_framework import viewsets
from rest_framework import serializers
from pycones.sponsors.models import Sponsor

class SponsorSerializer(serializers.HyperlinkedModelSerializer):
    level = serializers.ChoiceField(source='get_level_display')

    class Meta:
        model = Sponsor

class SponsorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Sponsor.objects.all()
    serializer_class = SponsorSerializer
