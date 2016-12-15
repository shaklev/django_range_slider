from django import forms
from django_range_slider.fields import RangeSliderField
from .models import TestModel

class TestFieldForm(forms.Form):

    class Meta:
        model = TestModel
        fields = ['range_field','name_range_field','label_range_field']

    def __init__(self, *args, **kwargs):
        super(TestFieldForm, self).__init__(*args, **kwargs)
        self.fields['name_range_field'] = RangeSliderField(minimum=30,maximum=300,name="TestName")
        self.fields['range_field'] = RangeSliderField(minimum=10,maximum=102)
        self.fields['label_range_field'] = RangeSliderField(label=True,minimum=1,maximum=10)
