from src import train
from click.testing import CliRunner

# Initialize runner
runner = CliRunner()


def test_cli_command():
    result = runner.invoke(train, 'data/processed/train.csv data/processed/test.csv models/model.clf reports/metrics.json')
    assert result.exit_code == 0
