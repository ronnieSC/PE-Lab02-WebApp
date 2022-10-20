from django import forms

from .models import Proveedor

class provForm(forms.ModelForm):
	class Meta:
		model = Proveedor
		fields = [
			'ProCod',
			'ProNom',
			'ProDir',
            'ProTel',
		]