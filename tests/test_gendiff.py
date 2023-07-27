from gendiff.constants import ADDED, CHANGED, UNCHANGED, NESTED, REMOVED
from gendiff.parser import parse, read_file
from gendiff.gen_diff import gendiff


before_dict = parse(read_file("./tests/fixtures/before.json"), 'json')
after_dict = parse(read_file("./tests/fixtures/after.json"), 'json')


def test_gendiff():
    result = gendiff(before_dict, after_dict)

    assert result == {
        "common": (NESTED, {
            "setting1": (UNCHANGED, "Value 1"),
            "setting2": (REMOVED, "200"),
            "setting3": (UNCHANGED, True),
            "setting4": (ADDED, "blah blah"),
            "setting5": (ADDED, {"key5": "value5"}),
            "setting6": (REMOVED, {"key": "value"})
        }),
        "group1": (NESTED, {
            "baz": (CHANGED, "bas", "bars"),
            "foo": (UNCHANGED, "bar")
        }),
        "group2": (REMOVED, {"abc": "12345"}),
        "group3": (ADDED, {"fee": "100500"})
    }
