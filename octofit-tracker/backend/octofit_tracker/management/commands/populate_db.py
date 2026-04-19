from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models

from octofit_tracker import models as app_models

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        User = get_user_model()
        # Delete existing data
        User.objects.all().delete()
        app_models.Team.objects.all().delete()
        app_models.Activity.objects.all().delete()
        app_models.Leaderboard.objects.all().delete()
        app_models.Workout.objects.all().delete()

        # Create Teams
        marvel = app_models.Team.objects.create(name='Marvel')
        dc = app_models.Team.objects.create(name='DC')

        # Create Users
        tony = User.objects.create_user(username='tony', email='tony@stark.com', password='ironman', first_name='Tony', last_name='Stark', team=marvel)
        steve = User.objects.create_user(username='steve', email='steve@rogers.com', password='captain', first_name='Steve', last_name='Rogers', team=marvel)
        bruce = User.objects.create_user(username='bruce', email='bruce@wayne.com', password='batman', first_name='Bruce', last_name='Wayne', team=dc)
        clark = User.objects.create_user(username='clark', email='clark@kent.com', password='superman', first_name='Clark', last_name='Kent', team=dc)

        # Create Activities
        app_models.Activity.objects.create(user=tony, type='Run', duration=30, calories=300)
        app_models.Activity.objects.create(user=steve, type='Swim', duration=45, calories=400)
        app_models.Activity.objects.create(user=bruce, type='Cycle', duration=60, calories=500)
        app_models.Activity.objects.create(user=clark, type='Yoga', duration=50, calories=250)

        # Create Workouts
        app_models.Workout.objects.create(name='Morning Cardio', description='Cardio workout for all', suggested_for=marvel)
        app_models.Workout.objects.create(name='Strength Training', description='Strength workout for all', suggested_for=dc)

        # Create Leaderboard
        app_models.Leaderboard.objects.create(team=marvel, points=700)
        app_models.Leaderboard.objects.create(team=dc, points=750)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
