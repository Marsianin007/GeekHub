from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'products'


urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# urlpatterns = [
#     path('', views.index),
#     path('register/', views.register, name='register'),
#     path('login/', views.user_login, name='login'),
#     path('women/', views.product_list_women)
# ]
