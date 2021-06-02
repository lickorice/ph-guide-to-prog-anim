# This is the file of the current scene being worked on.
# Scenes are then archived in their respective episode folders.

from manim import *
from math import log2, e
from classes import text
from random import randint

config.background_color = "#0d121f"
config.max_files_cached = 1000

class Video(Scene):
    def construct(self):
        # chc1 = Tex("1. Experimental Technique")
        # chc2 = Tex("2. Analytical Technique").next_to(chc1, DOWN)
        # title = Tex("Two methods of analysis:").next_to(chc1, UP)
        # tx = VGroup(chc1, chc2)
        # tx.arrange(DOWN, center=False, aligned_edge=LEFT)
        # self.play(Write(title), run_time=1.0)
        # self.play(Write(tx), run_time=1.0)
        # self.wait()
        # self.play(Indicate(chc1))
        # self.wait()
        # self.play(Indicate(chc2))
        # self.wait()

        # table = Tex(r"""
        #             \begin{tabular}{c|c}
        #             Pros & Cons \\
        #             \hline
        #             Straightforward & Takes time to run \\
        #             Robust and factual & Reliant on your machine \\
        #              & \textit{Hindi ibibigay sa exam} \\
        #             \end{tabular}
        #             """)
        # title = Tex("The experimental technique").next_to(table, UP)
        # self.play(Write(VGroup(title, table)))
        # self.wait()

        # t1 = Tex(r"If you liked the video so far,").move_to(UP*0.5)
        # t2 = Tex(r"please support the channel by sharing!").next_to(t1, DOWN)
        # self.play(Write(t1))
        # self.wait()
        # self.play(Write(t2))
        # self.wait()

        # table = Tex(r"""
        #             \begin{tabular}{c|c}
        #              & Runtime \\
        #             \hline
        #             & $x$ \\
        #              \\
        #              & $y$ \\
        #              & $z$ \\
        #             \end{tabular}
        #             """)
        # table2 = Tex(r"""
        #             \begin{tabular}{c|c}
        #              & Runtime \\
        #             \hline
        #             & $x$ \\
        #              \\
        #              & $k \cdot y$ \\
        #              & $z$ \\
        #             \end{tabular}
        #             """)
        # self.play(Write(table))
        # self.wait()
        # self.play(Transform(table, table2))
        # self.wait()

        # table = Tex(r"""
        #             \begin{tabular}{c|c}
        #              & Runtime \\
        #             \hline
        #             \\ 
        #             \\
        #             & $n \cdot n \cdot c_{1}$ \\ 
        #             \\
        #             \\
        #              & $n \cdot n \cdot n \cdot c_{2}$ \\
        #             \end{tabular}
        #             """).move_to(LEFT*4)
        # eq1 = Tex(r"$\text{runtime} = n^{2}c_{1} \cdot n^{3}c_{2} $").next_to(table, DOWN+RIGHT)
        # eq2 = Tex(r"$\text{runtime} = O(n^3) $").next_to(table, DOWN+RIGHT)
        # self.play(Write(table))
        # self.wait()
        # self.play(Write(eq1))
        # self.wait()
        # self.play(Transform(eq1, eq2))
        # self.wait()

        # table = Tex(r"""
        #             \begin{tabular}{c|c}
        #              & Runtime \\
        #             \hline
        #             \\ 
        #             \\
        #             \\
        #             & $n \cdot n \cdot O(n)$ \\ 
        #             \end{tabular}
        #             """).move_to(LEFT*4)
        # eq1 = Tex(r"$\text{runtime} = n^{2}O(n)$").next_to(table, DOWN+RIGHT)
        # eq2 = Tex(r"$\text{runtime} = O(n^3) $").next_to(table, DOWN+RIGHT)
        # self.play(Write(table))
        # self.wait()
        # self.play(Write(eq1))
        # self.wait()
        # self.play(Transform(eq1, eq2))
        # self.wait()

        # table = Tex(r"""
        #             \begin{tabular}{c|c}
        #              & Runtime \\
        #             \hline
        #             \\ 
        #             \\
        #             \\
        #             & $n \cdot O(n^2)$ \\ 
        #             \end{tabular}
        #             """).move_to(LEFT*4)
        # eq1 = Tex(r"$\text{runtime} = nO(h^2) $").next_to(table, UP+RIGHT)
        # eq2 = Tex(r"$\text{runtime} = nO(1) $").next_to(table, UP+RIGHT)
        # eq3 = Tex(r"$\text{runtime} = O(n) $").next_to(table, UP+RIGHT)
        # self.play(Write(table))
        # self.wait()
        # self.play(Write(eq1))
        # self.wait()
        # self.play(Transform(eq1, eq2))
        # self.wait()
        # self.play(Transform(eq1, eq3))
        # self.wait()

        table = Tex(r"""
                    \begin{tabular}{c|c}
                    Pros & Cons \\
                    \hline
                    Also robust, relies on logic & Prone to human error \\
                    Faster to do, execution not needed &  \\
                    \textit{Binibigay sa exam} &  \\
                    \end{tabular}
                    """)
        title = Tex("The analytical technique").next_to(table, UP)
        self.play(Write(VGroup(title, table)))
        self.wait()
