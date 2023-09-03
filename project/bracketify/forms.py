from django import forms


class UserChoiceForm(forms.Form):
    def __init__(self, option1, option2, *args, **kwargs):
        super(UserChoiceForm, self).__init__(*args, **kwargs)

        # Set the choices dynamically based on the provided options
        self.fields['choice'] = forms.ChoiceField(
            choices=[(1, option1), (2, option2)],
            widget=forms.RadioSelect
        )
