import typer

app = typer.Typer()

@app.command()
def validations():
    i = 0
    while i <= 100000:
        typer.secho(f'{i}')
        i += 1