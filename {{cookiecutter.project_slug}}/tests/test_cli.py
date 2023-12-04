from typer.testing import CliRunner

from python_cli_template.cli import app

runner = CliRunner()


def test_app():
    result = runner.invoke(app, ["command1", "test"])
    assert result.exit_code == 0
    assert "test" in result.stdout
