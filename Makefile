build:
	uv build

package-install:
	uv tool install dist/*.whl --force

install:
	uv sync

brain-games:
	uv run brain-games
