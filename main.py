from fasthtml.common import *

from pages.about import About
from pages.blank import Blank
from pages.home import Home
from pages.navbar import Navbar
from pages.projects import Projects
from pages.build import Build

app,rt = fast_app(
    title="Afazta",
    hdrs=(
        Favicon("/favicon.png","/favicon.png"),
        Link(rel="stylesheet",href="/main.css"),
        Script(src="https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"),
        ),
    pico=False,
    static_path="assets"
    )

home = Home()
navbar = Navbar()
pagecomp = [
            {"title":"abouts","url":"/abouts","page":About},
            {"title":"projects","url":"/projects","page":Projects},
            {"title":"blogs","url":"/blogs","page":None},
            {"title":"builds","url":"/builds","page":Build},
        ]

clickplay = Script("""
    document.addEventListener('mousedown', () => {
        var x = document.getElementById("bgclick");
        if (x) {
            x.currentTime = 0;
            x.play().catch(e => console.log("Playback failed"));
        }
    });
""")

def layout(content):
    return Body(
        Audio(Source(src="/clicksound.mp3", type="audio/mpeg"),cls="hidden",  id="bgclick"),
        navbar.run(pagecomp),
        Main(
            Div(
            Div(
                cls="size-65 md:size-115 lg:size-150 rounded-full bg-conic-180 from-red-600 via-red-50 to-red-600 -translate-x-8 -translate-y-14 lg:-translate-x-24 lg:-translate-y-20 blur-[35px] md:blur-[60px] md:-translate-y-20 md:-translate-x-10 lg:blur-[70px] opacity-10 mr-auto lg:opacity-10 absolute -inset-2 will-change-[filter]"
            ),
            Div(
                cls="size-65 md:size-115 lg:size-150 rounded-full bg-conic-180 from-blue-600 via-blue-50 to-blue-600 -translate-x-20 lg:-translate-x-70 translate-y-20 lg:translate-y-80 mt-auto blur-[35px] md:blur-[60px] md:-translate-x-40 md:translate-y-30 lg:blur-[70px] mx-auto opacity-10 lg:opacity-10 absolute -inset-2 will-change-[filter]"
            ),
            Div(
                cls="size-65 md:size-115 lg:size-150 rounded-full bg-conic-180 from-indigo-600 via-indigo-50 to-indigo-600 my-auto translate-x-30 lg:translate-x-35 blur-[35px] md:blur-[60px]  lg:blur-[70px] ml-auto opacity-10 lg:opacity-10 absolute -inset-2 will-change-[filter]"
            ),
            # Div(
            #     # cls="h-full dots absolute -inset-2 opacity-50 "
            # ),
            content,
            cls="relative z-1 overflow-hidden w-screen h-screen"
            )
        ),
        clickplay,
        cls="flex flex-col overflow-hidden bg-(--main-black)"
    )

@rt("/tophero/{idx}/{alp}/{lent}/{typ}")
def get(idx: int,alp: int,lent: int,typ: str):
    return home.getTopHero(idx,alp,lent,typ)

for pg in pagecomp:
    def make_page(p):
        @rt(p["url"])
        def get():
            if p["page"]:
                return layout(
                    p["page"]().run()
                )
            else: return layout(Blank().run())
    make_page(pg)

@rt("/")
def get():
    return layout(home.run())

if __name__ == "__main__":
    serve(app='app')