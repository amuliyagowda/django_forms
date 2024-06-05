from django import forms
from app.models import *
from django.core.validators import RegexValidator,MinLengthValidator

def validate_for_a(value):
    if value[0]=='a':
        raise forms.ValidationError('should not start with a')
    
def validate_for_s(value):
    if value[0]!='a':
        raise forms.ValidationError('should start with a')
    
def validate_for_len(value):
    if len(value)<5:
        raise forms.ValidationError('length should be more than 5')
    

class Topicform(forms.Form):
    topic_name=forms.CharField(validators=[validate_for_a,validate_for_len])
    mobile_number=forms.CharField(min_length=10,max_length=10,validators=[RegexValidator('[6-9]\d{9}')])

#def validate_for_url(value):
    #if value.endswidth('.com'):
        #raise forms.ValidationError('please check')
    
def validate_for_len(value):
    if len(value)<10:
        raise forms.ValidationError('length should be more than 10')

class Webpagesform(forms.Form):
    topic_name=forms.ModelChoiceField(queryset=Topic.objects.all())
    name=forms.CharField(max_length=50,validators=[validate_for_s])
    url=forms.URLField()
    email=forms.EmailField()
    reemail=forms.EmailField()
    botchatcher=forms.CharField(widget=forms.HiddenInput,required=False)

    def clean_botcatcher(self):
        cu=self.cleaned_data['botcatcher']
        if len(cu)>0:
            raise forms.ValidationError('bot us catched')
        
    def clean(self):
        em=self.cleaned_data['email']
        rem=self.cleaned_data['reemail']
        if em!=rem:
            raise forms.ValidationError('Email doesnt match')


class AccessRecordsform(forms.Form):
    name=forms.ModelChoiceField(queryset=Webpages.objects.all())
    date=forms.DateField()
    author=forms.CharField()

