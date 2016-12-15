# DJANGO RANGE SLIDER

<snippet>
  <content>

[![Build Status](https://travis-ci.org/Chive/django-multiupload.svg?branch=master)](https://travis-ci.org/Chive/django-multiupload)


Dead simple drop-in multi file upload field for django forms using HTML5's ``multiple`` attribute.

## Installation

* Install the package using pip (or easy_install if you really have to)

```bash
$ pip install django-multiupload
```

* Or directly from this repository to get the development version (if you're feeling adventurous)

```bash
$ pip install -e git+https://github.com/Chive/django-multiupload.git#egg=multiupload
```

## Usage

Add the form field to your form and make sure to save the uploaded files in the form's ``save`` method.

For more detailed examples visit the [examples section](https://github.com/Chive/django-multiupload/tree/master/examples).


```python
# forms.py
from django import forms
from multiupload.fields import MultiFileField

class UploadForm(forms.Form):
    attachments = MultiFileField(min_num=1, max_num=3, max_file_size=1024*1024*5)

    # If you need to upload media files, you can use this:
    attachments = MultiMediaField(
        min_num=1, 
        max_num=3, 
        max_file_size=1024*1024*5, 
        media_type='video'  # 'audio', 'video' or 'image'
    )

    # For images (requires Pillow for validation):
    attachments = MultiImageField(min_num=1, max_num=3, max_file_size=1024*1024*5)
```

The latter two options just add fancy attributes to HTML's `<input>`, restricting the scope to corresponding filetypes.

```python
# models.py
from django.db import models

class Attachment(models.Model):
    file = models.FileField(upload_to='attachments')

```

```python
# views.py
from django.views.generic.edit import FormView
from .forms import UploadForm
from .models import Attachment

class UploadView(FormView):
    template_name = 'form.html'
    form_class = UploadForm
    success_url = '/done/'

    def form_valid(self, form):
        for each in form.cleaned_data['attachments']:
            Attachment.objects.create(file=each)
        return super(UploadView, self).form_valid(form)

```

## License
MIT License

Copyright (c) 2016 Aleksandar

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

</content>
</snippet>
