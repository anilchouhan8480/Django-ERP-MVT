from django import forms

from .models import Gst_Model


class Gst_Forms(forms.ModelForm):
    class Meta:
        model = Gst_Model
        fields = ['Description', 'Gst', 'Created_By']
        labels = {
            'Gst': 'GST',

        }
