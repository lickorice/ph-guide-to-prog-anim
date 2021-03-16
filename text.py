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
            # r"Then, what arrangement of numbers would lead\\ to the \textbf{most} number of checks?"
            # r"Which is more important to us?\\The \textbf{best-case} or the \textbf{worst-case} runtime?",
            # r"The \textbf{worst-case} runtime is usually considered.",
            # r"First, we could better understand an algorithm when it\\performs at its worst.",
            # r"Second, it can't get any worse than that.\\(\textit{Sagad na.})",
            # r"Third, the average case usually tends to the worst case.",
            # r'Big O notation\\"Big" for uppercase\\"O" for \text{order of complexity}',
            # r"Bubble sort's worst-case \textbf{time complexity}:\\ \Large{$O(n^2)$}",
            # r"\textit{Teka, Carlos. Anyare sa $-n$ sa $n^2-n$?}",
            # r"Let's work through an example.",
            # r'$n^2-n$ \textbf{behaves like} $n^2$ with a big enough input—\\Therefore, it is $O(n^2)$.',
            # r"Now, here's an important question: which is faster?\\$O(n)$ or $O(n^2)$?",
            # r"It actually depends! But we know that\\$O(n^2)$ is slower in the long run.",
            # r"Take for example two algorithms with time complexities\\$100n$ and $n^2$.",
            # r"The \textbf{growth rate} of $n^2$ is larger than $100n$.",
            # r"$n^2$ is $O(n^2)$ and $100n$ is $O(n)$,\\but $n^2$ can still be faster at smaller input sizes.",
            # r"Therefore, big O notation describes only the \textbf{growth rate},\\but not necessarily the runtime.",
            # r"Time complexities aren't limited by $n^x$ terms.",
            # r"Merge sort, for example, has $O(n\log{n})$ complexity,\\ which is faster than bubble sort.",
            # r"Worst-case: Big O ($O(x)$)",
            # r"Best-case: Omega ($\Omega(x)$)",
            # r"Average-case: Theta ($\Theta(x)$)",
            r"Time complexity concerns itself with \textbf{running time}.",
            r"Space complexity concerns itself\\ with \textbf{consumed memory} (RAM)",
        ]
        text.transition_all(self, text_list, transition_time=1.0)