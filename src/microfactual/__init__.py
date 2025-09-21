"""
MicroFactual: A user-friendly Python framework for microbiome machine learning workflows.

This package provides tools for performing interpretable microbiome machine learning
workflows based on counterfactual explanations.
"""

__version__ = "0.1.0"
__author__ = "Simeon Hebrew, Lawrence Adu-Gyamfi"
__email__ = "simeonhebrew@gmail.com, lagyamfi@outlook.com"

# Import main modules for easy access
from . import data_processing
from . import modeling
from . import utils
from . import visualisation

__all__ = [
    "data_processing",
    "modeling",
    "utils",
    "visualisation",
]
