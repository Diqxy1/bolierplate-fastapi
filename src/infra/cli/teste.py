import typer

app = typer.Typer()

@app.command()
def validations():
    print('aaaaaa')
    typer.secho('Não trava pelo amor de deus')