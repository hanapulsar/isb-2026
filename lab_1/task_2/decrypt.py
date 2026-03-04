import argparse
import os.path
import json

def load_json(path: str) -> dict:
    with open(path, 'r', encoding='utf-8') as file:
        return json.load(file)

def save_json(path: str, data: dict) -> None:
    with open(path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def main() -> None:

if __name__ == "__main__":
    main()
