from django import forms

from .models import Presentacion

class presForm(forms.ModelForm):
	class Meta:
		model = Presentacion
		fields = [
			'PreCod',
			'PreDes',
		]