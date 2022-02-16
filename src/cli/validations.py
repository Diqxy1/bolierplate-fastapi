import typer

app = typer.Typer()

@app.command()
def teste():
    typer.secho('Teste não crasha pelo amor de deus')