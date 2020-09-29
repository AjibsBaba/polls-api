from django.urls import path, include, re_path
from polls.views import userCreate, loginView, pollList, pollDetail, choiceList, createVote
from rest_framework.routers import DefaultRouter
from .views import PollViewSet
from rest_framework import permissions
from django.views.generic import TemplateView
from rest_framework.documentation import include_docs_urls
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Polls APi')

router = DefaultRouter()
router.register('polls', PollViewSet, basename='polls')



urlpatterns = [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('register/', userCreate.as_view(), name='user-create'),
    path('login/', loginView.as_view(), name='login'),
    path('polls/', pollList.as_view(), name='polls-list'),
    path('polls/<int:pk>', pollDetail.as_view(), name='polls-details'),
    path('polls/<int:pk>/choices/', choiceList.as_view(), name='choice-list'),
    path('polls/<int:pk>/choices/<int:choice_pk>/vote', createVote.as_view(), name='create-vote'),
    path('', schema_view)

]
