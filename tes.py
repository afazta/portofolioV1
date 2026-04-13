from fasthtml.common import *
from pages.home import Home
from pages.navbar import Navbar

# Pastikan file audio ada di folder assets/clicksound.mp3
app, rt = fast_app(
    title="Afazta",
    hdrs=(
        Favicon("/favicon.png", "/favicon.png"),
        Link(rel="stylesheet", href="/main.css"),
        Script(src="https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"),
    ),
    pico=False,
    static_path="assets"
)

home = Home()
navbar = Navbar()
pagecomp = [
    {"title": "abouts", "url": "/abouts"},
    {"title": "skills", "url": "/skills"},
    {"title": "projects", "url": "/projects"},
    {"title": "contacts", "url": "/about"},
]

# Script global: Menangkap klik biasa DAN event navigasi HTMX
clickplay = Script("""
    function playClick() {
        var x = document.getElementById("bgclick");
        if (x) {
            x.currentTime = 0;
            x.play().catch(e => {});
        }
    }
    // Bunyi untuk semua klik di dokumen
    document.addEventListener('click', playClick);
    
    // Bunyi saat HTMX mulai melakukan request pindah halaman
    document.addEventListener('htmx:beforeRequest', playClick);
""")

def layout(content):
    return Body(
        # Tag Audio tetap di luar main-content agar tidak ter-reset saat navigasi
        Audio(Source(src="/clicksound.mp3", type="audio/mpeg"), cls="hidden", id="bgclick"),
        navbar.run(pagecomp),
        # Kontainer Utama yang akan diganti isinya oleh HTMX
        Main(content, id="main-content", cls="flex-1"),
        clickplay,
        cls="flex flex-col min-h-screen overflow-hidden bg-(--main-black)"
    )

# Helper untuk menangani request HTMX vs Request Biasa
def render_page(request, content):
    # Jika request datang dari HTMX (klik navbar), kirim kontennya saja
    if 'HX-Request' in request.headers:
        return content
    # Jika user ketik URL manual/refresh, kirim seluruh layout
    return layout(content)

@rt("/tophero/{idx}/{alp}/{lent}/{typ}")
def get(idx: int, alp: int, lent: int, typ: str):
    return home.getTopHero(idx, alp, lent, typ)

# Loop Route untuk halaman statis
for p in pagecomp:
    @rt(p["url"])
    def get(request, p=p): # p=p untuk closure scope
        content = P(p["title"], cls="text-white p-10")
        return render_page(request, content)

@rt("/")
def get(request):
    content = home.run()
    return render_page(request, content)

serve(port=4000)