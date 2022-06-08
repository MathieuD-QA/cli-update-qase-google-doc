import typer
from qase.client_qase import Qase
from sheet.client_google import Sheet

qase_client = Qase()
sheet = Sheet()
app = typer.Typer()


@app.command("get_test_run_id")
def qase():
    result_qase = qase_client.get_test_run_id()
    print(result_qase)
    sheet.updata_multiple_value(result_qase)


@app.command("hello world")
def home():
    typer.echo("hello world")


if __name__ == "__main__":
    app()
