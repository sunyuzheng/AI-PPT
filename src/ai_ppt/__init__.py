"""AI-PPT package.

This package provides helpers for rapidly producing presentation outlines
and PowerPoint slides with the help of AI systems.
"""

from .main import PresentationPlan, generate_presentation, main

__all__ = [
    "PresentationPlan",
    "generate_presentation",
    "main",
]
