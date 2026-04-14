from fasthtml.common import *

class Navbar: 
    def __init__(self):
        ...

    def run(self,listpage):
        return Div(
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
            cls=" w-full px-5 md:px-10 py-2 flex items-center"
            ),
            cls="block w-screen h-fit fixed z-10 bottom-0"
        )