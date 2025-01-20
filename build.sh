#!/usr/bin/env bash
# Exit on error
# set -o errexit

curl -LsSf https://astral.sh/uv/install.sh | sh
source $HOME/.local/bin/env
uv sync

# # Convert static asset files
# uv run python3 manage.py collectstatic --no-input

# # Apply any outstanding database migrations
# uv run python3 manage.py migrate