from fasthtml.common import *

class Navbar: 
    def __init__(self):
        self.listpage = [
            {"title":"abouts","url":"#abouts"},
            {"title":"skills","url":"#skills"},
            {"title":"projects","url":"#projects"},
            {"title":"contacts","url":"#about"},
        ]

    def run(self):
        return Div(
            Div(
                Div(
                    Div(
                        H3(
                            "Me.",
                            cls="domine-400 text-white text-[20px] cursor-pointer antialiased appearance-none"
                        ),
                        cls="mr-auto"
                    ),
                    Div(
                        
                            (P(d["title"].capitalize(),
                            cls="text-[13px] jetbrains-mono-400 cursor-pointer antialiased appearance-none text-[#888888] hover:text-white",
                            )
                            for d in self.listpage),
                        cls="flex items-center justify-beetwen gap-6 ml-auto"
                    ),
                    cls="flex items-center",
                ),
                cls="flow-root w-full p-10 py-3"
            ),
            Div(
                # Div(cls="w-screen h-5 bg-linear-to-r from-[#FF8A8A] via-[#8AEAFF] to-[#A294FF] absolute -inset-2 opacity-40 rounded blur-xl translate-y-6"),
                Div(cls="w-screen h-[.8px] bg-linear-to-r from-[#FF8A8A] via-[#8AEAFF] to-[#A294FF] relative"),
                cls="relative"
            ),
            cls="hidden md:block w-screen flow-root fixed backdrop-blur-md bg-black/10 z-10 top-0"
        )