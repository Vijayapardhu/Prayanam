from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['place', 'package', 'rating', 'category', 'comment']
        widgets = {
            'place': forms.Select(attrs={'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'}),
            'package': forms.Select(attrs={'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'}),
            'rating': forms.Select(attrs={'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'}),
            'category': forms.Select(attrs={'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'}),
            'comment': forms.Textarea(attrs={'rows': 4, 'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Make place and package optional
        self.fields['place'].required = False
        self.fields['package'].required = False
        
        # Add empty choice
        self.fields['place'].empty_label = "Select a place (optional)"
        self.fields['package'].empty_label = "Select a package (optional)"
    
    def clean(self):
        cleaned_data = super().clean()
        place = cleaned_data.get('place')
        package = cleaned_data.get('package')
        
        # Ensure at least one of place or package is selected
        if not place and not package:
            raise forms.ValidationError("Please select either a place or a package.")
        
        return cleaned_data
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['place', 'package', 'rating', 'category', 'comment']
        widgets = {
            'place': forms.Select(attrs={'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'}),
            'package': forms.Select(attrs={'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'}),
            'rating': forms.Select(attrs={'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'}),
            'category': forms.Select(attrs={'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'}),
            'comment': forms.Textarea(attrs={'rows': 4, 'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Make place and package optional
        self.fields['place'].required = False
        self.fields['package'].required = False
        
        # Add empty choice
        self.fields['place'].empty_label = "Select a place (optional)"
        self.fields['package'].empty_label = "Select a package (optional)"
    
    def clean(self):
        cleaned_data = super().clean()
        place = cleaned_data.get('place')
        package = cleaned_data.get('package')
        
        # Ensure at least one of place or package is selected
        if not place and not package:
            raise forms.ValidationError("Please select either a place or a package.")
        
        return cleaned_data
