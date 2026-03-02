from .models import StudResults
from django import forms
class StudResultsForm(forms.ModelForm):
    class Meta:
        model = StudResults
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        maths = cleaned_data.get('maths')
        physics = cleaned_data.get('physics')
        biology = cleaned_data.get('biology')
        social = cleaned_data.get('social')
        english = cleaned_data.get('english')

        subjects = (maths,physics,biology,social,english)
        for subject in subjects:
            if (subject<0 or subject>100):
                raise forms.ValidationError('Marks should be between 0 and 100')

