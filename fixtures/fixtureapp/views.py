from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from .models import Match, Team
import datetime


class HomeView(generic.ListView):
    template_name = 'fixtureapp/home.html'
    context_object_name = 'fixtures'

    def get_queryset(self):
        """return matches except away games, order by date, next 10 only"""
        s_start = datetime.date(2021, 4, 17)
        today = datetime.date.today()
        if s_start > today:
            start = s_start
        else:
            start = today
        end = start + datetime.timedelta(days=15)
        return Match.objects.exclude(venue='A').filter(date__range=(start, end)).order_by('date')


class TeamView(generic.ListView):
    queryset = Match.objects.all().order_by('date')
    template_name = 'fixtureapp/team.html'
    context_object_name = 'fixtures'

    def get_queryset(self):
        """return all team_id team matches"""
        return Match.objects.filter(team_id=self.kwargs.get('team_id_slug')).order_by('date')

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        m = Match(team_id=self.kwargs.get('team_id_slug'))
        data['team_name'] = m.team
        return data

