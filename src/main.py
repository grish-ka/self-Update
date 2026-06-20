import argparse
from loguru import logger


def main():
    logger.add("./logs/self-Update_{time}.log", level="INFO", retention="1 days", rotation="500 MB", compression="zip")
    parser = argparse.ArgumentParser(description="Update itself")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    parser.add_argument("--version", action="version", version="self-Update 1.0.0")
    parser.add_argument("--text", "-t", type=str, help="Text to display", default="Hello, World!")
    args = parser.parse_args()

    # Your update logic here
    if args.verbose:
        logger.remove()
        logger.add("./logs/self-Update_{time}.log", level="DEBUG", retention="1 days", rotation="500 MB", compression="zip")

    logger.info("System loaded successfully.")
    logger.info(f"TEXT: {args.text}")

if __name__ == "__main__":
    main()