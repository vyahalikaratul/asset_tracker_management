from django.contrib import admin
from django.contrib.admin import AdminSite
from .models import AssetType, Asset, AssetImage
from .forms import AssetForm, AssetTypeForm
from django.http import HttpResponse


import csv


# Inline representation for AssetImage model in Asset admin


class AssetImageInline(admin.TabularInline):
    """
    Inline model admin for managing AssetImage objects within the Asset admin interface.

    This allows administrators to add, edit, and delete AssetImage objects inline with Asset objects.
    """
    model = AssetImage
    extra = 1


class AssetTypeAdmin(admin.ModelAdmin):
    """
    Model admin for managing AssetType objects in the Django admin interface.

    This class provides a customized representation of AssetType objects in the admin interface,
    including a custom display of assets count associated with each asset type.
    """
    form = AssetTypeForm

    list_display = ('name', 'description', 'get_assets_count')
    list_per_page = 2

    def get_assets_count(self, obj):
        """Custom method to display the count of assets associated with each asset type."""
        return obj.asset_set.count()

    get_assets_count.short_description = 'Assets Count'


# admin.site.register(AssetType, AssetTypeAdmin)


class AssetAdmin(admin.ModelAdmin):
    """
    Model admin for managing Asset objects in the Django admin interface.

    This class provides a customized representation of Asset objects in the admin interface,
    including functionality to download all assets as a CSV file.
    """
    form = AssetForm
    list_display = ('name', 'code', 'asset_type', 'is_active', 'created_at', 'updated_at')
    list_filter = ('asset_type', 'is_active')
    search_fields = ('name', 'asset_type__name')  # Allows searching by asset name or asset type name
    list_per_page = 2
    inlines = [AssetImageInline]

    def download_all_assets(self, request, queryset):
        """Custom action to download all assets as a CSV file."""
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="all_assets.csv"'
        writer = csv.writer(response)
        writer.writerow(['Name', 'Code', 'Asset Type', 'Is Active', 'Created At', 'Updated At'])
        assets = Asset.objects.all()
        for asset in assets:
            writer.writerow(
                [asset.name, asset.code, asset.asset_type.name, asset.is_active, asset.created_at, asset.updated_at])
        return response

    download_all_assets.short_description = "Download all assets as CSV"

    actions = ['download_all_assets']


class MyAdminSite(AdminSite):
    site_header = 'Asset Tracker System Admin'  # Set your custom admin name here


# Instantiate your custom admin site
admin_site = MyAdminSite(name='myadmin')


admin_site.register(Asset, AssetAdmin)
admin_site.register(AssetType, AssetTypeAdmin)

