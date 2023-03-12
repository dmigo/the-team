import pytest
from domain.team import Day, Person, Team

class TestPlanning:

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
    
