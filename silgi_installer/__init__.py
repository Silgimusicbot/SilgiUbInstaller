from rich.console import Console
from rich.panel import Panel
from rich.live_render import LiveRender
import sys
import os, shutil
console = Console()

def hata (text):
   console.print(text, style="bold red")
def bilgi (text):
   console.print(text, style="blue")
def basarili (text):
   console.print(f"[bold green]{text}[/]")
def onemli (text):
   console.print(text, style="bold cyan")
def soru (soru):
   return console.input(f"[bold yellow]{soru}[/]")
def logo(dil="None"):
    python_versiya = f"{sys.version_info[0]}.{sys.version_info[1]}"
    try:
        import telethon
        telethon_versiya = telethon.__version__
    except ImportError:
        telethon_version = "None"
    console.print("\n" + Panel(
        " ⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝ \n\n"
        f"[bold cyan]Version: [/][i]2.6[/]\n"
        f"[bold cyan]Python: [/][i]{python_versiya}[/]\n"
        f"[bold cyan]Telethon: [/][i]{telethon_versiya}[/]\n"
        f"[bold cyan]Dil: [/][i]{dil}[/]",
        width=60,
        justify="center"
    ) + "\n")                         
def tamamlandi (saniye):
   console.print(Panel(f"[bold green]Qurulum başa çatdı!\n[i]Botu {round(saniye)} saniyə içində qurdunuz.[/]\n\n[bold green]Bir neçə dəqiqə sonra hər hansı bir söhbətdə .alive yazaraq botu test edə bilərsiz. Xoş işlətmələr :)[/]"), justify="center")                         
                   
def rm_r(path):
    if not os.path.exists(path):
        return
    if os.path.isfile(path) or os.path.islink(path):
        os.unlink(path)
    else:
        shutil.rmtree(path)
