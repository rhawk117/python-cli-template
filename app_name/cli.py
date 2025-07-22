import argparse


def add_cli_arguments(app: argparse.ArgumentParser) -> None:
    app.add_argument("---name", type=str, required=True)


def create_cli_app() -> argparse.ArgumentParser:
    app = argparse.ArgumentParser(
        description="CLI for app-name",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    add_cli_arguments(app)
    return app


def run(*, name: str) -> None:
    print(f"Hello, {name}!")


def main() -> None:
    app = create_cli_app()

    args = app.parse_args()
    run(name=args.name)
