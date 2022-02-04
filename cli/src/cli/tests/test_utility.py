from utils import convert_file
from io import StringIO

def test_convert_success():
    out = StringIO()
    convert_file("./input.json", "USD", out=out)
    output = out.getvalue().split('\n')
    assert output[5] == '{"value":0.0,"currency":"USD"}'

def test_convert_fail_not_json():
    out = StringIO()
    convert_file("./tests/data/not_json.json", "JPY", out=out)
    output = out.getvalue().strip()
    assert "Invalid input" in output

def test_convert_fail_malformed_json():
    out = StringIO()
    convert_file("./tests/data/malformed.json", "USD", out=out)
    output = out.getvalue().split('\n')
    assert output[0] == '{"value":0.0,"currency":"USD"}'
    assert "Invalid input" in output[1]
    assert "Invalid input" in output[-1]