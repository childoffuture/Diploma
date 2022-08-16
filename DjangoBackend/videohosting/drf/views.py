from rest_framework.response import Response
from rest_framework.views import APIView

from videoportal.models import Video, Subscription

from .serializers import BaseSerializer


class DrfBaseView(APIView):
    def get(self, request):
        queryset = self.init_queryset()
        serializer = BaseSerializer(queryset, many=True)
        return Response(serializer.data)

    def init_queryset(self):
        return Video.objects.all()


class DrfSubscriptionView(DrfBaseView):
    def init_queryset(self):
        return Video.objects.filter(id_category__in=Subscription.objects.filter(id_user=self.request.user).values('id_category'))


class DrfRecommendView(DrfBaseView):
    def init_queryset(self):
        return Video.objects.filter(pk__in=Video.objects.all().order_by('-created').values('pk')[:5])


class DrfMyVideoView(DrfBaseView):
    def init_queryset(self):
        return Video.objects.filter(id_author=self.request.user)