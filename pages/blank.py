import time
from fasthtml.common import *


class Blank:
    def __init__(self):
        ...
    
    def run(self):
        return Div(P("404 | Coming soon",cls="text-white jetbrains-mono-500 antialiased appearance-none"),cls="flex flex-row m-auto relative h-full w-full items-center justify-center")