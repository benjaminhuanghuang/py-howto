from argparse import ArgumentParser


def main():
    ap = ArgumentParser()
    ap.add_argument('-v', '--verbose', default=False, action='store_true', help='Increase verbosity')
    ap.add_argument('-n', '--number', type=int, default=1, help='The number of times to greet NAME')
    ap.add_argument('name', help='The person to greet')

    args = ap.parse_args()

    for index in range(args.number):
        print "Hello", args.name, '!'

    if args.verbose:
        print "I've finished now."



if __name__ == '__main__':
    main()

# argparse_demo.py -n2 aaa
