from django import forms
from .widgets import RangeSlider

class RangeSliderField(forms.CharField):
    def __init__(self, *args, **kwargs):
        self.name = kwargs.pop('name', '')
        self.minimum = kwargs.pop('minimum',0)
        self.maximum = kwargs.pop('maximum',100)
        kwargs['widget'] = RangeSlider(self.minimum, self.maximum, self.name)
        if 'label' not in kwargs.keys():
            kwargs['label'] = False
        super(RangeSliderField, self).__init__(*args, **kwargs)
