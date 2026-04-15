import time
from fasthtml.common import *

class About:
    def __init__(self):
        ...

    def run(self):
        return Div(
            Div(
                Div(
                    H1("Hi! I'm ",Span("Tafsir",cls=" text-(--main-blue)"), cls="text-white domine-700 text-3xl md:text-5xl tracking-normal"),
                    Div(
                        Div(
                            Img(src="https://cdn.simpleicons.org/make/888888", cls="w-4 h-4 md:w-6 md:h-6"),
                            Span("Technology Enthusiast", cls="text-(--main-gray-light) jetbrains-mono-400 text-sm md:text-base"),
                            cls="flex flex-row items-center gap-3"),
                        Div(
                            Img(src="https://cdn.simpleicons.org/mapillary/888888", cls="w-4 h-4 md:w-6 md:h-6"),
                            Span("Jakarta, Indonesia", cls="text-(--main-gray-light) jetbrains-mono-400 text-sm md:text-base"),
                            cls="flex flex-row items-center gap-3"),
                        cls="flex flex-wrap gap-x-5 gap-y-2 mt-3"
                    ),
                    cls="space-y-2 mb-4 my-4 md:mb-0 md:my-0 border-l-4 border-white/10 pl-4"
                ),
                P("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."*2,cls="line-clamp-4 text-(--main-gray-light) text-xs md:text-sm mt-4 max-w-200"),
            ),
            cls="place-content-center m-auto p-5 md:p-14 container lg:p-20 items-center justify-center w-full h-full relative block space-y-4 md:space-y-10 overflow-y-scroll md:overflow-hidden pb-24 lg:pb-20"
        )