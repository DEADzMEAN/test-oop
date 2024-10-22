#!/usr/bin/env python3

import argparse
import glob
import logging
import os

def is_line_valid(data: str, number: int) -> bool:
    result: bool = True

    for symbol in data:
        if ord(symbol) > 0x7E:
            logging.error(f"Line {number}: invalid symbol '{symbol}'")
            result = False

    return result


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    logging.info("Started")

    parser = argparse.ArgumentParser(description="Config files checker")
    parser.add_argument("--input_dir", type=str, help="Input directory", required=True)
    parser.add_argument("--mask", type=str, help="Input mask", required=True)
    parser.add_argument("--recursive", action='store_true', help="Recursively search for files")

    # TODO: Replace --input_file with --input_dir, --mask, --recursive to do it like:
    # TODO: symbol_checker.py --input_dir=/.github/workflows --mask=*.yml --recursive

    args = parser.parse_args()

    path = args.input_dir
    mask = args.mask
    recursive = args.recursive

    logging.info(f"Searching in directory: {path} with mask: {mask}")

    search_pattern = os.path.join(path, '**', mask) if recursive else os.path.join(path, mask)
    valid: bool = True

    for input_file in glob.glob(search_pattern, recursive=recursive):
        logging.info(f"Checking file: {input_file}")
        with open(input_file, 'r', encoding='UTF-8') as f:
            index: int = 0
            for line in f:
                index += 1
                if not is_line_valid(line.rstrip(), index):
                    valid = False

    if not valid:
        logging.error("Errors found, consider checking your code")
        exit(1)

    logging.info("No errors found, you're breathtaking!")

