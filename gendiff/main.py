import argparse
from gendiff.gen_diff import generate_diff


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )

    parser.add_argument('first_file')
    parser.add_argument('second_file')

    parser.add_argument('-f', '--format', help='set format of output')

    args = parser.parse_args()

    diff = generate_diff(args.first_file, args.second_file)
    for key, value in diff.items():
        print("{0}: {1}".format(key, value))


if __name__ == '__main__':
    main()
