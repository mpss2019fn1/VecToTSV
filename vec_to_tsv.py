import argparse

from accessible_text_file import AccessibleTextFile


def main():
    parser = _initialize_parser()

    args = parser.parse_args()

    with open(args.output_vec, "w") as modelOut, open(args.output_meta, "w") as metaOut, open(
            args.input, "r") as inputFile:
        # skip header row
        next(inputFile)
        for line in inputFile:
            tokens = line.split(" ")
            without_word = "\t".join(tokens[1:])
            print(without_word, file=modelOut, end="")
            print(tokens[0], file=metaOut)


def _initialize_parser():
    general_parser = argparse.ArgumentParser(description='Named entity recognition')
    general_parser.add_argument("--input", help='.vec File containing trained word embeddings',
                                action=AccessibleTextFile)
    general_parser.add_argument("--output-vec", help='Filename for tsv containing vector information')
    general_parser.add_argument("--output-meta", help='Filename for tsv containing meta information')

    return general_parser


if __name__ == "__main__":
    main()
