from django import forms
from django.utils.safestring import mark_safe
import re

class RangeSlider(forms.TextInput):
    def __init__(self, minimum, maximum, step, elem_name,*args,**kwargs):
        widget = super(RangeSlider,self).__init__(*args,**kwargs)
        self.minimum = str(minimum)
        self.maximum = str(maximum)
        self.step = str(step)
        self.elem_name = str(elem_name)

    def render(self, name, value, attrs=None, renderer=None):
        s = super(RangeSlider, self).render(name, value, attrs)
        self.elem_id = re.findall(r'id_([A-Za-z0-9_\./\\-]*)"',s)[0]
        html = """<div id="slider-range-"""+self.elem_id+""""></div>
        <script>
        $('#id_"""+self.elem_id+"""').attr("readonly", true)
        $( "#slider-range-"""+self.elem_id + """" ).slider({
        range: true,
        min: """+self.minimum+""",
        max: """+self.maximum+""",
        step: """+self.step+""",
        values: [ """+self.minimum+""","""+self.maximum+""" ],
        slide: function( event, ui ) {
          $( "#id_"""+self.elem_id+"""" ).val(" """ + self.elem_name + """ "+ ui.values[ 0 ] + " - " + ui.values[ 1 ] );
        }
        });
        $( "#id_"""+self.elem_id+"""" ).val(" """ + self.elem_name + """ "+ $( "#slider-range-""" + self.elem_id + """" ).slider( "values", 0 ) +
        " - " + $( "#slider-range-"""+ self.elem_id + """" ).slider( "values", 1 ) );
        </script>
        """
        return mark_safe(s+html)

