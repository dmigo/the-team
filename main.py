from dataclasses import dataclass
from domain.team import Team, Day, Feature, Person
from typing import List
from time import sleep


PROMPT = """
How would you like to spend the next hour?
The options are:
1. Meet the PM
2. Plan the next available feature
3. Assign tasks
4. Just work in peace
"""

@dataclass
class TeamReporter:
    team: Team

    def report(self):
        print(f"## Current team ##")
        for member in self.team.members:
            print(f'\t{member.name}\t[skill: {member.skill}]')
        print("")
        features_reporter = FeaturesReporter(features=self.team.features)
        features_reporter.report()
        print("")
        print("## Current idleness ##")
        print("")
        print(self.team.idle_time())
        print("")



@dataclass
class FeaturesReporter:
    features: List[Feature]

    def report(self):
        print(f'### Current work in progress ###')
        for feature in self.features:
            print("")
            print(f'\t {feature.name}\t[{len(feature.tasks)}]')
            for task in feature.tasks:
                print(f'\t {task.name}\t[{task.complexity} {task.progress}]')

@dataclass
class DayReporter:
    day: Day

    def report(self):
        print(f"# DAY {self.day.number} {self.day.current_time()} #")
        print("")
        team_reporter = TeamReporter(team=self.day.team)
        team_reporter.report()

            

def setup_game()-> Day:
    jessie = Person('Jessie Daniels', 7)
    jim = Person('Jim Daniels', 13)
    john = Person('John Daniels', 5)
    jane = Person('Jane Daniels', 21)

    team = Team()
    team.hire(jessie)
    team.hire(jim)
    team.hire(john)
    team.hire(jane)

    day = Day(team =team)

    return day

def main_loop():
    day = setup_game()
    p0 = day.team.members[0]
    p1 = day.team.members[1]
    p2 = day.team.members[2]
    p3 = day.team.members[3]

    print(PROMPT)
    print("")
    sleep(3)
    reporter = DayReporter(day=day)
    sleep(3)
    day.meet_pm()
    reporter.report()
    sleep(3)
    day.plan()
    reporter.report()
    t1 = day.team.features[0].tasks[0]
    t2 = day.team.features[0].tasks[1]
    p0.assigned_task = t1
    p1.assigned_task = t1
    p2.assigned_task = t1
    p3.assigned_task = t2
    sleep(3)
    day.work()
    reporter.report()
    sleep(10)

if __name__ =="__main__":
    main_loop()
