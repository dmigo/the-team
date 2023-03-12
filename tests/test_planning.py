import pytest
from domain.team import Day, Person, Team, Task, Feature

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
    def feature(self):
        initial_task = Task(name="This is the initial task")
        feature =  Feature(name = 'Mock feature', tasks = [initial_task])
        return feature

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
    
    def test_that_feature_gets_split(self, day,feature, team):
        team.features.append(feature)
        assert len(feature.tasks) == 1

        day.plan()

        assert len(feature.tasks) > 1
    
    def test_that_feature_gets_split_twice(self, day, feature, team):
        team.features.append(feature)
        assert len(feature.tasks) == 1

        day.plan()

        assert len(feature.tasks) == 2

        day.plan()

        assert len(feature.tasks) == 4
    
    def test_that_the_team_is_not_idle(self, day, feature, team):
        team.features.append(feature)

        day.plan()

        assert team.idle_time() == 0
    
    def test_that_planning_takes_time(self, day, feature, team):
        team.features.append(feature)

        day.plan()

        assert day.elapsed_hours==1
    
    def test_that_two_plannings_take_twice_the_time(self, day, feature, team):
        team.features.append(feature)

        day.plan()
        day.plan()

        assert day.elapsed_hours==2



