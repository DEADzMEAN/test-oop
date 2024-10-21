#!/usr/bin/env python3

import logging
import argparse
import os
import glob

logging.basicConfig(level=logging.INFO, format="%(asctime)s SymbolsChecker %(levelname)s %(message)s")


def is_line_valid(data: str, number: int) -> bool:
    result: bool = True

    for symbol in data:
        if ord(symbol) > 0x7E:
            logging.error(f"Line {number}: invalid symbol '{symbol}'")
            result = False

    return result


if __name__ == "__main__":
    logging.info("Started")

    parser = argparse.ArgumentParser(description="Config files checker")
    parser.add_argument("--input_file", type=str, help="Input file name", required=True)

    # TODO: Replace --input_file with --input_dir, --mask, --recursive to do it like:
    # TODO: symbol_checker.py --input_dir=/.github/workflows --mask=*.yml --recursive

    args = parser.parse_args()
    logging.info(f"Input file: {args.input_file}")
    path = '.github/workflows'
    valid: bool = True
    for filename in glob.glob(os.path.join(path, '**/*.yml')):   #чтобы не забыть , recursive=True не дружит с чётким путём но я оставил **/*yml
        with open(os.path.join(os.getcwd(), filename), 'r', encoding='UTF-8') as f:
            index: int = 0
            for line in f:
                index += 1
                if not is_line_valid(line.rstrip(), index):
                    valid = False

    if not valid:
        logging.error("Errors found, consider checking your code")
        exit(1)

    logging.info("No errors found, you're breathtaking!")
#    with open(args.input_file, 'r', encoding='UTF-8') as f:


