from domain.team import Team, Day, Person
from ui.loop import MainLoop


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


if __name__ == "__main__":
    day = setup_game()
    loop = MainLoop(day=day)
    loop.run()
