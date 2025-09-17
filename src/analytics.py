from typing import List, Optional


def chunk(values: List[int], size: int) -> List[List[int]]:
    """Split values into chunks of length `size`.
    
    The last chunk may be shorter if not divisible.
    If size <= 0, raise ValueError.
    """
    if size <= 0:
        raise ValueError("Chunk size must be positive")
    return [values[i:i+size] for i in range(0, len(values), size)]


def running_total(initial: int, changes: List[int]) -> List[int]:
    """Return the cumulative totals starting from initial,
    applying each change in order.
    """
    result = []
    total = initial
    for change in changes:
        total += change
        result.append(total)
    return result


def index_of_first_at_least(values: List[int], target: int) -> Optional[int]:
    """Return index of first element >= target, else None."""
    for i, v in enumerate(values):
        if v >= target:
            return i
    return None
