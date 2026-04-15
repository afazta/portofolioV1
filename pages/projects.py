from fasthtml.common import *

from components.cardbox import CardBox

class Projects:
    def __init__(self):
        self.dataproj = [
            {"url":"https://afazta.github.io/jugux/","name":"Jugux","img":"/jugux.png","desc":"Free software to upscale, smooth, and enhance images and videos. Includes background removal."},
            {"url":"https://github.com/MottiFx","name":"Mottifx","img":"/mottifx.png","desc":"A free, open-source video editing software built for high-performance. Designed to be lightweight, fast, and powerful for professional-grade creative workflows."},
            {"url":"https://github.com/afazta/o-toilet","name":"O-Toilet","img":"/otoilet.png","desc":"O-Toilet is an automatic toilet system, where all the systems are fully automatic [(automatic door opening and locking feature), (water feature that fills itself when the water in the tub is empty, this can help reduce water waste for users who misuse it), (LED that lights up according to the conditions)] and is only in the toilet [this is only in the form of a small model or design] "},
        ]

    def run(self):
        return Div(
            Div(
                Div(
                    H1("Selected Projects", cls="text-white jetbrains-mono-700 text-3xl md:text-5xl tracking-tighter"),
                    Span("A showcase of my recent work and experiments.", cls="text-(--main-gray-light) jetbrains-mono-400 text-sm md:text-base"),
                    cls="space-y-2 mb-12 my-4 md:mb-0 md:my-0 border-l-4 border-white/10 pl-4"
                ),
            ),
            Div(
                *[CardBox().run(dt["img"],dt["name"],dt["url"],dt["desc"]) for dt in self.dataproj],
                cls="grid grid-flow-row grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8 items-center justify-center [&>*:last-child]:md:col-span-full lg:[&>*:last-child]:lg:col-span-1 m-auto w-fit"
            ),
            cls="place-content-center m-auto p-5 md:p-14 max-w-fit lg:p-20 items-center justify-center w-full h-full relative block space-y-4 md:space-y-10 overflow-y-scroll md:overflow-hidden pb-24 lg:pb-20"
        )