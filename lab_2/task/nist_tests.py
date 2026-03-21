import argparse


def parse_arguments() -> argparse.Namespace:
    """
    Adds and parses command-line arguments
    """
    parser = argparse.ArgumentParser(description="Template.")
    parser.add_argument('--Placeholder', '-p', default='Placeholder.txt', help='Placeholder')
    return parser.parse_args()


def main() -> None:
    """
    Main function
    """
    args = parse_arguments()


if __name__ == "__main__":
    main()
