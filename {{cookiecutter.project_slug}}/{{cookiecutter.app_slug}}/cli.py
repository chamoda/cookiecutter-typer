import typer

app = typer.Typer()


@app.callback()
def callback():
    """
    Python CLI Template
    """
    pass


@app.command()
def command1(name: str):
    """
    Command1
    """
    print(name)
