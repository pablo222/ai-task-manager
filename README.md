# AI Task Manager

A simple AI-powered task manager built with **Python**, **Google Agent Development Kit (ADK)**, and **Gemini via Vertex AI**.

The agent uses Python functions as tools to manage an in-memory task list through natural-language requests.

## Features

- Add a task
- List tasks
- Mark a task as completed
- Remove a task
- Handle invalid task numbers

## Tech stack

- Python
- Google ADK
- Gemini (`gemini-3.1-flash-lite`) on Vertex AI
- pytest

## Project structure

```text
ai-task-manager/
├── .env.example
├── .gitignore
├── README.md
├── task_manager.py
├── test_task_manager.py
└── task_manager_agent/
    ├── __init__.py
    └── agent.py
```

## Prerequisites

- Python and `pip`
- A Google Cloud project with billing enabled and the Vertex AI API enabled
- Google Cloud CLI (`gcloud`) for local authentication

## Local setup

Clone the repository and enter the project directory. Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
python -m pip install google-adk pytest
```

Authenticate to Google Cloud using Application Default Credentials (ADC):

```bash
gcloud auth application-default login
gcloud auth application-default set-quota-project YOUR_GCP_PROJECT_ID
```

Set the environment variables in your terminal (see `.env.example` for reference):

```bash
export GOOGLE_GENAI_USE_VERTEXAI=TRUE
export GOOGLE_CLOUD_PROJECT=YOUR_GCP_PROJECT_ID
export GOOGLE_CLOUD_LOCATION=eu
```

> `.env.example` is documentation only. This project does not automatically load `.env` files. The example uses the `eu` location, which was used during development; model availability may vary by location and project.

## Run the agent

From the project root, start the ADK development UI:

```bash
adk web
```

Open the local URL shown in the terminal, select `task_manager_agent`, and try requests such as:

- `Add a task: Learn Python`
- `Show me all my tasks`
- `Complete task number 1`
- `Remove task number 1`

## Run tests

The CRUD functions are covered by unit tests that do **not** call Gemini or Vertex AI:

```bash
python -m pytest -v
```

## Limitations

- Tasks are stored in a Python list in memory and are lost when the process restarts.
- The agent does not support priorities, deadlines, or reminders.
- The application is a learning project and is not production-ready.

## CI/CD

GitHub Actions integration is planned to run pytest automatically on pushes and pull requests.
