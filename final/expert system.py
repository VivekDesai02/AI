#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 13 18:32:00 2023

@author: himanshubisht
"""

rules = [
    (["fever", "cough", "fatigue"], "You may have the flu."),
    (["rash", "fever", "joint pain"], "You may have measles."),
    (["headache", "stiff neck", "fever"], "You may have meningitis.")]


def expert_system(symptoms):
    # check each rule for a match
    for condition, conclusion in rules:
        if all(i in symptoms for i in condition):
            # return the conclusion if all conditions are met
            return conclusion
    # return a default message if no rules match
    return "I'm sorry, I cannot diagnose your condition."


symptoms = ["fever", "cough", "fatigue"]
diagnosis = expert_system(symptoms)
print(diagnosis)