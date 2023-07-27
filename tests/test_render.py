from gendiff.gen_diff import gendiff
from gendiff.render import nested_renderer, json_renderer, plain_renderer
from gendiff.parser import parse, read_file


file1 = parse(read_file('./tests/fixtures/file1.json'), 'json')
file2 = parse(read_file('./tests/fixtures/file2.json'), 'json')
diff = gendiff(file1, file2)


def test_nested_renderer():
    result = nested_renderer.render(diff).replace(' ', '')
    with open('./tests/fixtures/nested') as f:
        test_str = f.read().replace(' ', '')
    assert result == test_str


def test_json_renderer():
    result = json_renderer.render(diff)
    with open('./tests/fixtures/json') as f:
        test_str = f.read()
    assert result == test_str


def test_plain_renderer():
    result = plain_renderer.render(diff).strip()
    with open('./tests/fixtures/plain') as f:
        test_str = f.read()
    assert result == test_str
