"""pollsapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from polls.apiviews import PollList, PollDetail,ChoiceList, CreateVote,UserCreate,LoginView
from rest_framework.routers import DefaultRouter
from polls.apiviews import PollViewSet
from rest_framework.authtoken import views
from rest_framework.documentation import include_docs_urls


router = DefaultRouter()
router.register('polls', PollViewSet)

urlpatterns = [

path("polls/", PollList.as_view(), name="polls_list"),
path("polls/<int:pk>/", PollDetail.as_view(), name="polls_detail"),
path("polls/<int:pk>/choices/", ChoiceList.as_view(), name="choice_list"),
path("polls/<int:pk>/choices/<int:choice_pk>/vote/", CreateVote.as_view(), name="polls_list"),
path("login/", LoginView.as_view(), name="login"),
path("users/", UserCreate.as_view(), name="user_create"),
#path("login/", views.obtain_auth_token, name="login"),
path(r'docs/', include_docs_urls(title='Polls API')),



]

urlpatterns += router.urls