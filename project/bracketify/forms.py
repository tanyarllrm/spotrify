from django import forms
from django.forms import formset_factory



# class UserChoiceForm(forms.Form):
#     def __init__(self, option1, option2, *args, **kwargs):
#         super(UserChoiceForm, self).__init__(*args, **kwargs)
#
#         # Set the choices dynamically based on the provided options
#         self.fields["choice"] = forms.ChoiceField(
#             choices=[("1", option1), ("2", option2)], widget=forms.RadioSelect(), label=""
#         )


class UserChoiceForm(forms.Form):
    # create a form with two choices passed in as arguments
    def __init__(self, option1, option2, *args, **kwargs):
        super(UserChoiceForm, self).__init__(*args, **kwargs)

        # Set the choices dynamically based on the provided options
        self.fields["user_choice"] = forms.ChoiceField(
            choices=[("L", option1), ("R", option2)], widget=forms.RadioSelect(), label=""
        )


class SongComparisonForm(forms.Form):
    CHOICES = [("1", "Song A"), ("2", "Song B")]

    preference = forms.ChoiceField(
        choices=CHOICES, widget=forms.RadioSelect(attrs={"class": "song-preference-radio"}), required=True, label=""
    )
