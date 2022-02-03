#!/bin/python3
import os
import sys
import argparse

from utils import convert_file

parser = argparse.ArgumentParser(
    prog="Convertor",
    description="Converts a json file of currency values to the target currency",
)
parser.add_argument(
    "--target-currency", type=str, help="The target currency to convert to. Could be one of 'USD', 'EUR','JPY' [Default: USD]",
    default="USD",
)
parser.add_argument(
    "--file",
    type=str,
    help="The path to the input file consisting of per-line JSON currency values [Default: ./input.json]",
    default="input.json",
)

args = parser.parse_args()


target = args.target_currency.upper()
file_path = os.path.abspath(args.file)

if target not in ["USD", "EUR", "JPY"]:
    print("Invalid target currency | Must be one of: USD, EUR, JPY")
    exit(1)

if not os.path.exists(file_path):
    print(f"Invalid file path | File {file_path} does not exist")
    exit(1)

convert_file(file_path, target)
