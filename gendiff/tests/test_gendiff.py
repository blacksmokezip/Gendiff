from gendiff.gen_diff import generate_diff


file1 = './gendiff/tests/fixtures/file1.json'
file2 = './gendiff/tests/fixtures/file2.json'


def test_gendiff():
    result = generate_diff(file1, file2)

    assert result == {'- follow': False,
                      '  host': 'hexlet.io',
                      '- proxy': '123.234.53.22',
                      '- timeout': 50,
                      '+ timeout': 20,
                      '+ verbose': True}
