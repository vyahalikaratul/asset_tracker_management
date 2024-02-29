# views.py
import csv
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import AssetType, Asset
from .forms import AssetTypeForm, AssetForm

# Asset Type Views


class AssetTypeListView(ListView):
    """View for listing asset types."""
    model = AssetType
    template_name = 'asset_type_list.html'
    context_object_name = 'asset_types'
    paginate_by = 10


class AssetTypeCreateView(CreateView):
    """View for creating asset types."""
    model = AssetType
    form_class = AssetTypeForm
    template_name = 'create_asset_type.html'
    success_url = reverse_lazy('asset_type_list')


class AssetTypeUpdateView(UpdateView):
    """View for updating asset types."""
    model = AssetType
    form_class = AssetTypeForm
    template_name = 'update_asset_type.html'
    success_url = reverse_lazy('asset_type_list')


class AssetTypeDeleteView(DeleteView):
    """View for deleting asset types."""
    model = AssetType
    template_name = 'delete_asset_type.html'
    success_url = reverse_lazy('asset_type_list')

    def get_object(self, queryset=None):
        return get_object_or_404(AssetType, pk=self.kwargs['pk'])

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.assets.exists():
            return redirect('confirm_asset_type_delete', pk=self.object.pk)
        else:
            return super().delete(request, *args, **kwargs)


class AssetTypeConfirmDeleteView(DeleteView):
    """View for confirming deletion of asset types."""
    model = AssetType
    template_name = 'confirm_asset_type_delete.html'
    success_url = reverse_lazy('asset_type_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['asset_type'] = get_object_or_404(AssetType, pk=self.kwargs['pk'])
        return context

    def post(self, request, *args, **kwargs):
        asset_type = get_object_or_404(AssetType, pk=self.kwargs['pk'])
        if request.POST.get('confirm_delete') == 'Yes':
            asset_type.assets.all().delete()  # Delete associated assets
            asset_type.delete()
            messages.success(request, 'Asset type and associated assets deleted successfully.')
        return redirect('asset_type_list')

# Asset Views


class AssetListView(ListView):
    """View for listing assets."""
    model = Asset
    template_name = 'asset_list.html'
    context_object_name = 'assets'
    paginate_by = 10


class AssetCreateView(CreateView):
    """View for creating assets."""
    model = Asset
    form_class = AssetForm
    template_name = 'create_asset.html'
    success_url = reverse_lazy('asset_list')


class AssetUpdateView(UpdateView):
    """View for updating assets."""
    model = Asset
    form_class = AssetForm
    template_name = 'update_asset.html'
    success_url = reverse_lazy('asset_list')


class AssetDeleteView(DeleteView):
    """View for deleting assets."""
    model = Asset
    template_name = 'delete_asset.html'
    success_url = reverse_lazy('asset_list')

    def get_object(self, queryset=None):
        return get_object_or_404(Asset, pk=self.kwargs['pk'])

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        return self.object.delete_with_confirmation(request, *args, **kwargs)

