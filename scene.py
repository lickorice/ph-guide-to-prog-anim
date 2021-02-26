# This is the file of the current scene being worked on.
# Scenes are then archived in their respective episode folders.

from manim import *
from random import randint

config.background_color = "#0d121f"

class Video(Scene):
    def construct(self):
        # title_card = Tex(r"Let's grow up from this analogy.").move_to(3*DOWN)
        # title_card = Tex(r"Why do arrays start at 0? - Kaka-computer Mo 'Yan! \#0").move_to(3*DOWN)
        # title_card = Tex(r"\texttt{my\_array[7]}")
        # title_1 = Tex(r"*(\texttt{my\_array +(} (size of element in bytes) \texttt{* 7)})")
        # title_card = Tex(r"\texttt{malloc(} size in bytes \texttt{})}")
        # title_1 = Tex(r"Manually allocate \textit{contiguous} bytes in memory").next_to(title_card, DOWN)
        # title_2 = Tex(r"Returns a \textbf{pointer} to the first byte")
        # title_card = Tex(r"\texttt{sizeof(} data type \texttt{})}")
        # title_1 = Tex(r"Returns the \textbf{size of the type in bytes} (\texttt{int})").next_to(title_card, DOWN)
        # title_card = Tex(r"\texttt{void * =} 32 bits (4 bytes)").move_to(1.5*UP)
        # title_1 = Tex(r"\texttt{char * =} 32 bits (4 bytes)").next_to(title_card, DOWN)
        # title_2 = Tex(r"\texttt{int * =} 32 bits (4 bytes)").next_to(title_1, DOWN)
        # title_3 = Tex(r"Any pointer = 32 bits (4 bytes)").next_to(title_2, DOWN)
        # title_1 = Tex(r"Pointer to \texttt{int} (\texttt{int*})").move_to(UP*0.75)
        # title_2 = Tex(r"Array of (Array of \texttt{int}s)").move_to(DOWN*0.75)
        # title_card = Tex(r"Array of \texttt{int}s").next_to(title_1, UP)
        # title_3 = Tex(r"Pointer to (pointer to \texttt{int}) (\texttt{int**})").next_to(title_2, DOWN)
        title_card = Tex(r"(\texttt{int**}) $\leftarrow$ \texttt{my\_2d\_array}").move_to(1.0*UP)
        title_1 = Tex(r"(\texttt{int*}) $\leftarrow$ \texttt{my\_2d\_array[i]}").next_to(title_card, DOWN)
        title_2 = Tex(r"(\texttt{int}) $\leftarrow$ \texttt{my\_2d\_array[i][j]}").next_to(title_1, DOWN)

        self.play(Write(title_card))
        self.wait()
        self.play(Transform(title_card.copy(), title_1))
        self.wait()
        self.play(Transform(title_1.copy(), title_2))
        self.wait()


class RAMPointer:
    def __init__(self, ram_size=1.0, start_address=0):
        self.ram_size = ram_size
        self.arrow = Arrow([(ram_size * 4) + 0.5, 0, 0], end=[0, 0, 0], color=YELLOW)
        self.address = Text("0x" + format(start_address, "08X"), 
                            font="monospace", 
                            color=YELLOW
                           ).scale(ram_size).next_to(self.arrow, RIGHT)
        self.Mobject = VGroup(self.arrow, self.address)

    def change_address(self, scene, address):
        scene.play(Transform(self.address, 
                             Text("0x" + format(address, "08X"), 
                                  font="monospace", 
                                  color=YELLOW
                                 ).scale(self.ram_size).next_to(self.arrow, RIGHT)))


class RAMSample:
    def __init__(self, size, raw_2d_values=[], box_values=True, start_address=0):
        self.raw_2d_values = raw_2d_values
        self.row_count = len(raw_2d_values)
        self.col_count = len(raw_2d_values[0])

        self.addresses = []

        self.Marrays = []
        self.Mobject = []
        
        for i in range(self.row_count):
            position = (UP * (size*self.row_count/2)) + (DOWN * i * size) + (DOWN * size/2)
            self.Marrays.append(MArray(size, raw_2d_values[i], box_values))
            self.Mobject.append(self.Marrays[i].Mobject.move_to(position))
            self.addresses.append(
                Text("0x" + format(start_address + (i * 4), "08X"), font="monospace").scale(size).next_to(self.Mobject[i], LEFT)
            )

        self.y_addresses = MArray(size, [format(i, "02X") for i in range(self.col_count)], False)
        self.y_addresses.Mobject.next_to(self.Mobject[0], UP)

        self.Mobject = VGroup(*self.Mobject)
        self.Mobject_addr = VGroup(*self.addresses, self.y_addresses.Mobject)

    def get_value(self, i, j):
        return self.Marrays[i].Mvalues[j]


class MArray:
    def __init__(self, size=1.0, raw_values=[], box_values=True):
        self.raw_values = raw_values
        self.count = len(raw_values)
        self.size = size

        self.Mboxes = []
        self.Mvalues = []

        for i in range(self.count):
            position = (LEFT * (size*self.count/2)) + (RIGHT * i * size) + (RIGHT * size/2)
            if (box_values):
                self.Mboxes.append(Square(side_length=size).move_to(position))
            self.Mvalues.append(Tex(raw_values[i]).scale(size).move_to(position))

        self.Mobject = VGroup(*self.Mboxes, *self.Mvalues)

    @staticmethod
    def get_position(count, index, size=1.0):
        return (LEFT * (size*count/2)) + (RIGHT * index * size) + (RIGHT * size/2)

