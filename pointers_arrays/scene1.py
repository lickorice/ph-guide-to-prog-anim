# This is the file of the current scene being worked on.
# Scenes are then archived in their respective episode folders.

from manim import *

config.background_color = "#0d121f"

class Video(Scene):
    def construct(self):
        title_card = Tex(r"Our computer stores data in \textbf{binary}.")

        bit = MArray(1, 1.0, [0])
        byte = MArray(8, 1.0, [0 for i in range(8)])

        title_bit = Tex(r"This is a bit:").next_to(bit.Mobject, UP)
        title_byte = Tex(r"A byte is eight bits:").next_to(byte.Mobject, UP)
        
        self.play(Write(title_card))
        self.wait()
        self.play(Transform(title_card, title_bit))
        self.play(ShowCreation(bit.Mobject))
        self.wait()
        self.play(Transform(title_card, title_byte))
        self.play(ReplacementTransform(bit.Mobject, byte.Mobject))
        self.wait()

        brace_1 = Brace(VGroup(*byte.Mboxes[:4]), DOWN)
        brace_2 = Brace(VGroup(*byte.Mboxes[4:]), DOWN)

        self.play(ShowCreation(VGroup(brace_1, brace_2)))
        self.wait(0.2)

        title_bin_1 = Tex("0 to 15").next_to(brace_1, DOWN)
        title_bin_2 = Tex("0 to 15").next_to(brace_2, DOWN)
        
        title_hex_1 = Tex("0 to F").next_to(brace_1, DOWN)
        title_hex_2 = Tex("0 to F").next_to(brace_2, DOWN)

        self.play(Write(VGroup(title_bin_1, title_bin_2)))
        self.wait()
        self.play(Transform(title_bin_1, title_hex_1))
        self.play(Transform(title_bin_2, title_hex_2))
        self.wait()
        self.play(FadeOut(VGroup(brace_1, brace_2, title_bin_1, title_bin_2)))
        self.wait()

        # Our raw numbers:
        equals = Tex("=").next_to(byte.Mobject, DOWN, buff=0.50)
        number = DecimalNumber(0, num_decimal_places=0).next_to(equals, LEFT)
        hex_number = Tex("0x", "0", "0").next_to(equals, RIGHT)
        hex_number[1].next_to(hex_number[0], RIGHT, buff=0.05)
        hex_number[2].next_to(hex_number[1], RIGHT, buff=0.05)

        def hex_num_update(i):
            def update(obj):
                obj.become(Tex(format(int(number.get_value()), "02X")[i-1]))
                obj.next_to(hex_number[i-1], RIGHT, buff=0.05)
            return update

        number.add_updater(lambda o: o.next_to(equals, LEFT))

        # Increment our array, sadly cannot be put in a for-loop:
        byte.Mvalues[0].add_updater(lambda x: x.set_value( int(format(int(number.get_value()), "08b")[0]) ))
        byte.Mvalues[1].add_updater(lambda x: x.set_value( int(format(int(number.get_value()), "08b")[1]) ))
        byte.Mvalues[2].add_updater(lambda x: x.set_value( int(format(int(number.get_value()), "08b")[2]) ))
        byte.Mvalues[3].add_updater(lambda x: x.set_value( int(format(int(number.get_value()), "08b")[3]) ))
        byte.Mvalues[4].add_updater(lambda x: x.set_value( int(format(int(number.get_value()), "08b")[4]) ))
        byte.Mvalues[5].add_updater(lambda x: x.set_value( int(format(int(number.get_value()), "08b")[5]) ))
        byte.Mvalues[6].add_updater(lambda x: x.set_value( int(format(int(number.get_value()), "08b")[6]) ))
        byte.Mvalues[7].add_updater(lambda x: x.set_value( int(format(int(number.get_value()), "08b")[7]) ))

        self.play(FadeIn(VGroup(equals, number, hex_number[0], hex_number[1], hex_number[2])))
        self.wait()

        hex_number[1].add_updater(hex_num_update(1))
        hex_number[2].add_updater(hex_num_update(2))

        self.play(ChangeDecimalToValue(number, 255), run_time=3)
        self.wait(2)


class MArray:
    def __init__(self, count, size=1.0, raw_values=[]):
        self.raw_values = raw_values
        self.count = count
        self.size = size

        self.Mboxes = []
        self.Mvalues = []

        for i in range(count):
            position = (LEFT * (size*count/2)) + (RIGHT * i * size) + (RIGHT * size/2)
            self.Mboxes.append(Square(side_length=size).move_to(position))
            self.Mvalues.append(DecimalNumber(raw_values[i], num_decimal_places=0).scale(size).move_to(position))

        self.Mobject = VGroup(*self.Mboxes, *self.Mvalues)

