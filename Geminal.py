import google.generativeai as genai
from rich.console import Console
from rich.markdown import Markdown
from rich.rule import Rule
import os

# Substitua pela sua chave REAL
API_KEY = "COLE_SUA_API_KEY_AQUI" 

# Configura o modelo
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-2.5-flash') 
chat = model.start_chat(history=[])

console = Console()

def main():
    console.clear()
    console.print(Rule("[bold blue]Chat com Gemini (Terminal)[/]", style="blue"))
    console.print("[italic grey50]Digite 'sair' para encerrar.[/]\n")

    while True:
        try:
            
            user_input = console.input("[bold green]Você ❯ [/]")
            
            if user_input.strip().lower() in ['sair', 'exit', 'quit']:
                console.print("\n[bold red]Encerrando... Até mais![/]")
                break
            
            if not user_input:
                continue

            with console.status("[bold yellow]Gemini está pensando...", spinner="dots"):
                response = chat.send_message(user_input)

            console.print()
            console.print(Rule(style="blue"))
            
            md = Markdown(response.text)
            console.print(md)
            
            console.print(Rule(style="blue"))
            console.print()

        except Exception as e:
            console.print(f"\n[bold red]Erro:[/ {e}]")

if __name__ == "__main__":
    main()
