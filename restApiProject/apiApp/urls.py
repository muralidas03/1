from django.urls import path
from .views import *

urlpatterns = [
    path('item', ItemListCreate.as_view()),
    path('item/<int:id>/',ItemInfo.as_view())
]