import time

from fasthtml.common import *

class Hero:
    def __init__(self):
        self.tophero = [
            "Assalamualaikum", 
            "Software dev enthusiast", 
            "Arduino & Robotics hobbyist", 
            "Turning code into hardware", 
            "Editing & Creative mind", 
            "Just for fun"
        ]
    
    def getTopHero(self,idx,alp,lent,typ):
        cur_word = self.tophero[idx]
        next_lent = lent
        next_alp = alp
        next_id = idx
        next_typ = typ
        maincls = "jetbrains-mono-400 text-[22px] antialiased appearance-none translate-y-8 w-sm"
        maincss = "color: var(--main-gray-light)"

        if next_lent == 0: 
            time.sleep(0.15)            
            next_lent = len(cur_word) + 1
        if next_alp == next_lent:
            time.sleep(0.15)            

        if next_typ == "p":
            if next_alp < next_lent:
                next_alp += 1
            else: 
                next_typ = "n"
        else:
            if next_alp > 0:
                next_alp -= 1
            else:
                next_id = (idx + 1) % len(self.tophero)
                next_lent = 0
                next_alp = 0
                next_typ = "p"

        cur_alp = cur_word[:next_alp]

        return P(
            cur_alp,
            cls=maincls,
            style=maincss,
            hx_get=f"/tophero/{next_id}/{next_alp}/{next_lent}/{next_typ}",
            hx_trigger="every 30ms",
            hx_swap="outerHTML"
        )
    
    def run(self):
        return Div(
            Div(
                Div(
                    cls="size-150 rounded-full bg-conic-180 from-red-600 via-red-50 to-red-600 -translate-x-14 -translate-y-20  blur-[180px] mr-auto opacity-60"
                ),
                Div(
                    cls="size-150 rounded-full bg-conic-180 from-indigo-600 via-indigo-50 to-indigo-600 -translate-x-10 translate-y-full  blur-[180px] ml-auto opacity-60"
                ),
                cls="flex absolute -inset-2 w-screen"
            ),
            Div(
                cls="w-screen h-screen dots absolute -inset-2 opacity-50"
            ),
            Div(
                self.sideLeft(),
                self.sideRight(),
                cls="flex m-auto p-20 items-center justify-around h-screen  w-screen relative"
            ),
            cls="flow-root relative"
            )
    
    def sideLeft(self):
        return Div(
            Div(
                self.getTopHero(0,0,0,"p"),
                H1(
                    "Tafsir.",
                    cls="domine-700 text-white text-[200px] antialiased appearance-none m-0"
                ),
                P(
                    "Doing like a cat, sometime sleep sometime coding",
                    cls="jetbrains-mono-400 text-[18px] antialiased appearance-none -translate-y-8 w-sm",
                    style="color: var(--main-gray-light)"
                ),
                P(
                    "Scroll to explore ↓",
                    cls="jetbrains-mono-400 text-[14px] antialiased appearance-none -translate-y-0 w-sm",
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
                cls="w-[90%] saturate-100 opacity-100 rounded h-full antialiased appearance-none"
            ),
            cls="w-fit h-xl flow-root "
        )