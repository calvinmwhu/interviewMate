__author__ = 'calvinmwhu'
from django import forms
from interviewmate.models import Category, Question

class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text="please enter the category name")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(),required=False)

    class Meta:
        model = Category
        fields = ('name',)


class QuestionForm(forms.ModelForm):
    title = forms.CharField(max_length=128, help_text="Please enter the title of the question")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    content = forms.CharField(widget=forms.Textarea, help_text="enter the question content")

    class Meta:
        model = Question
        exclude = ('category',)


