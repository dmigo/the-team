import click
from dataclasses import dataclass
from domain.team import Team, Day, Feature
from typing import List
from time import sleep


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
        click.echo(f"## Current team ##")
        for member in self.team.members:
            click.echo(f"\t{member.name}\t[skill: {member.skill}]")
        click.echo("")
        features_reporter = FeaturesReporter(features=self.team.features)
        features_reporter.report()
        click.echo("")
        click.echo("## Current idleness ##")
        click.echo("")
        click.echo(self.team.idle_time())
        click.echo("")


@dataclass
class FeaturesReporter:
    features: List[Feature]

    def report(self):
        click.echo(f"### Current work in progress ###")
        for feature in self.features:
            click.echo("")
            click.echo(f"\t {feature.name}\t[{len(feature.tasks)}]")
            for task in feature.tasks:
                click.echo(f"\t {task.name}\t[{task.complexity} {task.progress}]")


@dataclass
class DayReporter:
    day: Day

    def report(self):
        click.echo("")
        click.secho(f"# DAY {self.day.number} {self.day.current_time()} #", bold=True)
        click.echo("")
        team_reporter = TeamReporter(team=self.day.team)
        team_reporter.report()


def ellipsis():
    sleep(1)
    click.echo(".")
    sleep(1)
    click.echo(".", end="")
    sleep(1)
    click.echo(".", end="")


class MainLoop:
    day: Day
    reporter: DayReporter

    def __init__(self, day: Day) -> None:
        self.day = day
        self.reporter = DayReporter(day=self.day)

    def run(self):
        click.echo(RULES)

        while True:
            action = input(PROMPT)
            if action == "1":
                self.day.meet_pm()
                self.reporter.report()
            elif action == "2":
                self.day.plan()
                self.reporter.report()
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
            elif action == "q":
                # TODO calculate score
                click.secho("Fare well!", bold=True)
                break
            else:
                click.secho("No such action", bold=True)
