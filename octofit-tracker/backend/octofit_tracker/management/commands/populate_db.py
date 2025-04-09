from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = "Populate the octofit_db database with test data"

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Add test data for users
        users = [
            {"username": "alice", "email": "alice@example.com"},
            {"username": "bob", "email": "bob@example.com"},
        ]
        for user_data in users:
            User.objects.create(**user_data)

        # Add test data for teams
        teams = [
            {"name": "Team Octopus", "description": "The best team in Merington"},
            {"name": "Team Kraken", "description": "Rivals of Team Octopus"},
        ]
        for team_data in teams:
            Team.objects.create(**team_data)

        # Add test data for activities
        activities = [
            {"name": "Swimming", "calories_burned_per_minute": 12},
            {"name": "Yoga", "calories_burned_per_minute": 5},
        ]
        for activity_data in activities:
            Activity.objects.create(**activity_data)

        # Add test data for leaderboard
        leaderboard_entries = [
            {"user_id": 1, "team_id": 1, "points": 150},
            {"user_id": 2, "team_id": 2, "points": 120},
        ]
        for entry in leaderboard_entries:
            Leaderboard.objects.create(**entry)

        # Add test data for workouts
        workouts = [
            {"user_id": 1, "activity_id": 1, "duration_minutes": 40},
            {"user_id": 2, "activity_id": 2, "duration_minutes": 60},
        ]
        for workout_data in workouts:
            Workout.objects.create(**workout_data)

        self.stdout.write(self.style.SUCCESS("Test data successfully populated!"))
