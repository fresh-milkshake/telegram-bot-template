## Features

- [x] User registration and access level management
- [x] Command handling using aiogram
- [x] User ORM model using peewee and sqlite
- [ ] Rotating logging using loguru
- [ ] Watcher for auto-restarting the bot on code changes
- [ ] Settings management using toml file
- [ ] Script for generating new project based on this template

## Requirements

- Python 3.10+
- Dependencies listed in `requirements.txt`

## Installation

1. `git clone https://github.com/fresh-milkshake/telegram-bot-template.git`
2. `cd telegram-bot-template`
3. `python -m venv .venv`
4. `.venv\Scripts\activate`
5. `pip install -r requirements.txt`

## Project Structure

- `bot/`: Main bot package
  - `handlers/`
    - `default.py`: Main handlers for bot operations
  - `tools/`
    - `decorators.py`: Decorators for user access levels
    - `helpers.py`: Helper functions
  - `models.py`: Database models using peewee ORM
  - `constants.py`: Constant values and configurations
  - `strings.py`: String constants for bot messages
- `main.py`: Entry point for the bot
- `requirements.txt`: List of project dependencies

## Usage

1. `python main.py`

