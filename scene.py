# This is the file of the current scene being worked on.
# Scenes are then archived in their respective episode folders.

from manim import *
from math import log2, e
from classes import text
from random import randint

config.background_color = "#0d121f"
config.max_files_cached = 1000

class Video2(GraphScene):
    
    def __init__(self, **kwargs):
        GraphScene.__init__(
            self,
            y_max=10000,
            x_max=100,
            x_min=1,
            y_min=0,
            y_axis_config={"tick_frequency": 1000, "include_ticks": False},
            x_axis_config={"tick_frequency": 1000},
            x_axis_label="$n$",
            y_axis_label="time",
            axes_color=WHITE,
            y_label_position=UP+LEFT,

            graph_origin=3 * DOWN + 4 * LEFT,

            **kwargs
        )

    def construct(self):
        self.setup_axes()
        self.wait()
        curves = [
            self.get_graph(lambda x: 50*x, x_min=1),
            self.get_graph(lambda x: x*x, x_min=1),
            self.get_graph(lambda x: x*x*x, x_min=1, x_max=22),
            self.get_graph(lambda x: 850*log2(x), x_min=1),
        ]
        raw_labels = [
            "O(n)", "O(n^2)", "O(n^3)", r"O(\log{n})",
        ]
        x_vals = [80, 90, 20, 75, 50]
        directions = [UP+LEFT for i in range(5)]
        directions[2] = LEFT
        directions[1] = RIGHT
        directions[0] = UP
        labels = [self.get_graph_label(curves[i], raw_labels[i], direction=directions[i], x_val=x_vals[i]) for i in range(len(curves))]
        self.play(ShowCreation(VGroup(*curves[:3], *labels[:3])))
        self.wait()
        self.play(ShowCreation(VGroup(*curves[3:], *labels[3:])))
        self.wait()
