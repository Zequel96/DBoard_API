from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('getAllGames/',views.getAllGames),
    path('getGame/<str:gameTitle>',views.getGame),
    path('addGame/',views.addGame),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)