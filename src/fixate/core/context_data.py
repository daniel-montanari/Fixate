"""
This module is intended to create an interface between a test script and context data
to allow for providing a loose communication between different tests

Historically the sequencer has been used as a global dictionary which results in scripts with
complex structure and inability to run individually

How to use this module:
define requirements for context data using requires_context_items
then set and get an item using set_context_data_item and get_context_data_item

"""
import logging
import functools
from fixate.config import RESOURCES
logger = logging.getLogger(__name__)

def set_context_data_item(key, value):
    """
    Set an item in context data to value
    """
    data = RESOURCES["SEQUENCER"].context_data
    data[key] = value
    

def get_context_data_item(key):
    """
    Gets an item from context data if it exists
    """
    data = RESOURCES["SEQUENCER"].context_data
    return data[key]

class ContextItemNotFound(Exception):
    """
    The item is not available in the current context
    """

def requires_context_items(*keys):
    """
    This thing needs to doctor a TestClass, and possibly also a TestList
    to include a check that the keyed item is present in context data

    needs to be done after the init, set_up looks like a good place as it is the first thing
    the sequencer interacts with.
    Both TestClass and TestList have a set_up method

    The way this gets used is very simple, just decorate the test class with the required key
    The decorator can also be stacked which is generally good for not breaking things

    @requires_context_items("required item 1", "required item 2")
    @requires_context_items("required item 3")
    ...
    class MyTest(TestClass):
        ...

    """
    def class_decorator(cls):
        # cls is not yet an instance, it is still a type
        # store the original function to avoid recursion and allow stacking this decorator
        logger.debug(f"patching {cls} {cls.set_up}")
        original_setup = cls.set_up
        # wrap to hide our hack (but we can still tell the functions apart because they live in different spots in memory)
        @functools.wraps(original_setup)
        def set_up(self):
            logger.debug(f"running decorated set_up for {cls}")
            # check the item exists
            for key in keys:
                try:
                    get_context_data_item(key)
                except KeyError:
                    raise ContextItemNotFound(f"Item '{key}' not found in current context")
            # call the original set_up function
            logger.debug("calling set_up")
            original_setup(self)
        # nasty evil patching
        cls.set_up = set_up
        return cls
    return class_decorator
