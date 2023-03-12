import pytest
from domain.team import Task, Person, Team

class TestPassHour:
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


    def test_that_task_moves_forward(self, team, jessie):
        jessie.assigned_task = Task('Do something')

        team.pass_hour()

        assert jessie.assigned_task.progress == jessie.skill
    
    def test_that_task_moves_forward_twice(self, team, jessie):
        jessie.assigned_task = Task('Do something')

        team.pass_hour()
        team.pass_hour()

        assert jessie.assigned_task.progress == 2*jessie.skill
    
    
    def test_that_idle_task_moves_forward_for_each_team_member(self, team, jessie, jim,john, jane):
        team.pass_hour()

        assert team.idle_time() == jessie.skill + jim.skill + john.skill + jane.skill

    def test_that_idle_task_moves_forward_twice_for_each_team_member(self, team, jessie, jim,john, jane):
        team.pass_hour()
        team.pass_hour()

        assert team.idle_time() == 2*(jessie.skill + jim.skill + john.skill + jane.skill)
    

    def test_that_shared_tasks_moves_forward_for_each_person_working(self, team, jessie, jim,john, jane):
        task = Task('Setup database')
        jim.assigned_task = task
        jane.assigned_task = task

        team.pass_hour()

        team.idle_time() ==  jessie.skill + john.skill
        task.progress == jim.skill + jane.skill
