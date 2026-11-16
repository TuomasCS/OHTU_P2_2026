# Copilot instructions for this repository

This repository is a collection of small Python coursework projects grouped by week (`viikko1/`, `viikko2/`, `viikko3/`). Each project has its own `pyproject.toml`, dependencies, and tests. Work in the relevant project directory rather than assuming a single monolithic application.

## Build, test, and lint commands

There is no repo-level build or test command. Use the nearest project directory as the source of truth.

For the active web-login project in `viikko3/login`:

- Install dependencies: `cd viikko3/login && uv sync --group dev`
- Install the Browser library browser: `cd viikko3/login && uv run rfbrowser install chromium`
- Start the Flask app: `cd viikko3/login && uv run python3 src/index.py`
- App URL: `http://localhost:5001/ping` should return `Pong`
- Run the full Robot suite: `cd viikko3/login && uv run robot src/tests`
- Run a single Robot suite: `cd viikko3/login && uv run robot src/tests/login.robot`
- Run headless browser tests: `cd viikko3/login && uv run robot --variable HEADLESS:true src/tests`

For other weekly projects in this repo, use the project-local commands instead of a root-level runner. Typical examples:

- `cd viikko1/riippuvuuksien-injektointi && uv run pytest`
- `cd viikko1/riippuvuuksien-injektointi && uv run pytest src/tests/laskin_test.py`
- `cd viikko1/nhl-statistics && uv run pytest`
- `cd viikko2/nhl-reader && uv run pylint src`
- `cd viikko2/uv-web && uv run pytest`

## High-level architecture

This repo is organized by coursework week, not by business domain:

- `viikko1/`: small Python exercises, usually unit-test driven.
- `viikko2/`: CLI/data-reader projects and lint-friendly Python code.
- `viikko3/`: Flask web apps and Robot Framework browser tests.

Within each project, the structure is intentionally lightweight:

- `src/` holds application code.
- `src/tests/` contains automated tests.
- `src/entities/` contains domain models.
- `src/repositories/` contains storage/in-memory data access.
- `src/services/` contains business logic and validation.
- `src/templates/` contains Flask templates for the UI.

For the login app specifically (`viikko3/login`):

- `src/app.py` defines the Flask routes and request handling.
- `src/services/user_service.py` validates usernames/passwords and enforces uniqueness.
- `src/repositories/user_repository.py` stores users in memory and exposes lookup/create/delete helpers.
- `src/entities/user.py` defines the `User` model.
- `src/AppLibrary.py` provides custom Robot Framework keywords used by the acceptance tests.
- `src/tests/resource.robot` contains shared Robot variables and browser setup for the login/register flows.

The codebase favors explicit service-layer validation and simple in-memory repositories over databases or heavier frameworks. The app is designed for coursework exercises, not for production use.

## Key conventions

- Keep work scoped to the active project directory. Do not assume shared state across different `viikko*` folders.
- Match the project’s existing naming and structure before introducing new layers or abstractions.
- Use the project-local `pyproject.toml` as the authority for dependencies and tooling.
- Prefer the smallest relevant validation command: a single test file or a single Robot suite before broader runs.
- In `viikko3/login`, always run Python and Robot commands with `uv run` and do not invoke bare `python3` or `robot` directly.
- The login app listens on port `5001`; if you change Python code, restart the server so the Flask app reflects the new version.
- Browser tests use Robot Framework with the Browser library (Playwright), not SeleniumLibrary.
- Use Browser keyword syntax with the keyword name and arguments separated by at least two spaces, for example `Click  button >> text=Register`.
- Shared Robot keywords and variables belong in `src/tests/resource.robot`, not in individual test files.
- The login tests start from a known state via `POST /tests/reset`; `Reset Application` clears the in-memory repository and `Create User` creates `kalle` / `kalle123`.
- Validation messages are part of the assignment contract. Preserve the exact strings in `UserService.validate()` because the acceptance tests assert them:
  - `Username and password are required`
  - `Username must be at least 3 characters long`
  - `Password must be at least 8 characters long`
  - `User with username <username> already exists`
  - `Invalid username or password`
- `password_confirmation` is not currently enforced in the app logic unless the task explicitly asks for it.
- Several exercise names and messages are intentionally in Finnish (for example `kalle`, `ohtu`), so preserve the existing vocabulary and conventions unless a task specifically requires otherwise.

## WebLogin project notes

This project is the Flask login/register exercise in `viikko3/login`:

- `src/app.py` handles GET/POST routes for `/`, `/login`, `/register`, `/welcome`, `/ohtu`, `/logout`, and `/tests/reset`.
- `src/services/user_service.py` is the validation and authentication layer.
- `src/repositories/user_repository.py` is a simple in-memory repository.
- `src/templates/` stores the HTML pages and layouts for the app.
- Robot tests live under `src/tests/` and exercise the browser flows end to end.

The project is intentionally small and educational; it is not a production monorepo and should not be treated as one.
