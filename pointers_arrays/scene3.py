# This is the file of the current scene being worked on.
# Scenes are then archived in their respective episode folders.

from manim import *
from random import randint

config.background_color = "#0d121f"

class Video(Scene):
    def construct(self):
        words = [[format(randint(0, 256), "02X") for i in range(8)] for _ in range(8)]

        Mram = RAMSample(0.80, list(map(lambda x: x[:4], words)), start_address=0x2c)

        self.add(Mram.Mobject)
        self.add(Mram.Mobject_addr)
        self.wait()

        Mword32inc = MArray(1.0, [format(0, "02X") for i in range(4)])
        title = Tex(r"Address space/size is also limited by the \textbf{word size!}").next_to(Mword32inc.Mobject, UP)

        number = DecimalNumber(0, num_decimal_places=0).next_to(Mword32inc.Mobject, DOWN, buff=0.50)
        bitsword = Tex("addressable bytes").next_to(number, DOWN)

        self.play(FadeOut(Mram.Mobject_addr))
        self.play(ReplacementTransform(Mram.Mobject, Mword32inc.Mobject))
        self.play(FadeIn(title))
        self.play(FadeIn(VGroup(number, bitsword)))

        Mword32inc.Mvalues[0].add_updater( lambda x: x.become( Tex(format(int(number.get_value()), "08X")[0:2]).move_to(MArray.get_position(4, 0)) ) )
        Mword32inc.Mvalues[1].add_updater( lambda x: x.become( Tex(format(int(number.get_value()), "08X")[2:4]).move_to(MArray.get_position(4, 1)) ) )
        Mword32inc.Mvalues[2].add_updater( lambda x: x.become( Tex(format(int(number.get_value()), "08X")[4:6]).move_to(MArray.get_position(4, 2)) ) )
        Mword32inc.Mvalues[3].add_updater( lambda x: x.become( Tex(format(int(number.get_value()), "08X")[6:8]).move_to(MArray.get_position(4, 3)) ) )

        number.add_updater(lambda o: o.next_to(Mword32inc.Mobject, DOWN, buff=0.50))

        self.wait()
        self.play(ChangeDecimalToValue(number, 4294967295), run_time=3)
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

