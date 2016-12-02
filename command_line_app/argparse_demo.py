from argparse import ArgumentParser


def main():
    ap = ArgumentParser()
    ap.add_argument('name', nargs='?')
    args = ap.parse_args()
    name = args.name or 'World'
    print "Hello", name, '!'


if __name__ == '__main__':
    main()

# argparse_demo.py --help

