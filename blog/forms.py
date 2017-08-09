from django.forms import ModelForm, Textarea, HiddenInput
from models import Comment



class commentForm(ModelForm):
    
    class Meta:
        model = Comment
        fields = ('author', 'content')
        #exclude = ('slug',)
        
        widgets = {
            'content':Textarea(attrs = {'rows':20, 'cols':80}),
            #'slug':HiddenInput(),
        }
    
