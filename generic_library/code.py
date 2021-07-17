# Databricks notebook source
import numpy as np
import pandas as pd


class SomeClass(object):
    """Basic Class documentation
    
    This is a brief description of the class.

    Parameters
    ----------
    parameter1 : str
        description of param: \n
        \t extra info \n
        \t formatted here \n
        \t to look nice

    parameter2 : int, optional
        description; defaults to 10

    Returns
    -------
    generic_library.SomeClass
        An initialized SomeClass with description.
    """

    def __init__(self, parameter1, parameter2=10):
        """see class docstring"""
        pass

    def _private_method(self, gt_relevance):
        """
        In a pinch, no need to doc a private method
        this method won't get autodoc'd.
        """
        pass

    def public_method(self, parameter1):
        """example for public method docstring

        Parameters
        ----------
        parameter1 : str
            description of param, a string

        Returns
        -------
        str
            a string
        
        """
        pass

def some_func(arg):    
    """some little function

    A description of the function

    Parameters
    ----------
    arg : int
        an integer

    Returns
    -------
    None
    """

    pass