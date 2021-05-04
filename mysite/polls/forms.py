"""
Form components for poll app
"""
from django import forms
from .models import Question, Choice


class QuestionAddForm(forms.ModelForm):
    """
    Add Question form input fields
    """
    choice1 = forms.CharField(label='Choice 1', max_length=100, min_length=2, required=True,
                              widget=forms.TextInput(attrs={'class': 'form-control is-invalid'}))
    choice2 = forms.CharField(label='Choice 2', max_length=100, min_length=2, required=True,
                              widget=forms.TextInput(attrs={'class': 'form-control is-invalid'}))
    choice3 = forms.CharField(label='Choice 3', max_length=100, min_length=2, required=False,
                              widget=forms.TextInput(attrs={'class': 'form-control'}))
    choice4 = forms.CharField(label='Choice 4', max_length=100, min_length=2, required=False,
                              widget=forms.TextInput(attrs={'class': 'form-control'}))
    choice5 = forms.CharField(label='Choice 5', max_length=100, min_length=2, required=False,
                              widget=forms.TextInput(attrs={'class': 'form-control'}))
    choice6 = forms.CharField(label='Choice 6', max_length=100, min_length=2, required=False,
                              widget=forms.TextInput(attrs={'class': 'form-control'}))
    choice7 = forms.CharField(label='Choice 7', max_length=100, min_length=2, required=False,
                              widget=forms.TextInput(attrs={'class': 'form-control'}))
    choice8 = forms.CharField(label='Choice 8', max_length=100, min_length=2, required=False,
                              widget=forms.TextInput(attrs={'class': 'form-control'}))
    choice9 = forms.CharField(label='Choice 9', max_length=100, min_length=2, required=False,
                              widget=forms.TextInput(attrs={'class': 'form-control'}))
    choice10 = forms.CharField(label='Choice 10', max_length=100, min_length=2, required=False,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        """
        Config the meta tags
        """
        model = Question
        fields = [
            'question_text', 'choice1', 'choice2',
            'choice3', 'choice4', 'choice5', 'choice6',
            'choice7', 'choice8', 'choice9', 'choice10',
        ]
        widgets = {
            'question_text': forms.Textarea(
                attrs={'class': 'form-control is-invalid', 'rows': 5, 'cols': 20}
            ),
        }


class EditQuestionForm(forms.ModelForm):
    """
    Edit Question form input fields
    """
    class Meta:
        """
        Config the meta tags
        """
        model = Question
        fields = ['question_text', ]
        widgets = {
            'question_text': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'cols': 20}),
        }


class ChoiceAddForm(forms.ModelForm):
    """
    Add Choice form input fields
    """
    class Meta:
        """
        Config the meta tags
        """
        model = Choice
        fields = ['choice_text', ]
        widgets = {
            'choice_text': forms.TextInput(attrs={'class': 'form-control', })
        }
