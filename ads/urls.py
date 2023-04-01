from django.urls import path, include
from .views import AdsList, AdsCreate, AdsDetail, AdsUpdate, AdsDelete

urlpatterns = [
    path('', AdsList.as_view(), name='ads_list'),
    path('<int:pk>', (AdsDetail.as_view()), name='ads'),
    path('create/', AdsCreate.as_view(), name='ads_create'),
    path('<int:pk>/edit', AdsUpdate.as_view(), name='ads_edit'),
    path('<int:pk>/delete', AdsDelete.as_view(), name='ads_delete'),
]