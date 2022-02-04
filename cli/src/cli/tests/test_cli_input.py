import os

def test_cli_entrypoint():
    exit_status = os.system("./convertor.py --help")
    assert exit_status == 0

def test_cli_invalid_input_file():
    exit_status = os.system("./convertor.py -f ./tests/data/input.json")
    assert exit_status == 256

def test_cli_invalid_input_target():
    exit_status = os.system("./convertor.py -t ABC")
    assert exit_status == 256

def test_cli_invalid_parameter():
    exit_status = os.system("./convertor.py -z")
    assert exit_status == 512