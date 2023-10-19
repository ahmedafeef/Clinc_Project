from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

import Clinc_API
from ClincProject import settings
from Clinc_API import views,urls
from Clinc_API.views import LoginView

router = routers.DefaultRouter()
router.register(r'gender', views.GenderViewSet)
router.register(r'InsuranceCompanies', views.InsuranceCompaniesViewSet)
router.register(r'clinic', views.ClinicViewSet)
router.register(r'patient', views.PatientViewSet)
router.register(r'session', views.SessionViewSet)
router.register(r'document', views.DocumentViewSet)
router.register(r'doctor', views.DectorViewSet)
router.register(r'bookingstatus', views.BookingStatusViewSet)
router.register(r'booking', views.BookingViewSet)
router.register(r'users', views.UsersViewSet)

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
    path('', include(Clinc_API.urls)),
]


urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('login2/', LoginView.as_view(), name='login1'),
    path('accounting/', include('hordak.urls', namespace='hordak')),
    path('login/', views.UserLoginApiView.as_view()),
)

