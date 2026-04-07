from fasthtml.common import *

app,rt = fast_app(
    title="Afazta",
    hdrs=(
        Favicon("./assets/favicon.png","./assets/favicon.png"),
        Script(src="https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"),
        Link(rel="stylesheet",href="./styles/main.css")
        ),
    pico=False
    )

@rt("/")
def get():
    # Definisikan style background dots
    dot_style = "background-image: radial-gradient(#333 1px, transparent 1px); background-size: 24px 24px;"
    
    return Body(
        H1("Efek Background Dots", cls="text-white text-center mt-20"),
        Div(
            Div("Konten 1", cls="bg-gray-800 p-8 rounded-xl border border-gray-700"),
            Div("Konten 2", cls="bg-gray-800 p-8 rounded-xl border border-gray-700"),
            Div("Konten 3", cls="bg-gray-800 p-8 rounded-xl border border-gray-700"),
            cls="grid grid-cols-3 gap-6 max-w-4xl mx-auto mt-10"
        ),
        style=dot_style, # Masukkan style di sini
        cls="bg-black min-h-screen"
    )

serve()