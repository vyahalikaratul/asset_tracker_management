# views.py
from django.shortcuts import render
from django.db.models import Count
from asset_management.models import AssetType, Asset

def dashboard(request):
    # Data for the PIE chart - count of assets per asset type
    asset_type_counts = Asset.objects.values('asset_type__name').annotate(total=Count('id'))

    # Data for the BAR chart - count of active and inactive assets
    active_inactive_counts = Asset.objects.values('is_active').annotate(total=Count('id'))

    return render(request, 'dashboard.html', {
        'asset_type_counts': asset_type_counts,
        'active_inactive_counts': active_inactive_counts
    })
