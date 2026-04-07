from fasthtml.common import *

class Navbar: 
    def __init__(self):
        ...

    def run(self):
        return Div(
            Div(
                Div(
                    P("Hello"),
                    cls="flex items-center justify-center",
                    style="color: var(--main-gray-light);"
                ),
                cls="flow-root w-full p-2"
            ),
            Div(cls="w-screen h-1 bg-linear-to-r from-[#FF8A8A] via-[#8AEAFF] to-[#A294FF]"),
            cls="block w-full flow-root"
        )