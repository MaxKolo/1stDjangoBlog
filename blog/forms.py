from django.forms import ModelForm, Textarea, HiddenInput
from models import Comment
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class commentForm(ModelForm):
    
    class Meta:
        model = Comment
        fields = ('author', 'content')
        #exclude = ('slug',)
        
        widgets = {
            'content':Textarea(attrs = {'rows':20, 'cols':80}),
            #'slug':HiddenInput(),
        }
    
