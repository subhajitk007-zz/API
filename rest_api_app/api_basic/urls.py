
from django.urls import path
from .views import UserAPIView#,ActivityDetails
# from .views import user_list
urlpatterns = [

    path('info/', UserAPIView.as_view()),
    # path('detail/<int:id>/', ActivityDetails.as_view()),

]