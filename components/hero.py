from fasthtml.common import *


class Hero:
    def __init__(self):
        ...

    def run(self):
        return Div(
            Div(
                self.sideLeft(),
                self.sideRight(),
                cls="flex m-auto p-20 items-center justify-around h-screen  w-screen dots"
            ),
            cls="flow-root"
            )
    
    def sideLeft(self):
        return Div(
            Div(
                P(
                    "Software Enginnering",
                    cls="jetbrains-mono-400 text-[22px] antialiased appearance-none translate-y-8 w-sm",
                    style="color: var(--main-gray-light)"
                ),
                H1(
                    "Tafsir",
                    cls="domine-700 text-white text-[200px] antialiased appearance-none m-0"
                ),
                P(
                    "Doing like a cat, sometime sleep sometime coding",
                    cls="jetbrains-mono-400 text-[18px] antialiased appearance-none -translate-y-8 w-sm",
                    style="color: var(--main-gray-light)"
                ),
                cls="flex flex-col items-start"
            ),
            cls="w-fit flow-root"
        )
    
    def sideRight(self):
        return Div(
            Img(
                src="/profile.png",
                id="profile",
                cls="w-[90%] saturate-0 opacity-100 rounded h-full"
            ),
            cls="w-fit h-xl flow-root "
        )