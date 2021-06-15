""" Used as a control structure when used after with keyword"""
# Context manager - A pyhton object that is able to act as a control structure when used after the with statement
# Setup try
# Handoff control - Yield
# wrap-up - finally

# basic contextmanager framework
"""
@contextmanager
def simple_context_manager(obj):
    try:
        #do something
        yield
    finally:
        #wrap up
"""

# increments some_property by 1

from contextlib import contextmanager

@contextmanager
def simple_context_manager(obj):
    try:
        obj.some_property += 1
        yield
    finally:
        obj.some_property -= 1