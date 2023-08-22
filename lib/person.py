#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__(self, name = "Jane", job = "Admin"):
        if type(name) == str and 1 <= len(name) <=25 and name != "":
            self._name = name.title()
        else:
            print("Name must be string between 1 and 25 characters.") 

        if job not in APPROVED_JOBS:
            print("Job must be in list of approved jobs.")
        
        else:
            self._job = job

    def get_name(self):
        return self._name
    
    def set_name(self, new_name):
        if type(new_name) == str and 1 <= len(new_name) <=25 and new_name != "":
            self._name = new_name

        else:
            print("Name must be string between 1 and 25 characters.")

    def get_job(self):
        return self._job
    
    def set_job(self, new_job):
        if type(new_job) == str and 1<= len(new_job) <=25 and new_job != "":
            self._job = new_job

        else:
            print("Name must be string between 1 and 25 characters.")

    name = property(get_name, set_name)
    job = property(get_job, set_job)