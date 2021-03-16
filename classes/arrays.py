from manim import *

class MArray:
    def __init__(self, size=1.0, raw_values=[], box_values=True):
        self.raw_values = raw_values
        self.count = len(raw_values)
        self.size = size

        self.mboxes = []
        self.mvalues = []

        for i in range(self.count):
            position = MArray.get_position(self.count, i, self.size)
            if (box_values):
                self.mboxes.append(Square(side_length=size).move_to(position))
            self.mvalues.append(Tex(raw_values[i]).scale(size).move_to(position))

        self.mobject = VGroup(*self.mboxes, *self.mvalues)

    @staticmethod
    def get_position(count, index, size=1.0):
        return (LEFT * (size*count/2)) + (RIGHT * index * size) + (RIGHT * size/2)


class BubbleSortArray(MArray):
    def __init__(self, size=1.0, raw_values=[]):
        super().__init__(size, raw_values, True)
        self.mbrace = Brace(
            VGroup(*self.mboxes[:2]),
            direction=DOWN
        )
        self.raw_checks = 0
        self.check_text = Tex("Checks:").next_to(self.mboxes[0], UP, buff=0.20)
        self.checks = DecimalNumber(0, num_decimal_places=0).next_to(self.check_text, RIGHT, buff=0.50)
        self.checks.add_updater(lambda o: o.next_to(self.check_text, RIGHT, buff=0.50))
        self.mobject = VGroup(self.mobject, self.check_text, self.checks)
        self.currently_sorting = 0

    def next_comparison(self, scene, wait_time, run_time):
        self.currently_sorting += 1
        if (self.currently_sorting >= self.count-1): self.currently_sorting = 0
        i = self.currently_sorting
        scene.play(Transform(self.mbrace,
            Brace(
                VGroup(*self.mboxes[i:i+2]),
                direction=DOWN
            )
        ), run_time=run_time)
        scene.wait(wait_time)

    def swap(self, scene, element_a, element_b, wait_time, run_time):
        scene.play(AnimationGroup(
            ApplyMethod(element_a.shift, (self.size, 0, 0)),
            ApplyMethod(element_b.shift, (-self.size, 0, 0)),
        ), run_time=run_time)
        scene.wait(wait_time)

    def sort(self, scene, wait_time=1.0, run_time=1.0):
        while True:
            is_sorted = True
            for i in range(self.count-1):
                self.raw_checks += 1
                scene.play(ChangeDecimalToValue(self.checks, self.raw_checks), run_time=0.07)
                if self.raw_values[i] > self.raw_values[i+1]:
                    self.raw_values[i], self.raw_values[i+1] = self.raw_values[i+1], self.raw_values[i]
                    self.swap(scene, self.mvalues[i], self.mvalues[i+1], wait_time, run_time)
                    self.mvalues[i], self.mvalues[i+1] = self.mvalues[i+1], self.mvalues[i]
                    is_sorted = False
                if (i < self.count-1):
                    self.next_comparison(scene, wait_time, run_time)
            if (is_sorted): break
        scene.play(FadeOut(self.mbrace))
