import time
from fasthtml.common import *

class About:
    def __init__(self):
        ...

    def run(self):
        return Div(
            cls="flex flex-row lg:mx-auto p-8 md:p-14 lg:p-20 items-center lg:justify-around w-full h-full relative"
        )