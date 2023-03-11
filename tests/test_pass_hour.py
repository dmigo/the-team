import pytest
from domain.team import Task, Person, Team

class TestPassHour:
    def test_that_task_moves_forward(self):
        team = Team()
        jessie = Person('Jessie Daniels', 10)
        team.hire(jessie)
        jessie.assigned_task = Task('Do something')

        team.pass_hour()

        assert jessie.assigned_task.progress == jessie.skill
    
    def test_that_task_moves_forward_twice(self):
        team = Team()
        jessie = Person('Jessie Daniels', 10)
        team.hire(jessie)
        jessie.assigned_task = Task('Do something')

        team.pass_hour()
        team.pass_hour()

        assert jessie.assigned_task.progress == 2*jessie.skill
    
    def test_that_idle_task_moves_forward(self):
        team = Team()
        jessie = Person('Jessie Daniels', 10)
        team.hire(jessie)

        team.pass_hour()

        assert team.idle_time() == jessie.skill
    
    def test_that_idle_task_moves_forward_for_each_team_member(self):
        team = Team()
        jessie = Person('Jessie Daniels',  7)
        team.hire(jessie)
        jim = Person('Jim Daniels',  5)
        team.hire(jim)
        john = Person('John Daniels',  11)
        team.hire(john)
        jane = Person('Jane Daniels', 13)
        team.hire(jane)

        team.pass_hour()

        assert team.idle_time() == jessie.skill + jim.skill + john.skill + jane.skill
    

    def test_that_shared_tasks_moves_forward_for_each_person_working(self):
        team = Team()
        jessie = Person('Jessie Daniels',  7)
        team.hire(jessie)
        jim = Person('Jim Daniels',  5)
        team.hire(jim)
        john = Person('John Daniels',  11)
        team.hire(john)
        jane = Person('Jane Daniels', 13)
        team.hire(jane)
        task = Task('Setup database')
        jim.assigned_task = task
        jane.assigned_task = task

        team.pass_hour()

        team.idle_time() ==  jessie.skill + john.skill
        task.progress == jim.skill + jane.skill
