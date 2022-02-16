import typer

app = typer.Typer()

@app.command()
def validations():
    i = 0
    while i >= 100000:
        typer.secho(i)
        i += 1