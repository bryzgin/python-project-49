build:
	uv build

package-install:
	uv tool install dist/*.whl --force

install:
	uv sync

brain-games:
	uv run brain-games

lint:
	uv run ruff check brain_games
