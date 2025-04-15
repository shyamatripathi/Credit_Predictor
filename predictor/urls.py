from django.contrib import admin
from django.urls import path
from predictor import views
from .views import predict_credit_score_api
app_name = 'predictor'  # ✅ Required for URL namespacing

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', views.home, name='home')
    path('', views.home, name='home'),
    path('download_pdf/', views.download_pdf, name='download_pdf'),
    path('predict/', views.predict_credit_score, name='predict_credit_score'),
    path('api/predict/', predict_credit_score_api, name='predict_credit_score_api'),
]


