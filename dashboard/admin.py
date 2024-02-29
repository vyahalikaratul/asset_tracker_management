# # admin.py
#
# from django.contrib import admin
# from django.http import JsonResponse
# from chartjs.views.lines import BaseLineChartView
# from asset_management.models import AssetType, Asset
#
# class MyAdminSite(admin.AdminSite):
#     def index(self, request, extra_context=None):
#         extra_context = extra_context or {}
#         asset_type_count_data = self.get_asset_type_count()
#         asset_status_count_data = self.get_asset_status_count()
#         extra_context['asset_type_count_data'] = asset_type_count_data
#         extra_context['asset_status_count_data'] = asset_status_count_data
#         return super().index(request, extra_context)
#
#     def get_asset_type_count(self):
#         asset_types = AssetType.objects.all()
#         data = {'labels': [], 'data': []}
#         for asset_type in asset_types:
#             data['labels'].append(asset_type.name)
#             data['data'].append(asset_type.asset_set.count())
#         return data
#
#     def get_asset_status_count(self):
#         active_assets = Asset.objects.filter(is_active=True).count()
#         inactive_assets = Asset.objects.filter(is_active=False).count()
#         data = {'labels': ['Active', 'Inactive'], 'data': [active_assets, inactive_assets]}
#         return data
#
# admin_site = MyAdminSite(name='myadmin')
