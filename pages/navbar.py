from fasthtml.common import *

class Navbar: 
    def __init__(self):
        ...

    def run(self,listpage):
        return Div(
            Div(
                Div(
                    Div(
                        H3(
                            A("Me.",href="/"),
                            cls="domine-400 text-white text-[14px] md:text-[20px] cursor-pointer antialiased appearance-none",
                        ),
                        cls="mr-auto"
                    ),
                    Div(
                        
                            (P(A(d["title"].capitalize(),href=d["url"]),
                            cls="text-[9px] md:text-[13px] jetbrains-mono-400 cursor-pointer antialiased appearance-none text-[#888888] hover:text-white"
                            )
                            for d in listpage),
                        cls="flex items-center justify-beetwen gap-3 md:gap-6 ml-auto"
                    ),
                    cls="flex items-center",
                ),
                cls="flow-root w-full p-5 md:p-10 py-3"
            ),
            Div(
                # Div(cls="w-screen h-5 bg-linear-to-r from-[#FF8A8A] via-[#8AEAFF] to-[#A294FF] absolute -inset-2 opacity-40 rounded blur-xl translate-y-6"),
                # Div(cls="w-screen h-[.8px] bg-linear-to-r from-[#FF8A8A] via-[#8AEAFF] to-[#A294FF] relative"),
                cls="relative"
            ),
            cls="block w-screen fixed z-10 bottom-0"
        )