from django.forms import ModelForm
from .models import League, LeagueMember


class LeagueForm(ModelForm):
    class Meta:
        model = League
        fields = '__all__'


class LeagueMemberForm(ModelForm):
    class Meta:
        model = LeagueMember
        fields = '__all__'