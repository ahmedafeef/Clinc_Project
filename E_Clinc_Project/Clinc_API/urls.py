from django.conf.urls.static import static

from ClincProject import settings

urlpatterns = [

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# urlpatterns += static(settings.STATIC_URL, document_root=settings.Sta)
