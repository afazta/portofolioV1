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

@app.route("/")
def home():
    return Body(
        Navbar().run(),
        Hero().run(),
        style="background-color: var(--main-black);",
        cls="flex-col overflow-x-hidden"
    )

serve(port=4000)