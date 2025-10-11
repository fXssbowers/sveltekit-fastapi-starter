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
    - Python 3.14+
    - uv package installer (`curl -LsSf https://astral.sh/uv/install.sh | sh`)

- #### Backend (FastAPI)

1. Create a virtual environment:
```bash
cd backend
uv venv --python 3.14
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

## Testing

### Backend
```bash
cd backend
pytest
```

### Frontend
```bash
cd frontend
npm run check
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
