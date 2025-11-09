"""
Project management program for tracking projects and their details.
Estimate: 3 hours
Time Taken:
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
print(MENU)


def main():
    """Main program for project management."""
    print("Welcome to Pythonic Project Management")
    projects = load_projects(FILENAME)
    print(f"Loaded {len(projects)} projects from {FILENAME}")

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


    save_choice = input(f"Would you like to save to {FILENAME}? ")
    if save_choice.lower() != ["no", "n", "no, i think not."]:
        save_projects(FILENAME, projects)
    print("Thank you for using custom-built project management software.")


def load_projects(filename):


def save_projects(filename, projects):


def display_projects(projects):



def filter_projects_by_date(projects):



def add_new_project(projects):



def update_project(projects):

