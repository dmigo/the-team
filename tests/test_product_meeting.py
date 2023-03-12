import pytest
from domain.team import Day, Person, Team

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
    