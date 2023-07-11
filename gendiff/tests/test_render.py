from gendiff.gen_diff import gendiff
from gendiff.render import nested_renderer, json_renderer, plain_renderer
from gendiff.open import open_file


file1 = open_file('./gendiff/tests/fixtures/file1.json')
file2 = open_file('./gendiff/tests/fixtures/file2.json')
diff = gendiff(file1, file2)


def test_neted_renderer():
    result = nested_renderer.render(diff).replace(' ', '')
    with open('./gendiff/tests/fixtures/nested') as f:
        test_str = f.read().replace(' ', '')
    assert result == test_str


def test_json_renderer():
    result = json_renderer.render(diff)
    with open('./gendiff/tests/fixtures/json') as f:
        test_str = f.read()
    assert result == test_str


def test_plain_renderer():
    result = plain_renderer.render(diff).strip()
    with open('./gendiff/tests/fixtures/plain') as f:
        test_str = f.read()
    assert result == test_str
