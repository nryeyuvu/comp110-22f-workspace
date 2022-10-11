"""Example implementing a list utility function."""

# Function name: contains
# We will have 2 parameters: neetdle (str), haystack (list[str])
# Return type bool
def contains(needle: str, haystack: list[str]) -> bool:
    # Gameplan:
    # 1. Starts with the first index
    i: int = 0
    # 2. Loop through every index          
    while i < len(haystack):
    #   2.A Test if item at index equal to needle
    #   We found it! No more work to do!
        if needle == haystack[i]:
    #       2.B True Return True! We Found it!
            return True
        i += 1
    # 3. Return False
    # We tries searching each item and came up short!
    return False