from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from .models import Rating, Audio


class RatingForm(forms.ModelForm):
	pronounciation_score = forms.IntegerField(
		min_value=0,
		max_value=5,
		widget=forms.NumberInput(attrs={"type": "range", "min": 0, "max": 5}),
		label="Pronunciation (0-5)",
	)
	naturalness_score = forms.IntegerField(
		min_value=0,
		max_value=5,
		widget=forms.NumberInput(attrs={"type": "range", "min": 0, "max": 5}),
		label="Naturalness (0-5)",
	)
	noise_score = forms.IntegerField(
		min_value=0,
		max_value=5,
		widget=forms.NumberInput(attrs={"type": "range", "min": 0, "max": 5}),
		label="Noise (0-5)",
	)
	edit_transcript = forms.CharField(
		widget=forms.Textarea(attrs={"rows": 3}), required=False, label="Transcript (optional)"
	)
	uid = forms.ModelChoiceField(queryset=User.objects.all(), widget=forms.HiddenInput(), required=True)
	audio_id = forms.IntegerField(widget=forms.HiddenInput(), required=True)
    
	class Meta:
		model = Rating
		fields = [
			"uid",
			"pronounciation_score",
			"naturalness_score",
			"noise_score",
			"edit_transcript",
		]

	def clean_audio_id(self):
		audio_id = self.cleaned_data.get("audio_id")
		try:
			Audio.objects.get(pk=audio_id)
		except Audio.DoesNotExist:
			raise ValidationError("Referenced audio does not exist.")
		return audio_id

