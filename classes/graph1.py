# This is the file of the current scene being worked on.
# Scenes are then archived in their respective episode folders.

from manim import *
from classes import text
from random import randint

config.background_color = "#0d121f"
config.max_files_cached = 1000

class Video(GraphScene):
    
    def __init__(self, **kwargs):
        GraphScene.__init__(
            self,
            y_max=100,
            x_max=10,
            x_min=0,
            y_min=0,
            y_axis_config={"tick_frequency": 10},
            x_axis_label="$n$",
            y_axis_label="time",
            axes_color=WHITE,
            y_label_position=UP+LEFT,

            graph_origin=3 * DOWN + 4 * LEFT,

            y_labeled_nums=np.array([50, 100]),
            x_labeled_nums=np.array([5, 10]),
            **kwargs
        )

    def construct(self):
        self.setup_axes()
        self.wait()
        curve1 = self.get_graph(lambda x: x*x, x_min=0)
        curve2 = self.get_graph(lambda x: (x*x) - x, x_min=0)
        label1 = self.get_graph_label(curve1, "n^2", direction=UP+LEFT, x_val=5)
        label2 = self.get_graph_label(curve2, "n^2-n", direction=DOWN+RIGHT, x_val=6)
        line1 = self.get_vertical_line_to_graph(5, curve1, DashedLine, color=YELLOW)
        line2 = self.get_vertical_line_to_graph(10, curve1, DashedLine, color=YELLOW)
        self.play(ShowCreation(VGroup(curve1, curve2, label1, label2)))
        self.wait()
