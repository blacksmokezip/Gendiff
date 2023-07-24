from gendiff.parser import parse

url = 'https://jsonplaceholder.typicode.com/todos/1'
path = './tests/fixtures/before.json'

def test_open_from_url():
    result = parse(url)
    assert result == {
        "userId": 1,
        "id": 1,
        "title": "delectus aut autem",
        "completed": False
    }


def test_open_file():
    result = parse(path)
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
