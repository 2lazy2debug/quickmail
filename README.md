# quickmail

A CLI client for M365 Exchange

## Tech Stack

- **Python**: >=3.13
- **exchangelib**: Exchange Web Services (EWS) client library
- **Poetry**: Dependency management and packaging
- **pytest**: Testing framework
- **mypy**: Static type checking
- **black**: Code formatting
- **flake8**: Code linting

## Setup

1. Install Poetry:
   ```bash
   curl -sSL https://install.python-poetry.org | python3 -
   ```

2. Clone the repository:
   ```bash
   git@github.com:2lazy2debug/quickmail.git
   cd quickmail
   ```

3. Install dependencies:
   ```bash
   poetry install
   ```

4. Activate the virtual environment:
   ```bash
   poetry shell
   ```

## Development

- **Format code**: `poetry run black .`
- **Lint code**: `poetry run flake8`
- **Type check**: `poetry run mypy .`
- **Run tests**: `poetry run pytest`

## License

MIT