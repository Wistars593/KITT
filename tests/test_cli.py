from pathlib import Path

from kitt.cli import main


def test_cli_validate_reports_summary(capsys) -> None:
    fixture = Path("fixtures/can/synthetic/sample-log.jsonl")

    exit_code = main([str(fixture)])
    captured = capsys.readouterr()

    assert exit_code == 0
    assert "Frame count: 3" in captured.out
    assert "Buses seen: can-b-sim, can-c-sim" in captured.out


def test_cli_validate_reports_errors_for_invalid_log(tmp_path, capsys) -> None:
    fixture = tmp_path / "invalid.jsonl"
    fixture.write_text("{bad json}\n", encoding="utf-8")

    exit_code = main([str(fixture)])
    captured = capsys.readouterr()

    assert exit_code == 1
    assert "error:" in captured.err
