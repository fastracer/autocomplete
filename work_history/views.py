from django.views.generic.base import TemplateView
from django.db.models import Q
from drf_multiple_model.views import ObjectMultipleModelAPIView
from .models import *
from .serializers import *


class HomePageView(TemplateView):
    template_name = "index.html"


class WorkHistoryAPIView(ObjectMultipleModelAPIView):

    def get_querylist(self):
        search = self.request.query_params['search']
        querylist = (
            {
                'queryset': Bio.objects.filter(test__contains=search),
                'serializer_class': BioSerializer
            },
            {
                'queryset': Location.objects.filter(place__contains=search),
                'serializer_class': LocationSerializer
            },
            {
                'queryset': PreviousClient.objects.filter(
                    Q(first_name__contains=search) | Q(last_name__contains=search)),
                'serializer_class': PreviousClientSerializer
            },
            {
                'queryset': Skill.objects.filter(title__contains=search),
                'serializer_class': SkillSerializer
            },
        )

        return querylist
