import pytest
from domain.team import Day, Person, Team, Task

class TestProductMeeting:

    @pytest.fixture
    def jessie(self):
        return Person('Jessie Daniels', 7)
    @pytest.fixture
    def jim(self):
        return Person('Jim Daniels', 7)
    @pytest.fixture
    def john(self):
        return Person('John Daniels', 7)
    @pytest.fixture
    def jane(self):
        return Person('Jane Daniels', 7)


    @pytest.fixture
    def team(self, jessie, jim, john, jane):
        team = Team()
        team.hire(jessie)
        team.hire(jim)
        team.hire(john)
        team.hire(jane)
        return team
        
    @pytest.fixture
    def day(self, team):
        day = Day(team=team)
        return day
    
    def test_that_meeting_pm_adds_a_feature_to_work_on(self, day, team):
        day.meet_pm()

        assert len(team.features) == 1
    
    def test_that_the_team_without_a_task_is_idle(self, day, team):
        assert team.idle_time() == 0

        day.meet_pm()

        assert team.idle_time() > 0
    
    def test_that_the_team_with_a_task_makes_progress(self, day, team, jessie):
        task = Task(name='Do work')
        jessie.assigned_task = task
        assert task.progress == 0

        day.meet_pm()

        assert task.progress == jessie.skill
    
    def test_that_meeting_pm_takes_time(self, day):
        day.meet_pm()

        assert day.elapsed_hours == day.STANDARD_MEETING_LENGTH
        
    def test_that_two_meeting_take_twice_the_time(self, day):
        day.meet_pm()
        day.meet_pm()

        assert day.elapsed_hours == 2*day.STANDARD_MEETING_LENGTH
    