from django import forms
from .models import Review
RATING_CHOICES = [
        (1, '1 ⭐'),
        (2, '2 ⭐⭐'),
        (3, '3 ⭐⭐⭐'),
        (4, '4 ⭐⭐⭐⭐'),
        (5, '5 ⭐⭐⭐⭐⭐'),
    ]
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['user_name','rating', 'title', 'comment', 'visit_date']
        widgets = {
            'rating': forms.Select(choices=RATING_CHOICES, attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Résumez votre expérience'}),
            'user_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Résumez votre Prenom et Nom'}),
            'comment': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Partagez votre expérience en détail...'}),
            'visit_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }
