from django.urls import path
from .views import PatoListCreatAPIView, PatoRetrieveUpdateDestroyAPIView, LoginView
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('patos/',PatoListCreatAPIView.as_view(), name='pato-list-all'),
    path('patos/<int:pk>/',PatoRetrieveUpdateDestroyAPIView.as_view(), name='pato-especifico'),
    path('logar/', LoginView.as_view(), name='logar')
]       
if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)