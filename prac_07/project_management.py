"""
Project management program for tracking projects and their details.
Estimate: 3 hours
Time Taken: Around 4 hours (split over a few days) - still not finished
"""
import datetime
from project import Project

MENU = """- (L)oad projects 
- (S)ave projects 
- (D)isplay projects 
- (F)ilter projects by date
- (A)dd new project 
- (U)pdate project
- (Q)uit"""
FILENAME = "projects.txt"


def main():
    """Main program for project management."""
    print("Welcome to Pythonic Project Management")
    projects = load_projects(FILENAME)
    print(f"Loaded {len(projects)} projects from {FILENAME}")
    print(MENU)

    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "l":
            filename = input("Filename to load from: ")
            projects = load_projects(filename)
        elif choice == "s":
            filename = input("Filename to save to: ")
            save_projects(filename, projects)
        elif choice == "d":
            display_projects(projects)
        elif choice == "f":
            filter_projects_by_date(projects)
        elif choice == "a":
            add_new_project(projects)
        elif choice == "u":
            update_project(projects)
        else:
            print("Invalid choice")

        print(MENU)
        choice = input(">>> ").lower()

    save_choice = input(f"Would you like to save to {FILENAME}? ").lower()
    if save_choice.startswith("y"):
        save_projects(FILENAME, projects)
    print("Thank you for using custom-built project management software.")


def load_projects(filename):
    projects = []
    with open(filename) as file:
        file.readline()
        for line in file:
            parts = line.strip().split('\t')
            project = Project(parts[0], parts[1], int(parts[2]), float(parts[3]))
            projects.append(project)
    return projects


def save_projects(filename, projects):
    with open(filename, 'w') as file:
        print("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage", file=file)
        for project in projects:
            print(f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t"
                  f"{project.priority}\t{project.cost_estimate}\t{project.completion_percentage}")


def display_projects(projects):
    incomplete = [project for project in projects if not project.is_complete()]
    complete = [project for project in projects if project.is_complete()]

    print("Incomplete projects:")
    for project in sorted(incomplete):
        print(f" {project}")

    print("Completed projects:")
    for project in sorted(complete):
        print(f" {project}")


def filter_projects_by_date(projects):
    date_string = input("Show projects that start after date (dd/mm/yy): ")
    date = datetime.datetime.strptime(date_string, "%d/%m/%y").date()
    filtered_projects = [project for project in projects if project.start_date > date]

    for project in sorted(filtered_projects):
        print(project)


def add_new_project(projects):
    print("Let's add a new project")
    name = input("Name: ")
    date_string = input("Start date (dd/mm/yy): ")
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: $"))
    percent_complete = int(input("Percent complete: "))


def update_project(projects):
    for i, project in enumerate(projects):
        print(f"{i} {project}")

    choice = int(input("Project choice: "))
    project = projects[choice]
    print(project)

    new_percentage = input("New Percentage: ")
    new_priority = input("New Priority: ")
    project.update(new_percentage, new_priority)


main()
