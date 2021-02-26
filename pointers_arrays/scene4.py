# This is the file of the current scene being worked on.
# Scenes are then archived in their respective episode folders.

from manim import *
from random import randint

config.background_color = "#0d121f"

class Video(Scene):
    def construct(self):

        title_card = Tex(r"\texttt{int x = 2,000,000}")
        title_1 = Tex(r"\texttt{int x = 0000 0000 0001 1110 1000 0100 1000 0000}")
        title_2 = Tex(r"\texttt{int x = 1E 84 80}")
        title_3 = Tex(r"In C/C++, an \texttt{int} is \textbf{4} bytes big.")

        self.play(Write(title_card))
        self.wait()
        self.play(Transform(title_card, title_1))
        self.wait()
        self.play(Transform(title_card, title_2))
        self.wait()
        self.play(Transform(title_card, title_3))
        self.wait()
        
        memory = [[format(0, "02X") for i in range(4)] for _ in range(8)]
        memory[1] = ["00", "1E", "84", "80"]

        Mram_1 = RAMSample(0.80, memory, start_address=0x2c)
        Mram_1.get_value(1, 0).set_color(YELLOW)
        Mram_1.get_value(1, 1).set_color(YELLOW)
        Mram_1.get_value(1, 2).set_color(YELLOW)
        Mram_1.get_value(1, 3).set_color(YELLOW)

        title_4 = Tex(r"\texttt{int x}", color=YELLOW).scale(0.80).next_to(Mram_1.get_value(1, 0), LEFT, buff=0.60)

        self.play(AnimationGroup(ShowCreation(Mram_1.Mobject), Transform(title_card, title_4)))
        self.wait()

        title_5 = Tex(r"\texttt{char y[] = 'h  e  l  l  o  {\textbackslash}0'}")
        title_6 = Tex(r"\texttt{char y[] =  68 65 6C 6C 6F 00 }")

        self.play(AnimationGroup(FadeOut(Mram_1.Mobject), Transform(title_card, title_5)))
        self.wait()
        self.play(Transform(title_card, title_6))
        self.wait()

        memory[5] = ["68", "65", "6C", "6C"]
        memory[6] = ["6F", "00", "00", "00"]

        Mram_2 = RAMSample(0.80, memory, start_address=0x2c)
        Mram_2.get_value(5, 0).set_color(YELLOW)
        Mram_2.get_value(5, 1).set_color(YELLOW)
        Mram_2.get_value(5, 2).set_color(YELLOW)
        Mram_2.get_value(5, 3).set_color(YELLOW)
        Mram_2.get_value(6, 0).set_color(YELLOW)
        Mram_2.get_value(6, 1).set_color(YELLOW)

        title_7 = Tex(r"\texttt{char y[]}", color=YELLOW).scale(0.80).next_to(Mram_1.get_value(5, 0), LEFT, buff=0.60)

        self.play(AnimationGroup(ShowCreation(Mram_2.Mobject), Transform(title_card, title_7)))
        self.wait()

        title_8 = Tex(r"The address stored for variables is usually the first byte.")

        Mram_3 = RAMSample(0.80, memory, start_address=0x2c)
        Mram_3.get_value(1, 0).set_color(RED)
        Mram_3.get_value(5, 0).set_color(RED)

        title_9 = Tex(r"\texttt{\&x = 0x00000030}", color=RED).scale(0.80).next_to(Mram_3.get_value(1, 3), RIGHT, buff=0.65)
        title_10 = Tex(r"\texttt{y = 0x00000040}", color=RED).scale(0.80).next_to(Mram_3.get_value(5, 3), RIGHT, buff=0.65)

        self.play(AnimationGroup(FadeOut(Mram_2.Mobject), Transform(title_card, title_8)))
        self.wait()
        self.play(AnimationGroup(ShowCreation(Mram_3.Mobject), 
                  Transform(title_card, VGroup(title_9, title_10)), 
                  Write(Mram_3.Mobject_addr)))
        self.wait()

        title_11 = Tex(r"\texttt{int* ptr\_to\_x = \&x}")
        title_12 = Tex(r"\texttt{int* ptr\_to\_x = 00 00 00 30}")

        self.play(Transform(title_card, title_12))
        self.wait()

        memory[7] = ["00", "00", "00", "30"]
        Mram_4 = RAMSample(0.80, memory, start_address=0x2c)
        Mram_4.get_value(7, 0).set_color(YELLOW)
        Mram_4.get_value(7, 1).set_color(YELLOW)
        Mram_4.get_value(7, 2).set_color(YELLOW)
        Mram_4.get_value(7, 3).set_color(YELLOW)

        title_13 = Tex(r"\texttt{int* ptr\_to\_x}", color=YELLOW).scale(0.80).next_to(Mram_1.get_value(7, 3), RIGHT, buff=0.60)
        
        self.play(AnimationGroup(ShowCreation(Mram_4.Mobject), 
                  Transform(title_card, title_13), 
                  Write(Mram_4.Mobject_addr)))
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

