"""Template for building a `dlt` pipeline to ingest data from a REST API."""

import dlt
from dlt.sources.rest_api import rest_api_source
from dlt.sources.rest_api.typing import RESTAPIConfig


@dlt.source
def open_library_rest_api_source():
    """dlt source for Open Library search endpoint querying Harry Potter books."""
    config: RESTAPIConfig = {
        "client": {"base_url": "https://openlibrary.org"},
        "resources": [
            {
                "name": "search",
                "endpoint": {
                    "path": "/search.json",
                    "params": {"q": "harry potter"},
                    "paginator": {"type": "page_number", "page_param": "page", "base_page": 1, "total_path": None},
                },
            }
        ],
    }
    return rest_api_source(config)


pipeline = dlt.pipeline(
    pipeline_name='open_library_pipeline',
    destination='duckdb',
    # `refresh="drop_sources"` ensures the data and the state is cleaned
    # on each `pipeline.run()`; remove the argument once you have a
    # working pipeline.
    refresh="drop_sources",
    # show basic progress of resources extracted, normalized files and load-jobs on stdout
    progress="log",
)


if __name__ == "__main__":
    load_info = pipeline.run(open_library_rest_api_source())
    print(load_info)  # noqa: T201
