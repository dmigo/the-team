import enum
import logging
from typing import Optional, List

from dataclasses import dataclass
from pathlib import Path

logger = logging.getLogger(__name__)


@enum.unique
class Complexity(enum.Enum):
    S = 1
    M = 2
    L = 3
    XL = 4
    UNKNOWN = 5

@dataclass
class Task:
    name: str
    progress: int = 0
    complexity: Complexity = Complexity.UNKNOWN

    def __init__(self, name: str):
        self.name = name

    def make_progress(self, score: int):
        self.progress += score

@dataclass
class Feature:
    name: str
    tasks: List[Task]

@dataclass
class Person:
    name: str
    skill: int
    team: Optional = None
    bio: Optional[str] = None
    avatar_path: Optional[Path] = None
    
    assigned_task: Optional[Task] = None

    def __init__(self, name: str, skill:int, bio: Optional[str]=None):
        self.skill = skill
        self.name = name
        self.bio = bio

    def pass_hour(self):
        if not self.team:
            raise Exception(f"{self.name} has no team assigned. Can't pass_hour.")

        score = self.skill

        if self.assigned_task:
            self.assigned_task.make_progress(score)
        else:
            self.team.idle_task.make_progress(score)


@dataclass
class Team:
    members: List[Person]
    idle_task: Task
    features: List[Feature]

    def __init__(self):
        self.members = []
        self.features = []
        self.idle_task = Task('Rest')

    def hire(self, person: Person):
        if person.team:
            raise Exception(f"{person.name} has a team already")

        person.team = self
        self.members.append(person)

    def pass_hour(self):
        for member in self.members:
            member.pass_hour()
    
    def idle_time(self):
        return self.idle_task.progress

@dataclass
class Activity:
    def do(self):
        pass

class Planning(Activity):
    def do(self, feature: Feature) -> List[Task]:
        """Breaks down a feature into a list of smaller tasks

        :param feature: a feature that we want to plan and break down
        :return: new list of tasks, that are the same tasks but better defined
        """
        result = []
        for task in feature.tasks:
            subtasks = task.break_down()
            result.append_many(subtasks)

        return subtasks

class ProductMeeting(Activity):
    def do(self) -> Feature:
        """Meet your PM, prepare a new feature for your team to work on

        :return: a newly planned feature
        """
        initial_task = Task('We need some task factory')
        feature = Feature(name="We need some features factory", tasks=[initial_task])
        return feature



@dataclass
class Day:
    team: Team

    def plan(self):
        feature = self.team.features.pop()
        planning = Planning()

        new_tasks = planning.do(feature)
        feature.tasks = new_tasks

        self.team.features.append(feature)

    def meet_pm(self):
        product_meeting = ProductMeeting()
        new_feature = product_meeting.do()

        self.team.features.append(new_feature)
        self.team.pass_hour()

    def work(self):
        self.team.pass_hour()

