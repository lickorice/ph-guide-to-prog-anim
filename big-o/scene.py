# This is the file of the current scene being worked on.
# Scenes are then archived in their respective episode folders.

from manim import *
from classes import arrays
from random import randint

config.background_color = "#0d121f"
config.max_files_cached = 1000

class Video(Scene):
    def construct(self):
        sample_array = list(map(str, list(range(10))))

        bubble_array = arrays.BubbleSortArray(raw_values=sample_array, size=0.7)

        self.play(ShowCreation(bubble_array.mobject))
        self.wait()
        self.play(ShowCreation(bubble_array.mbrace))
        self.wait()
        bubble_array.sort(self, wait_time=0, run_time=0.01)
        self.wait(5.0)