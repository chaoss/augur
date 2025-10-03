from typing import Any, Callable, Optional
from augur.application.db.util import catch_operational_error

def execute_session_query(query: Any, query_type: str = "all") -> Any:
    """
    Executes an SQLAlchemy ORM query with retries on OperationalError.
    
    Args:
        query: SQLAlchemy ORM query object.
        query_type: One of 'all', 'one', 'first'.
    
    Returns:
        Query result according to query_type.
    """
    func: Optional[Callable[[], Any]] = None

    if query_type == "all":
        func = query.all
    elif query_type == "one":
        func = query.one
    elif query_type == "first":
        func = query.first
    else:
        raise Exception(f"ERROR: Unsupported query type '{query_type}'")

    return catch_operational_error(func)
