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

## WebLogin (`viikko3/login`)

Apply these instructions only when working in `viikko3/login`:

- This is a `uv` project. Run Python and Robot Framework commands with the `uv run` prefix; do not run `python3` or `robot` directly.
- Install dependencies with `uv sync`, then install the Browser library's Chromium browser with `uv run rfbrowser install chromium`.
- The app uses Flask and a simple layered architecture: routes and UI are in `src/app.py`, templates in `src/templates/`, business logic in `src/services/user_service.py`, in-memory persistence in `src/repositories/user_repository.py`, and the `User` entity in `src/entities/user.py`. `src/AppLibrary.py` provides test keywords.
- Start the app from this project directory with `uv run python3 src/index.py`. It listens on port **5001**; `http://localhost:5001/ping` should return `Pong`. Restart the server after changing Python code if it has not reloaded the changes.
- Robot Framework acceptance tests are in `src/tests/`. Run them with `uv run robot src/tests` or run one suite, for example `uv run robot src/tests/register.robot`. The app must already be running on port 5001. Tests use a visible, slowed-down browser by default; run headless with `uv run robot --variable HEADLESS:true src/tests`.
- The suites are `home.robot`, `login.robot`, and `register.robot`; shared keywords and variables belong in `resource.robot`. Tests start from a known state: `Reset Application` clears users through `POST /tests/reset`, and `Create User` creates `kalle` / `kalle123`.
- Tests use the Browser library (Playwright), not SeleniumLibrary. Use Browser-library syntax, for example `Click  button >> text=Register`; `Click Button` is not a keyword. Separate Robot Framework keyword names from their arguments with at least two spaces. Put keywords shared by multiple suites in `resource.robot`, not in individual test files.
- Registration validation is in `UserService.validate(self, username, password, password_confirmation)` in `src/services/user_service.py`, called by `create_user` before saving. Preserve these exact `UserInputError` messages because the acceptance tests check the page text:

  | Rule | Error message |
  | --- | --- |
  | Username and password are required | `Username and password are required` |
  | Username must contain at least 3 characters | `Username must be at least 3 characters long` |
  | Password must contain at least 8 characters | `Password must be at least 8 characters long` |
  | Username is already in use | `User with username <username> already exists` |

- `check_credentials` raises `AuthenticationError` with `Invalid username or password` for a login failure. `app.py` displays these exceptions as flash messages. If changing a message, update the corresponding tests too.
- `password_confirmation` is currently not used by `validate`; do not assume confirmation matching is implemented unless adding it as part of the task. Other password requirements should likewise only be introduced when requested.

## Project-specific notes

The repository’s root README describes it as coursework for OHTU and links to the related exercise sources. The projects are intentionally small and educational: they are not meant to be treated like a production monorepo.
