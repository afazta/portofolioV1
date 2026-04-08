from fasthtml.common import *

from components.hero import Hero
from components.navbar import Navbar

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

hero = Hero()

@rt("/tophero/{idx}/{alp}/{lent}/{typ}")
def get(idx: int,alp: int,lent: int,typ: str):
    return hero.getTopHero(idx,alp,lent,typ)

@app.route("/")
def home():
    return Body(
        Navbar().run(),
        hero.run(),
        style="background-color: var(--main-black);",
        cls="flex flex-col overflow-x-hidden"
    )

serve(port=4000)