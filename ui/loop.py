from rich.console import Console
from dataclasses import dataclass
from domain.team import Team, Day, Feature
from typing import List
from time import sleep

console = Console()

RULES = """
How would you like to spend the next hour?
The options are:
1. Meet the PM
2. Plan the next available feature
3. Assign tasks
4. Just work in peace
q. For quit
"""
PROMPT = """
What do you do now?
"""


@dataclass
class TeamReporter:
    team: Team

    def report(self):
        console.print(f"## Current team ##")
        for member in self.team.members:
            console.print(f"\t{member.name}\t[skill: {member.skill}]")
        console.print("")
        features_reporter = FeaturesReporter(features=self.team.features)
        features_reporter.report()
        console.print("")
        console.print("## Current idleness ##")
        console.print("")
        console.print(self.team.idle_time())
        console.print("")


@dataclass
class FeaturesReporter:
    features: List[Feature]

    def report(self):
        console.print(f"### Current work in progress ###")
        for feature in self.features:
            console.print("")
            console.print(f"\t {feature.name}\t[{len(feature.tasks)}]")
            for task in feature.tasks:
                console.print(f"\t {task.name}\t[{task.complexity} {task.progress}]")


@dataclass
class DayReporter:
    day: Day

    def report(self):
        console.print("")
        console.print(
            f"# DAY {self.day.number} {self.day.current_time()} #", style="bold"
        )
        console.print("")
        team_reporter = TeamReporter(team=self.day.team)
        team_reporter.report()


def ellipsis(text: str = ""):
    with console.status(text, spinner="aesthetic"):
        sleep(2)


class MainLoop:
    day: Day
    reporter: DayReporter

    def __init__(self, day: Day) -> None:
        self.day = day
        self.reporter = DayReporter(day=self.day)

    def run(self):
        console.print(RULES)

        while True:
            action = input(PROMPT)
            if action == "1":
                self.day.meet_pm()
                self.reporter.report()
                ellipsis("Meeting the PM ")
            elif action == "2":
                self.day.plan()
                self.reporter.report()
                ellipsis("Planning the next feature")
            elif action == "3":
                t1 = self.day.team.features[0].tasks[0]
                t2 = self.day.team.features[0].tasks[1]
                self.day.team.members[0].assigned_task = t1
                self.day.team.members[1].assigned_task = t1
                self.day.team.members[2].assigned_task = t1
                self.day.team.members[3].assigned_task = t2
            elif action == "4":
                self.day.work()
                self.reporter.report()
                ellipsis("Everyone is working hard")
            elif action == "q":
                # TODO calculate score
                console.print("Fare well!", style="bold")
                break
            else:
                console.print("No such action", style="bold")
