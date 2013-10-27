from rest_framework import viewsets
from rest_framework import serializers
from pycones.call4papers.models import Talk, Speaker

class TalkSerializer(serializers.HyperlinkedModelSerializer):
    level = serializers.ChoiceField(source='get_level_display')
    sc_hour = serializers.ChoiceField(source='get_sc_hour_display')
    sc_track = serializers.ChoiceField(source='get_sc_track_display')
    sc_day = serializers.ChoiceField(source='get_sc_day_display')

    class Meta:
        model = Talk
        exclude = ('selected', 'slot')

class SpeakerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Speaker


class TalkViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Talk.objects.filter(selected=True)
    serializer_class = TalkSerializer


class SpeakerViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Speaker.objects.filter(talks__selected=True)
    serializer_class = SpeakerSerializer
