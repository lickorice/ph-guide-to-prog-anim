from manim import *

def transition_all(scene, text_list, transition_time=1.0):
    first_tex = Tex(text_list[0])
    scene.play(Write(first_tex), run_time=transition_time)
    scene.wait()
    for text in text_list[1:]:
        scene.play(Transform(first_tex, Tex(text)), run_time=transition_time)
        scene.wait()
