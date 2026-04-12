from fasthtml.common import *

from pages.home import Home
from pages.navbar import Navbar

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
            {"title":"abouts","url":"/abouts"},
            {"title":"skills","url":"/skills"},
            {"title":"projects","url":"/projects"},
            {"title":"contacts","url":"/about"},
        ]

def layout(content):
    return Body(
        navbar.run(pagecomp),
        content,
        cls="flex flex-col overflow-hidden bg-(--main-black)"
    )

@rt("/tophero/{idx}/{alp}/{lent}/{typ}")
def get(idx: int,alp: int,lent: int,typ: str):
    return home.getTopHero(idx,alp,lent,typ)

for p in pagecomp:
    @rt(p["url"])
    def get():
        return layout(P(p["title"],cls="text-white"))

@rt("/")
def get():
    return layout(home.run())

serve(port=4000)