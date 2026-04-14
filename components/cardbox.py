from fasthtml.common import *

class CardBox:
    def __init__(self):
        ...
    
    def run(self,img,name,url,desc):
            return Div(
                Img(src=img, id="card", 
                    cls="w-full h-64 object-cover appearance-none rounded-sm "),
                Div(
                    H1(name, cls="text-white antialiased appearance-none jetbrains-mono-500 text-[20px] md:text-[24px]"),
                    P(desc.capitalize(), 
                    cls="line-clamp-2 text-[12px] md:text-[16px] jetbrains-mono-400 text-(--main-gray-light) antialiased appearance-none"),
                    
                    A("Visit", 
                    href=url, 
                    cls="""mt-4 w-full text-center py-3 rounded-sm bg-white/10 text-white 
                            jetbrains-mono-500 border border-white/20 hover:bg-white/20 
                            transition-all duration-300 antialiased appearance-none text-[16px] md:text-[20px]"""),
                    
                    cls="flex flex-col gap-3 items-start"
                ),
                cls="flex flex-col overflow-hidden rounded-md backdrop-blur-md bg-(--main-gray-mid)/15 border border-white/10 w-full max-w-[500px] h-fit mx-auto px-4 md:px-6 py-4 md:py-6 gap-5 group"
            )