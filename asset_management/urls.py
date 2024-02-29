from django.urls import path
from . import views

urlpatterns = [
    # AssetType URLs
    path('', views.AssetTypeListView.as_view(), name='asset_type_list'),
    path('asset-types/', views.AssetTypeListView.as_view(), name='asset_type_list'),
    path('asset-types/create/', views.AssetTypeCreateView.as_view(), name='create_asset_type'),
    path('asset-types/<int:pk>/update/', views.AssetTypeUpdateView.as_view(), name='update_asset_type'),
    path('asset-types/<int:pk>/delete/', views.AssetTypeDeleteView.as_view(), name='delete_asset_type'),
    path('asset-types/<int:pk>/confirm-delete/', views.AssetTypeConfirmDeleteView.as_view(), name='confirm_asset_type_delete'),

    # Asset URLs
    path('assets/', views.AssetListView.as_view(), name='asset_list'),
    path('assets/create/', views.AssetCreateView.as_view(), name='create_asset'),
    path('assets/<int:pk>/update/', views.AssetUpdateView.as_view(), name='update_asset'),
    path('assets/<int:pk>/delete/', views.AssetDeleteView.as_view(), name='delete_asset'),
    path('assets/<int:pk>/confirm-delete/', views.AssetDeleteView.as_view(), name='confirm_asset_delete'),
    # Download Assets URL
    # path('download-assets/', views.download_assets, name='download_assets'),
]
