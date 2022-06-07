import typer
from qase.client_qase import Qase

qase_client = Qase()
app = typer.Typer()


@app.command("get_test_run_id")
def qase():
    qase_client.get_test_run_id()


@app.command("hello world")
def home():
    typer.echo("hello world")

if __name__ == "__main__":
    app()
