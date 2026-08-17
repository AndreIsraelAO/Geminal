from rich.console import Console
from rich.markdown import Markdown
from rich.rule import Rule
import os
from google import genai
from google.genai import errors

MODEL_NAME = "gemini-2.5-flash"

console = Console()


def create_chat():
    api_key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise RuntimeError(
            "Defina GEMINI_API_KEY (ou GOOGLE_API_KEY) antes de executar."
        )

    client = genai.Client(api_key=api_key)
    return client.chats.create(model=MODEL_NAME)


def main():
    try:
        chat = create_chat()
    except Exception as e:
        console.print(f"[bold red]Erro de configuração:[/] {e}")
        return

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

        except errors.APIError as e:
            console.print(f"\n[bold red]Erro da API Gemini:[/] {e}")
        except Exception as e:
            console.print(f"\n[bold red]Erro:[/] {e}")

if __name__ == "__main__":
    main()
