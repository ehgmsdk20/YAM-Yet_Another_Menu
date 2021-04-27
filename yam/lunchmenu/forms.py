from django import forms

class LocChooseForm(forms.Form):
    def __init__(self,*args,**kwargs):
        self.profile = kwargs.pop('profile')
        super(LocChooseForm, self).__init__(*args,**kwargs)
        if self.profile:
            self.fields['current_location'].choices = [(self.profile.home_latlng,'Home: '+self.profile.home),
                                         (self.profile.office_latlng,'Office: '+self.profile.office)]

    current_location = forms.ChoiceField(widget=forms.RadioSelect)
    radius = forms.IntegerField(label="검색 반경(m)")