
from django import forms
from .models import OfficeHour

class OfficeHourForm(forms.ModelForm):
    class Meta:
        model = OfficeHour
        fields = ['day_of_week', 'start_time', 'end_time']
        widgets = {
            'start_time': forms.TimeInput(attrs={'type': 'time'}),
            'end_time': forms.TimeInput(attrs={'type': 'time'}),
        }
from django import forms
from .models import Assignment

class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ['title', 'description', 'due_date']
        widgets = {
            'due_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
from django import forms

from django import forms

class FeedbackForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

    # You can add any other fields you'd like (e.g., rating, course name)






