from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path("", views.chathome, name="chathome"),
    path("<str:room>/", views.room, name='room'),
    path("checkview", views.checkview, name="checkview"),
    path("send", views.send, name='send'),
    path('get_messages/<str:room>/', views.get_messages, name='get_messages'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)