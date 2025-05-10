import pytest
from reports.payout import generate_report

@pytest.fixture
def sample_data():
    return [
        {"name": "Alice Johnson", "department": "Marketing", "hours_worked": 160, "hourly_rate": 50},
        {"name": "Bob Smith", "department": "Design", "hours_worked": 150, "hourly_rate": 40},
        {"name": "Carol Williams", "department": "Design", "hours_worked": 170, "hourly_rate": 60},
    ]

def test_generate_report_output(sample_data, capsys):
    generate_report(sample_data)
    captured = capsys.readouterr()
    assert "Design" in captured.out
    assert "Bob Smith" in captured.out
    assert "$6000" in captured.out
    assert "320" in captured.out
    assert "$16200" in captured.out