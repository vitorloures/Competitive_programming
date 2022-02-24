from dataclasses import dataclass, field
import typing
from typing import List, Dict
from collections import defaultdict



@dataclass
class Contributor:
    name: str
    skills: typing.Dict[str, int]
    available_at: int = 0


@dataclass
class Project:
    name: str
    duration: int
    score: int
    best_before: int
    roles: typing.Dict[str, int]
    contributors: typing.Dict[str, Contributor] = field(default_factory=dict)


@dataclass
class InputData:
    contributors: typing.Dict[str, Contributor]
    projects: typing.Dict[str, Project]


@dataclass
class Solution:
    planned_projects: int = field(default=0)
    project_lists: List[Dict[str, List[str]]] = field(default_factory=list)


class SkillSet:
    """
    C++: {
            level : number of person with that level
          }
    """
    skills: Dict[str, Dict[int, int]]

    def __init__(self, contributors: Dict[str, Contributor]):
        self.skills = {}
        for contributor in list(contributors.values()):
            for skill, level in contributor.skills.items():
                if not self.skills.get(skill):
                    self.skills[skill] = {}
                if not self.skills[skill].get(level):
                    self.skills[skill][level] = 0
                self.skills[skill][level] += 1


def parse_input_data(raw_data: typing.List[str]) -> InputData:

    current_row = 0

    number_of_contributors, number_of_projects = map(
        int, raw_data[current_row].split(" ")
    )

    contributors: typing.Dict[str, Contributor] = {}

    for _ in range(number_of_contributors):
        current_row += 1

        row_data = raw_data[current_row].split(" ")

        name = row_data[0]
        number_of_skills = int(row_data[1])

        skills: typing.Dict[str, int] = {}

        for __ in range(number_of_skills):
            current_row += 1
            row_data = raw_data[current_row].split(" ")
            skills[row_data[0]] = int(row_data[1])

        contributors[name] = Contributor(name=name, skills=skills)

    projects: typing.Dict[str, Project] = {}

    for _ in range(number_of_projects):
        current_row += 1

        row_data = raw_data[current_row].split(" ")

        name = row_data[0]
        duration = int(row_data[1])
        score = int(row_data[2])
        best_before = int(row_data[3])
        number_of_roles = int(row_data[4])

        roles: typing.Dict[str, int] = {}

        for __ in range(number_of_roles):
            current_row += 1
            row_data = raw_data[current_row].split(" ")
            # TODO: It can not do this. Two roles with the same
            #  skill will not be accounted
            roles[row_data[0]] = int(row_data[1])

        projects[name] = Project(
            name=name,
            duration=duration,
            score=score,
            best_before=best_before,
            roles=roles,
        )

    return InputData(contributors=contributors, projects=projects)


def get_person_by_skill_and_level(skill_needed: str, level: int, contributors: typing.Dict[str, Contributor]) -> typing.Optional[Contributor]:
    for c in list(contributors.values()):
        if isinstance(c.skills.get(skill_needed), int) and c.skills.get(skill_needed) >= level:
            return c
    return None


def print_output(output, filename):
    output_filename = filename.replace("input", "output").replace(".in", ".out")
    output_string = str(output.planned_projects)+'\n'
    for project_details in output.project_lists:
        for prj_name, people in project_details.items():
            output_string += prj_name+'\n'
            output_string += " ".join(people)
            output_string += '\n'

    f = open(output_filename, "w")
    f.write(output_string)
    f.close()


def main() -> None:
    file_list = ["a_an_example.in.txt", "b_better_start_small.in.txt",
                 "c_collaboration.in.txt", "d_dense_schedule.in.txt",
                 "e_exceptional_skills.in.txt", "f_find_great_mentors.in.txt"]

    for file_name in file_list:
        file_name = "input_data/" + file_name
        with open(file_name) as file:
            raw_data = file.read().split("\n")

        data = parse_input_data(raw_data)
        # print(data)
        # print(data)

        # Resort project by some heuristic
        """for prj_name, prj in enumerate(data.projects):
            heuristic = (prj.score * prj.duration) / (prj.best_before * len(prj.roles))"""
        output = Solution()
        # skill_set = SkillSet(data.contributors)

        # print(f"\n{skill_set.skills}\n")
        for prj_name, prj in data.projects.items():
            # print(prj_name)
            skills_for_project = prj.roles
            contributors_to_work = []
            # print(f"Skills for project {skills_for_project}")
            for skill_needed, level_needed in skills_for_project.items():
                # print(f"Buscando pessoa com {skill_needed} no level {level_needed}")
                person = get_person_by_skill_and_level(skill_needed, level_needed,
                                                       data.contributors)
                if person:
                    contributors_to_work.append(person.name)
                    # print(f"Achei a pessoa: {person}")
                else:
                    contributors_to_work = []
                    # print("Ninguém nesse nível")
                    break

            if len(contributors_to_work) == len(prj.roles):
                # print(f"Bora fazer o projeto: {prj_name} com {contributors_to_work}")
                output.planned_projects += 1
                output.project_lists.append({prj_name: contributors_to_work})
        # print(output)
        print_output(output, file_name)


if __name__ == "__main__":
    main()