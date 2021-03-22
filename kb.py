# this file will contain the knowledge base of the system
"""
This file houses the knowledge base of the system.

The knowledge base contains ingredients as well as tags/descriptors to help the system perform generalization for particular ingredients

Ingredients are housed in the knowledge base as key-value pairs in a python dictionary wherein:
    * the keys are the name of a particular ingredient
    * the value is a Lisp-like list that houses different attributes/generalizations of said ingredient
"""




DB = {
        "ingredients": dict(),
        "adjacency-list": dict()
        }
