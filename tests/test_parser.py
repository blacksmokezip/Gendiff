from gendiff.parser import parse

url = 'https://jsonplaceholder.typicode.com/todos/1'


def test_open_from_url():
    result = parse(url)
    assert result == {
        "userId": 1,
        "id": 1,
        "title": "delectus aut autem",
        "completed": False
    }