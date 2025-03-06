# /// script
# requires-python = ">=3.9"
# dependencies = [
#     "duckdb==1.1.1",
#     "marimo",
#     "polars==1.18.0",
#     "pyarrow==18.1.0",
#     "requests==2.32.3",
#     "sqlglot==26.7.0",
# ]
# ///

import marimo

__generated_with = "0.11.14"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        # Connect to SQLite

        You can use marimo's SQL cells to read from and write to SQLite databases.

        The first step is to attach a SQLite database. We attach to a sample database in a read-only mode below.

        For advanced usage, see [duckdb's documentation](https://duckdb.org/docs/extensions/sqlite).
        """
    )
    return


@app.cell(hide_code=True)
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _(mo):
    mo.md(r"""Download chinook sqlite database if required""")
    return


@app.cell(hide_code=True)
def _():
    def download_sample_data():
        import os
        import requests

        url = "https://github.com/lerocha/chinook-database/raw/master/ChinookDatabase/DataSources/Chinook_Sqlite.sqlite"
        filename = "Chinook_Sqlite.sqlite"
        if not os.path.exists(filename):
            print("Downloading the Chinook database ...")
            response = requests.get(url)
            with open(filename, "wb") as f:
                f.write(response.content)
        else:
            print("Chinook database already downloaded")

    download_sample_data()
    return (download_sample_data,)


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "Tip: Creating SQL Cells": mo.md(
                f"""
                Create a SQL cell in one of two ways:

                1. Click the {mo.icon("lucide:database")} `SQL` button at the **bottom of your notebook**
                2. **Right-click** the {mo.icon("lucide:circle-plus")} button to the **left of a cell**, and choose `SQL`.

                In the SQL cell, you can query dataframes in your notebook as if
                they were tables — just reference them by name.
                """
            )
        }
    )
    return


@app.cell
def _(INFORMATION_SCHEMA, TABLES, mo):
    table_names = mo.sql(
        f"""
        -- Boilerplate: detach the database so this cell works when you re-run it
        DETACH DATABASE IF EXISTS chinook;

        -- Attach the database; omit READ_ONLY if you want to write to the database.
        ATTACH 'Chinook_Sqlite.sqlite' as chinook (TYPE SQLITE, READ_ONLY);

        -- This query lists all the tables in the Chinook database
        SELECT table_name FROM INFORMATION_SCHEMA.TABLES where table_catalog == 'chinook';
        """
    )
    return chinook, table_names


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Once the database is attached, you can query it with SQL. For example, the next cell computes the average track length of each composer in the chinook database.""")
    return


@app.cell
def _(chinook, mo, track):
    _df = mo.sql(
        f"""
        SELECT composer, MEAN(Milliseconds) as avg_track_ms from chinook.track GROUP BY composer ORDER BY avg_track_ms DESC;
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        f"""
        You can explore the schemas of all your tables at a glance in the **data sources panel**: click
        the {mo.icon("lucide:database")} icon in the left sidebar to open it.
        """
    )
    return


app._unparsable_cell(
    r"""
    You can also query the data using python
    """,
    name="_"
)


@app.cell
def _(chinook, mo, track):
    track = mo.sql(
        f"""
        SELECT * FROM chinook.track
        """
    )
    return (track,)


@app.cell
def _(track):
    import polars as pl

    (
    track.group_by("Composer")
     .agg(pl.col("Milliseconds").mean().alias("avg_track_ms"))
     .sort("avg_track_ms", descending=True)
    )

    return (pl,)


if __name__ == "__main__":
    app.run()
