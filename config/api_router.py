from django.conf import settings
from django.urls import path
from rest_framework.routers import DefaultRouter, SimpleRouter

from toastiedata.club.api.views import MemberList, BestSpeaker ,BestEvaluator, BestTableTopicSpeaker
from toastiedata.users.api.views import UserViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)


app_name = "api"
urlpatterns = router.urls

urlpatterns += [
    path("members/", MemberList.as_view()),
    path("bestspeakers/", BestSpeaker.as_view()),
    path("bestevaluators/", BestSpeaker.as_view()),
    path("besttabletopicspeakers/", BestSpeaker.as_view()),
    

]
