
from django import forms
from .models import AssetType, Asset


class AssetTypeForm(forms.ModelForm):
    """
    Form class for creating and updating AssetType objects.

    This form is used in the creation and updating of AssetType objects in the Django admin interface.
    It includes validation for the asset type name to ensure it is at least 3 characters long and
    unique within the database.
    """
    class Meta:
        model = AssetType
        fields = ['name', 'description', 'created_at']

    def clean_name(self):
        """
        Custom validation method for ensuring uniqueness and minimum length of the asset type name.

        Raises:
            forms.ValidationError: If the asset type name is not at least 3 characters long or
                                     if an asset type with the same name already exists in the database.
        """
        name = self.cleaned_data.get('name')
        if len(name) < 3:
            raise forms.ValidationError("Asset type name must be at least 3 characters long.")

        try:
            AssetType.objects.get(name=name)
            raise forms.ValidationError("An asset type with this name already exists.")
        except AssetType.DoesNotExist:
            return name


class AssetForm(forms.ModelForm):
    """
    Form class for creating and updating Asset objects.

    This form is used in the creation and updating of Asset objects in the Django admin interface.
    It includes validation for the asset name to ensure it is at least 3 characters long and
    unique within the database.
    """
    class Meta:
        model = Asset
        fields = ['name', 'asset_type', 'is_active', 'created_at']

    def clean_name(self):
        """
        Custom validation method for ensuring uniqueness and minimum length of the asset name.

        Raises:
            forms.ValidationError: If the asset name is not at least 3 characters long or
                                     if an asset with the same name already exists in the database.
        """
        name = self.cleaned_data.get('name')
        # asset_type = self.cleaned_data.get('asset_type')
        if len(name) < 3:
            raise forms.ValidationError("Asset name must be at least 3 characters long.")

        assets_with_same_name = Asset.objects.filter(name=name)

        if assets_with_same_name.exists():
            raise forms.ValidationError("An asset with this name already exists.")

        return name