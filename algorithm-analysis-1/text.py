# This is the file of the current scene being worked on.
# Scenes are then archived in their respective episode folders.

from manim import *
from classes import text
from random import randint

config.background_color = "#0d121f"
config.max_files_cached = 1000

class Video2(Scene):
    def construct(self):
        text_list = [
            # r"Given some number $K$, \\ find \textbf{the sum} of all numbers from $1$ to $K$.",
            # r"$K=10$",
            # r"$K=10$",
            # r"$1 + 2 + 3 + 4 + ... + 10$",
            # r"$55$",
            # r"Thanks for sharing! \\ \large{\textbf{Maraming salamat!}}",
            r"$\text{runtime} = x + ky + z$", 
            r"$\text{runtime} = O(1) + k \cdot O(1) + O(1)$", 
            r"$\text{runtime} = k \cdot O(1)$", 
            r"$\text{runtime} = O(k)$", 
        ]
        text.transition_all(self, text_list, transition_time=1.0)