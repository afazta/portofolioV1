import time

from fasthtml.common import *

class Home:
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
        maincls = "jetbrains-mono-400 text-[14px] md:text-[15px] lg:text-[20px] antialiased appearance-none  lg:w-sm -translate-y-3 lg:-translate-y-5"
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
            Span(cls="cursor-blink"),
            cls=maincls,
            style=maincss,
            hx_get=f"/tophero/{next_id}/{next_alp}/{next_lent}/{next_typ}",
            hx_trigger="every 30ms",
            hx_swap="outerHTML"
        )
    
    def run(self):
        return Div(
            Div(
                cls="size-65 md:size-115 lg:size-150 rounded-full bg-conic-180 from-red-600 via-red-50 to-red-600 -translate-x-8 -translate-y-14 lg:-translate-x-24 lg:-translate-y-20 blur-[35px] md:blur-[60px] md:-translate-y-20 md:-translate-x-10 lg:blur-[70px] opacity-30 mr-auto lg:opacity-30 absolute -inset-2 will-change-[filter]"
            ),
            Div(
                cls="size-65 md:size-115 lg:size-150 rounded-full bg-conic-180 from-blue-600 via-blue-50 to-blue-600 -translate-x-20 lg:-translate-x-70 translate-y-20 lg:translate-y-80 mt-auto blur-[35px] md:blur-[60px] md:-translate-x-40 md:translate-y-30 lg:blur-[70px] mx-auto opacity-30 lg:opacity-30 absolute -inset-2 will-change-[filter]"
            ),
            Div(
                cls="size-65 md:size-115 lg:size-150 rounded-full bg-conic-180 from-indigo-600 via-indigo-50 to-indigo-600 my-auto translate-x-30 lg:translate-x-35 blur-[35px] md:blur-[60px]  lg:blur-[70px] ml-auto opacity-30 lg:opacity-30 absolute -inset-2 will-change-[filter]"
            ),
            Div(
                cls="h-full dots absolute -inset-2 opacity-50"
            ),
            Div(
                self.sideLeft(),
                self.sideRight(),
                cls="flex flex-row lg:mx-auto p-8 md:p-14 lg:p-20 items-center lg:justify-around h-full relative"
            ),
            cls="relative z-1 overflow-hidden w-screen h-screen"
            )
    
    def sideLeft(self):
        return Div(
            Div(
                self.getTopHero(0,0,0,"p"),
                H1(
                    "Tafsir.",
                    cls="domine-700 text-white text-[80px] md:text-[140px] lg:text-[200px] antialiased appearance-none m-0 leading-none"
                ),
                P(
                    "Doing like a cat, sometime sleep sometime coding",
                    cls="jetbrains-mono-400 text-[12px] md:text-[13px] lg:text-[18px] antialiased appearance-none lg:w-sm translate-y-2",
                    style="color: var(--main-gray-light)"
                ),
                P(
                    "Change path to explore ↑",
                    cls="jetbrains-mono-400 text-[10px] md:text-[11px] lg:text-[14px] antialiased appearance-none translate-y-10 lg:translate-y-12 lg:w-sm",
                    style="color: var(--main-gray-light)"
                ),
                cls="flex flex-col items-start"
            ),
            cls=" "
        )
    
    def sideRight(self):
        return Div(
            Img(
                src="/profile.png", 
                id="profile",
                cls="w-[60%] lg:w-[90%] xl:w-[97%] saturate-100 opacity-100 rounded-full h-full antialiased appearance-none aspect-1/1 object-cover absolute -insert-2 "
            ),
            Img(
                src="/rmbg.png",
                id="profile",
                cls="w-[60%] md:w-[65%] lg:w-[90%] xl:w-[97%] saturate-100 opacity-100 h-full antialiased appearance-none aspect-1/1 object-cover rounded-b-full relative "
            ),
            cls="h-xl hidden lg:block relative"
        )