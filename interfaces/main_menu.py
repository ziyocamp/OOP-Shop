from rich.console import Console
from rich.panel import Panel
from rich import box

console = Console()

def home_manu():
    menu_text = """
[bold cyan]1.[/] 🔐 Kirish  
[bold cyan]2.[/] 📝 Ro'yxatdan o'tish  
[bold cyan]3.[/] ❌ Chiqish  
"""
    panel = Panel(
        menu_text,
        title="[bold magenta]🏠 HOME MENU",
        box=box.ROUNDED,
        border_style="bright_magenta"
    )
    console.print(panel)