from django.urls import path
from .import views
urlpatterns = [
    # path('',views.DataGet),
    path('',views.ImageUpload)
]