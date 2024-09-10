from src.decorators import log


def test_log_success(capsys):
    @log()
    def add(a, b):
        return a + b

    add(2, 3)

    captured = capsys.readouterr()
    assert captured.out == "my_function is ok\n\n"


def test_log_filename_success():
    @log(filename="mylog.txt")
    def multiply(a, b):
        return a * b

    multiply(5, 3)

    with open("mylog.txt", "r") as f:
        assert f.readlines()[-1] == "my_function is ok\n"
