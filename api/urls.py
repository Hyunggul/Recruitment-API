from django.urls import path
from . import views
app_name = "api"
urlpatterns = [
    path(route ="",view = views.RecruitmentAPI.as_view(), name = "all"),
    path(route ="<int:pk>/",view = views.RecruitmentDetailAPI.as_view(), name = "detail"),
]