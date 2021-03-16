# This is the file of the current scene being worked on.
# Scenes are then archived in their respective episode folders.

from manim import *
from classes import text
from random import randint

config.background_color = "#0d121f"
config.max_files_cached = 1000

class Video(Scene):
    def construct(self):
        table = Tex(r"""
            \begin{tabular}{c| c c c}
            $n$ & $n^2$ & $n^2-n$ & \% error \\
            \hline
            10 & 100 & 90 & 10\% \\
            100 & 10,000 & 9900 & 1\% \\
            1,000 & 1,000,000 & 999,000 & 0.1\% \\
            \end{tabular}
            """)
        self.play(Write(table))
        self.wait()