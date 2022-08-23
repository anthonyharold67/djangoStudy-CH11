from django.urls import path
from .views import home,course_detail

urlpatterns = [
     path('',home,name='anasayfa'),
     path('<int:id>',course_detail,name="course_detail")
]
