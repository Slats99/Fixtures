from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Match(models.Model):
    VENUES = (
        ('T', 'Abbeydale Top Pitch'),
        ('B', 'Abbeydale Bottom Pitch'),
        ('D', 'Dronfield Woodhouse'),
        ('A', 'Away')
    )
    date = models.DateField()
    time = models.TimeField()
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    opposition = models.CharField(max_length=30)
    venue = models.CharField(max_length=1, choices=VENUES)
    notes = models.CharField(max_length=100, default="", blank=True)

    def __str__(self):
        return f"{self.date}: {self.team} v {self.opposition}"
