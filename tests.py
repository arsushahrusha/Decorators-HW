import pytest
from task1 import logger as logger1
from task2 import logger as logger2

"""Тест task1"""
@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 2, 4),
        (4.3, 2.2, 6.5),
        (0, 0, 0),
    ]
)
def test_logger_writes_data_to_main_log(tmp_path, monkeypatch, a, b, expected):
    monkeypatch.chdir(tmp_path)

    @logger1
    def summator(x, y=0):
        return x + y

    result = summator(a, b)

    assert result == expected

    log_file = tmp_path / "main.log"
    assert log_file.exists()

    content = log_file.read_text(encoding="utf-8")
    assert "summator" in content
    assert str(expected) in content
    assert str(a) in content
    assert str(b) in content


"""Тест task2"""
@pytest.mark.parametrize(
    "filename, a, b, expected",
    [
        ("log_1.log", 2, 2, 4),
        ("log_2.log", 4.3, 2.2, 6.5),
        ("custom.log", 10, 0, 10),
    ]
)
def test_parametrized_logger_writes_to_selected_file(tmp_path, filename, a, b, expected):
    log_path = tmp_path / filename

    @logger2(str(log_path))
    def summator(x, y=0):
        return x + y

    result = summator(a, b)

    assert result == expected
    assert log_path.exists()

    content = log_path.read_text(encoding="utf-8")
    assert "summator" in content
    assert str(a) in content
    assert str(b) in content
    assert str(expected) in content