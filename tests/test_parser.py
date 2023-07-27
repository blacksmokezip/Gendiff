from gendiff.parser import parse, read_file, get_format

path = './tests/fixtures/before.json'


def test_open_file():
    result = parse(read_file(path), get_format(path))
    assert result == {
        "common": {
            "setting1": "Value 1",
            "setting2": "200",
            "setting3": True,
            "setting6": {
                "key": "value"
            }
        },
        "group1": {
            "baz": "bas",
            "foo": "bar"
        },
        "group2": {
            "abc": "12345"
        }
    }
