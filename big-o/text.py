# This is the file of the current scene being worked on.
# Scenes are then archived in their respective episode folders.

from manim import *
from classes import text
from random import randint

config.background_color = "#0d121f"
config.max_files_cached = 1000

class Video(Scene):
    def construct(self):
        text_list = [
            # r"Let's count how many times the sorting algorithm\\ does \textbf{comparisons}.",
            # r"An operation by an algorithm is \textbf{NOT} free.",
            # r"This includes accessing and manipulating variables,\\ doing comparisons, etc.",
            # r"Each operation takes up \textbf{time}.",
            # r"So, what arrangement of numbers would lead\\ to the \textbf{least} number of checks?"
            r"Then, what arrangement of numbers would lead\\ to the \textbf{most} number of checks?"
        ]
        text.transition_all(self, text_list, transition_time=1.0)