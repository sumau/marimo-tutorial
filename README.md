# marimo-tutorial

This tutorial is a whistlestop tour of [uv](https://docs.astral.sh/uv/), [marimo](https://marimo.io/) and [duckdb](https://duckdb.org/). It uses the [chinook sample database](https://www.sqlitetutorial.net/sqlite-sample-database/) and is based on the [connect_to_sqlite.py](https://github.com/marimo-team/marimo/blob/main/examples/sql/connect_to_sqlite.py) example.

1. Open VSCode from your dev laptop

2. [Install uv](https://docs.astral.sh/uv/getting-started/installation/) if you haven't already:

```
wget -qO- https://astral.sh/uv/install.sh | sh
```

3. Clone https://github.com/uktrade/marimo-tutorial.git

4. Run the python script:

```
uv run main.py
```

5. Comment out the comment block at the top of the python script and rerun it. It should fail. Revert your changes.

6. Create a uv venv, install marimo and activate it:

```
uv venv
uv sync
source .venv/bin/activate
```

8. Edit the python script as a notebook, running the dependencies in a sandbox:

```
marimo edit main.py
```

9. Explore the different types of cells; markdown, python and sql

10. Explore the helper panels on the left hand side

11. Explore the options in the drop down menu

12. Make a change to the notebook and save it, then have a look at the `main.py` diff
