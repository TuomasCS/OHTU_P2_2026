# Copilot instructions for this repository

This repository is a collection of small Python exercise projects for different weeks (`viikko1/`, `viikko2/`, `viikko3/`). Each project has its own `pyproject.toml`, dependencies, and test setup. Treat the current task as belonging to one project directory rather than to a single monolithic app.

## Build, test, and lint commands

There is no root-level build or test command for the whole repository. Use the nearest project directory as the source of truth.

Common commands used in this repository:

- `cd viikko1/nhl-statistics && uv run pytest`
- `cd viikko1/riippuvuuksien-injektointi && uv run pytest`
- `cd viikko2/nhl-reader && uv run pylint src`
- `cd viikko2/uv-web && uv run pytest`
- `cd viikko3/login && uv run robot src/tests`
- `cd viikko3/hello-robot && uv run robot src/tests`

For a single test, run the specific file or Robot test instead of the full suite:

- `cd viikko1/riippuvuuksien-injektointi && uv run pytest src/tests/laskin_test.py`
- `cd viikko1/nhl-statistics && uv run pytest src/tests/statistics_service_test.py`
- `cd viikko3/login && uv run robot src/tests/login.robot`

If dependencies are not installed yet, run `uv sync --group dev` inside the project before executing the test or lint command.

## High-level architecture

This repo is organized by coursework week, not by feature domain:

- `viikko1/` contains small Python exercises and unit-test-driven tasks.
- `viikko2/` contains CLI and data reader projects, including a `pylint`-friendly codebase.
- `viikko3/` contains Flask and Robot Framework web-test projects.

Within each project, the code follows lightweight layered patterns:

- `src/` holds the application code.
- `src/tests/` contains test files.
- Domain entities are commonly placed under `src/entities/`.
- Data access logic sits in `src/repositories/`.
- Business logic sits in `src/services/`.
- The Flask apps in `viikko3/login` expose routes in `src/app.py` and rely on service/repository separation for login and registration flows.

The repository intentionally keeps business logic simple and explicit. Several examples are designed around dependency injection and in-memory storage rather than database persistence or frameworks beyond the assignment requirements.

## Key conventions

- Keep changes scoped to the active project directory; do not assume shared state across weeks.
- Match the project’s existing naming and structure (`StatisticsService`, `UserRepository`, `player_reader`, etc.) before introducing new abstractions.
- Use the project-local `pyproject.toml` as the authority for dependencies, Python version, and dev tooling.
- Python tests in this repo are often minimal and file-local. `*_test.py` names and `unittest.TestCase` are common in the earlier coursework.
- Robot Framework tests are written as `.robot` files using keyword-driven style (`Suite Setup`, `Test Setup`, `Resource`, etc.) and are often placed under `src/tests/`.
- Several tasks preserve Finnish naming and messages (for example `laskin`, `ohtu`, `kalle`) because they are course exercises. Preserve those conventions unless the task specifically calls for a behavior change.
- The architecture is intentionally simple: service layers validate input and repository layers manage storage. Prefer extending that pattern instead of introducing a new framework or cross-project abstraction.
- No repository-wide build system is configured; each weekly project is its own mini-application.

## Project-specific notes

The repository’s root README describes it as coursework for OHTU and links to the related exercise sources. The projects are intentionally small and educational: they are not meant to be treated like a production monorepo.
