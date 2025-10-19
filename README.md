# FastAPI + SvelteKit Starter

This is a full-stack web application template using FastAPI for the backend and SvelteKit for the frontend.

## Getting Started

- First clone the repository:
```bash
git clone <repository-url>
cd fastapi-sveltekit-starter
```

### Option 1: VS Code Devcontainer (Recommended)

The fastest way to get started is using VS Code's devcontainer feature:

1. Install prerequisites:
   - [VS Code](https://code.visualstudio.com/)
   - Docker
   - [Dev Containers Extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)
2. Open the project and click "Reopen in Container" when prompted
3. The container will set up everything you need for development

Note: Always run `docker compose` commands in a terminal on your host machine, not inside the devcontainer.

### Option 2: Manual Setup

- Install prerequisites:
    - Docker
    - Node.js 24+
    - Python 3.13+
    - uv package installer (`curl -LsSf https://astral.sh/uv/install.sh | sh`)

- #### Backend (FastAPI)

1. Create a virtual environment:
```bash
cd backend
uv venv --python 3.13
source .venv/bin/activate
```

2. Install dependencies:
```bash
uv pip install -r requirements.txt
```

- #### Frontend (SvelteKit)

    1. Install dependencies:
        ```bash
        cd frontend
        npm install
        ```

    2. Start the development server:
        ```bash
        npm run dev
        ```

-  Start the development environment with Docker:

The services will be available at:
- Frontend: http://localhost:3000
- Backend: http://localhost:8000

## Managing Python dependencies with uv

When adding or updating dependencies:

1. Edit [backend/pyproject.toml](backend/pyproject.toml)
   - Add runtime deps under `[project].dependencies`
   - Add dev-only deps under `[project.optional-dependencies].dev`

2. Recompile pinned requirements:
```bash
cd backend
uv pip compile pyproject.toml -o requirements.txt
uv pip compile pyproject.toml --extra dev -o requirements-dev.txt
```

3. Install:
```bash
uv pip install -r requirements.txt
# Or for dev environment:
uv pip install -r requirements-dev.txt
```

## Code Quality and Linting

### Backend (Python)

The backend uses **Ruff** for linting and formatting, and **Pyright** for type checking. Configuration is in [backend/pyproject.toml](backend/pyproject.toml).

#### Ruff

Ruff is an extremely fast Python linter and formatter that replaces tools like Flake8, isort, and Black.

**Run linting:**
```bash
cd backend
ruff check .
```

**Auto-fix issues:**
```bash
ruff check --fix .
```

**Format code:**
```bash
ruff format .
```

**VS Code Integration:**
The devcontainer automatically configures Ruff for format-on-save and auto-fix-on-save via the [Ruff extension](https://marketplace.visualstudio.com/items?itemName=charliermarsh.ruff).

#### Pyright

Pyright is a fast, feature-rich static type checker for Python.

**Run type checking:**
```bash
cd backend
pyright
```

**Configuration:**
Type checking is set to `strict` mode in [backend/pyproject.toml](backend/pyproject.toml). You can adjust the strictness level or enable/disable specific rules as needed.

### Frontend (SvelteKit/TypeScript)

The frontend uses **ESLint** for linting, **Prettier** for formatting, and **svelte-check** for type checking.

#### ESLint

**Run linting:**
```bash
cd frontend
npm run lint
```

Configuration is in [frontend/eslint.config.js](frontend/eslint.config.js).

#### Prettier

**Format code:**
```bash
cd frontend
npm run format
```

Configuration is in [frontend/prettier.config.js](frontend/prettier.config.js).

#### svelte-check

**Run type checking:**
```bash
cd frontend
npm run check
```

**VS Code Integration:**
The devcontainer automatically configures ESLint and Prettier for format-on-save via the [Svelte extension](https://marketplace.visualstudio.com/items?itemName=svelte.svelte-vscode).

## Git hooks (pre-commit)

This project uses pre-commit to run various hooks before each commit:
- **Backend**: Ruff (linting + formatting)
- **Frontend**: ESLint, Prettier, svelte-check
- **Security**: Gitleaks (secret detection)
- **General**: YAML/TOML validation, trailing whitespace, etc.

**Devcontainer**: pre-commit and the Git hook are installed automatically after the container is created.

**Local setup** (outside the Dev Container):

```bash
# Install pre-commit
pip install pre-commit  # or: uv pip install pre-commit

# Install frontend dependencies (required for frontend hooks)
cd frontend && npm install && cd ..

# Install the git hooks
pre-commit install

# Optional: run on all files immediately
pre-commit run --all-files
```


## Testing

### Backend
```bash
cd backend
pytest
```

## Building for Production

### Backend
```bash
cd backend
docker build -t fastapi-backend .
```

### Frontend
```bash
cd frontend
docker build -t sveltekit-frontend .
```

## Conventional Commits

Use Conventional Commits for all commit messages to keep history consistent and automatable.

Format:
- type(scope): short imperative summary

Common types:
- build, chore, ci, docs, feat, fix, perf, refactor, revert, style, test

Examples:
- feat(auth): add refresh token endpoint
- fix(api): handle 404 on user lookup
- docs(readme): add setup instructions

Enforcement:
- A commit-msg hook is configured via pre-commit.
