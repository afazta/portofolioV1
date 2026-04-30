import time
from fasthtml.common import *

class About:
    def __init__(self):
        ...

    def run(self):
        return Div(
            Div(
                Div(
                    H1("Hi! I'm ", 
                       Span("Tafsir", cls="text-(--main-blue)"), 
                       cls="text-white domine-700 text-4xl md:text-6xl tracking-tight"),
                    
                    # Core Info Tags
                    Div(
                        Div(
                            Img(src="https://cdn.simpleicons.org/github/888888", cls="w-4 h-4"),
                            Span("Full Stack Developer", cls="text-(--main-gray-light) jetbrains-mono-400 text-xs md:text-sm"),
                            cls="flex items-center gap-2"),
                        Div(
                            Img(src="https://cdn.simpleicons.org/mapillary/888888", cls="w-4 h-4"),
                            Span("Jakarta, Indonesia", cls="text-(--main-gray-light) jetbrains-mono-400 text-xs md:text-sm"),
                            cls="flex items-center gap-2"),
                        cls="flex flex-wrap justify-center gap-5 mt-4"
                    ),
                    cls="mb-10 text-center"
                ),                
                Div(
                    P("""
                        I'm a Full Stack Developer who enjoys building things. I like creating and releasing 
                        open-source projects that can be useful for others.
                    """, cls="text-white/90 jetbrains-mono-400 text-sm md:text-base leading-relaxed max-w-2xl mx-auto text-center mb-4"),
                    
                    P("""
                        I also do some creative design and video editing to keep the projects 
                        I work on looking decent and easy to use.
                    """, cls="text-(--main-gray-light) jetbrains-mono-400 text-sm md:text-base leading-relaxed max-w-2xl mx-auto text-center"),
                    
                    cls="mb-12"
                ),
                Div(
                    P("Mainly working with:", cls="text-(--main-gray-light) jetbrains-mono-500 text-[10px] uppercase tracking-[0.3em] mb-6 text-center"),
                    Div(
                        Div(Img(src="https://cdn.simpleicons.org/python/8AEAFF", cls="w-5 h-5"), Span("Python"), 
                            cls="flex items-center gap-2 bg-(--main-gray-dark) px-4 py-2 rounded border border-(--main-gray-mid) jetbrains-mono-400 text-xs text-white hover:border-(--main-blue) transition-all"),
                        Div(Img(src="https://cdn.simpleicons.org/dart/8AEAFF", cls="w-5 h-5"), Span("Dart/Flutter"), 
                            cls="flex items-center gap-2 bg-(--main-gray-dark) px-4 py-2 rounded border border-(--main-gray-mid) jetbrains-mono-400 text-xs text-white hover:border-(--main-blue) transition-all"),
                        Div(Img(src="https://cdn.simpleicons.org/typescript/8AEAFF", cls="w-5 h-5"), Span("TypeScript"), 
                            cls="flex items-center gap-2 bg-(--main-gray-dark) px-4 py-2 rounded border border-(--main-gray-mid) jetbrains-mono-400 text-xs text-white hover:border-(--main-blue) transition-all"),
                        Div(Img(src="https://cdn.simpleicons.org/zig/8AEAFF", cls="w-5 h-5"), Span("Zig"), 
                            cls="flex items-center gap-2 bg-(--main-gray-dark) px-4 py-2 rounded border border-(--main-gray-mid) jetbrains-mono-400 text-xs text-white hover:border-(--main-blue) transition-all"),
                        Div(Img(src="https://cdn.simpleicons.org/arduino/8AEAFF", cls="w-5 h-5"), Span("Arduino"), 
                            cls="flex items-center gap-2 bg-(--main-gray-dark) px-4 py-2 rounded border border-(--main-gray-mid) jetbrains-mono-400 text-xs text-white hover:border-(--main-blue) transition-all"),
                        
                        cls="flex flex-wrap justify-center gap-3"
                    )
                ),
                cls="w-full max-w-4xl"
            ),
            cls="flex flex-col items-center justify-center min-h-screen mb-10 md:mb-auto m-auto p-6 md:p-14 container relative w-full overflow-hidden"
        )