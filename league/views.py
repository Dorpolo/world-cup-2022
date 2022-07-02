from django.http import HttpResponse
from django.shortcuts import render, redirect

from league.forms import LeagueForm, LeagueMemberForm
from league.models import League, LeagueMember


class LeagueDataClient:
    def __init__(self, request):
        self.request = request

    @staticmethod
    def get_league_id(pk):
        return League.objects.get(pk=pk)

    @staticmethod
    def get_league_members(league_id):
        return LeagueMember.objects.filter(league=league_id)


def my_leagues(request) -> HttpResponse:
    leagues = League.objects.all()
    league_meta_data = [
        {
            'members': LeagueMember.objects.filter(league__id=k.id),
            'owner': k.owner,
            'name': k.name,
            'logo': k.logo,
        } for k in leagues
    ]

    return render(
        request=request,
        template_name='league/league_zone.html',
        context={
            'leagues': leagues,
            'league_meta_data': league_meta_data,
        }
    )


class LeagueBuilder:
    def __init__(self):
        self.context = {
            'data': {'some_data': 'some_data'}
        }
        self.template_name = 'league/league_builder.html'

    def create(self, request) -> HttpResponse:
        form = LeagueForm()
        if request.method == 'POST':
            form = LeagueForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('/league-zone/')
        return render(
            request=request,
            template_name=self.template_name,
            context=dict(**self.context, form=form)
        )

    def update(self, request, pk) -> HttpResponse:
        prediction = League.objects.get(id=pk)
        form = LeagueForm(instance=prediction)
        if request.method == 'POST':
            form = LeagueForm(request.POST, request.FILES, instance=prediction)
            if form.is_valid():
                form.save()
                return redirect('/league-zone/')
        return render(
            request=request,
            template_name=self.template_name,
            context=dict(**self.context, form=form)
        )


class LeagueMembership:
    def __init__(self):
        self.context = {
            'data': {
                'some_data': 'some_data',
            }
        }
        self.template_name = 'league/league_membership.html'

    def create(self, request) -> HttpResponse:
        form = LeagueMemberForm()
        if request.method == 'POST':
            form = LeagueMemberForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('/league-zone')
        return render(
            request=request,
            template_name=self.template_name,
            context=dict(**self.context, form=form)
        )

    def update(self, request, pk) -> HttpResponse:
        prediction = LeagueMember.objects.get(id=pk)
        form = LeagueMemberForm(instance=prediction)
        if request.method == 'POST':
            form = LeagueMemberForm(request.POST, request.FILES, instance=prediction)
            if form.is_valid():
                form.save()
                return redirect('/')
        return render(
            request=request,
            template_name=self.template_name,
            context=dict(**self.context, form=form)
        )