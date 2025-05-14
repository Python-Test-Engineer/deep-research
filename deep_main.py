import asyncio
from dotenv import load_dotenv
from rich.console import Console
from rich.prompt import Prompt
import datetime
import random
from deep_coordinator import ResearchCoordinator

load_dotenv()

console = Console()


async def main() -> None:
    console.print("[bold cyan]Deep Research Tool[/bold cyan] - Console Edition")
    console.print("This tool performs in-depth research on any topic using AI agents.")

    # get the users query
    query = Prompt.ask("\n[bold]What would you like to research?[/bold]")

    if not query.strip():
        console.print("[bold red]Error:[/bold red] Please provide a valid query.")
        return

    research_coordinator = ResearchCoordinator(query)
    report = await research_coordinator.research()
    current_date = datetime.datetime.now()
    # Format the date as YYYY-MM-DD
    formatted_date = current_date.strftime("%Y-%m-%d")
    random_number = random.randint(1000, 9999)
    report_filename = f"./reports/research_report_{formatted_date}_{random_number}.md"
    with open(report_filename, "w") as f:
        f.write(report)


if __name__ == "__main__":
    asyncio.run(main())
