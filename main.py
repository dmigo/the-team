import click
from dataclasses import dataclass
from domain.team import Team, Day, Feature, Person
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


def setup_game() -> Day:
    jessie = Person("Jessie Daniels", 7)
    jim = Person("Jim Daniels", 13)
    john = Person("John Daniels", 5)
    jane = Person("Jane Daniels", 21)

    team = Team()
    team.hire(jessie)
    team.hire(jim)
    team.hire(john)
    team.hire(jane)

    day = Day(team=team)

    return day


def ellipsis():
    sleep(1)
    click.echo(".")
    sleep(1)
    click.echo(".", end="")
    sleep(1)
    click.echo(".", end="")


def main_loop():
    day = setup_game()
    p0 = day.team.members[0]
    p1 = day.team.members[1]
    p2 = day.team.members[2]
    p3 = day.team.members[3]

    reporter = DayReporter(day=day)
    click.echo(RULES)

    while True:
        action = input(PROMPT)
        if action == "1":
            day.meet_pm()
            reporter.report()
        elif action == "2":
            day.plan()
            reporter.report()
        elif action == "3":
            t1 = day.team.features[0].tasks[0]
            t2 = day.team.features[0].tasks[1]
            p0.assigned_task = t1
            p1.assigned_task = t1
            p2.assigned_task = t1
            p3.assigned_task = t2
        elif action == "4":
            day.work()
            reporter.report()
        elif action == "q":
            # TODO calculate score
            click.secho("Fare well!", bold=True)
            break
        else:
            click.secho("No such action", bold=True)


if __name__ == "__main__":
    main_loop()
