from fasthtml.common import *

class Build:
    def __init__(self):
        ...

    def run(self):
        description_text = (
            "I'm available for new projects, specializing in programming for both paid contracts and "
            "open-source collaborations. I also accept professional projects for Design, Video Editing, "
            "and IoT development."
        )
        return Div(
            Div(
                H1(
                    "Have Something  \n To Build ?",
                    cls="text-white whitespace-pre-line domine-700 text-4xl md:text-6xl tracking-tight",
                    ),
                Div(
                    A(Div(
                        Img(src="https://cdn.simpleicons.org/github/888888", cls="w-4 h-4"),
                        Span("Github ↗", cls="text-(--main-gray-light) jetbrains-mono-400 text-xs md:text-sm"),
                        cls="flex items-center gap-2"),href="https://github.com/afazta"),
                    A(Div(
                        Img(src="https://cdn.simpleicons.org/instagram/888888", cls="w-4 h-4"),
                        Span("Instagram ↗", cls="text-(--main-gray-light) jetbrains-mono-400 text-xs md:text-sm"),
                        cls="flex items-center gap-2"),href="https://www.instagram.com/kawenzy_"),
                    A(Div(
                        Img(src="https://cdn.simpleicons.org/codeberg/888888", cls="w-4 h-4"),
                        Span("Codeberg ↗", cls="text-(--main-gray-light) jetbrains-mono-400 text-xs md:text-sm"),
                        cls="flex items-center gap-2"),href="https://codeberg.org/afazta/"),
                    cls="flex flex-wrap justify-center gap-5 mt-4"
                ),
                cls="mb-10 text-center"
            ),
            Div(
                P(description_text, cls="text-(--main-gray-light) jetbrains-mono-400 text-sm md:text-base leading-relaxed max-w-2xl mx-auto text-center"),
                cls="mb-12"
            ),
            Div(
                A(Button(
                    "AFAZTA@PROTON.ME",
                    cls="px-4 py-2 jetbrains-mono-600 cursor-pointer text-sm text-white rounded backdrop-blur-md bg-(--main-gray-mid)/15 border border-white/10 hover:border-white/30 hover:bg-(--main-gray-mid)/35 transition-all duration-200 w-fit"
                ),href="mailto:afazta@proton.me"),
                A(Button(
                    "DOWNLOAD CV",
                    cls="px-4 py-2 jetbrains-mono-600 cursor-pointer text-sm text-white rounded backdrop-blur-md bg-(--main-gray-mid)/15 border border-white/10 hover:border-white/30 hover:bg-(--main-gray-mid)/35 transition-all duration-200 w-fit"
                ),href="https://drive.google.com/file/d/1Lc3sHD86-QQ7ov2TBWXAAC4faMC-lBmj/view?usp=drive_link"),
                cls="flex flex-wrap justify-center gap-3"
            ),
            cls="flex flex-col items-center justify-center min-h-screen m-auto p-6 md:p-14 container relative w-full overflow-hidden"
        )