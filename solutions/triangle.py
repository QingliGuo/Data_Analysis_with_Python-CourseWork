#!/usr/bin/env python3
import numpy as np

__doc__ = """Calculte hypothenuse and area of right-angled triangle with two known sides"""

__author__ = "Super Star"
__version__ = "Beta v-0.1"

def hypothenuse(side1,side2):
    """Calculte the hypothenuse"""
    return np.sqrt(side1 ** 2.0 + side2 ** 2.0)

def area (side1,side2):
    """Calculte the area"""
    return side1 * side2 / 2.0
