"""
AI Software Engineering Assistant — Proposed Fix
Issue #3362: `HelpFormatter.write_usage` breaks options at a hyphen

The issue can be resolved by modifying the `HelpFormatter.write_usage` function in the `click` library to prevent breaking options at hyphens. This can be achieved by setting the `break_on_hyphens` option of `textwrap.TextWrapper` to `False`. The `HelpFormatter` class is likely defined in `src/click/core.py`, and the `write_usage` method can be modified to create a `TextWrapper` instance with `break_on_hyphens=False`. This change will prevent options from being broken at hyphens when printing usage at the line break limit.
"""

from textwrap import TextWrapper

class HelpFormatter:
    def write_usage(self, ctx, formatter):
        wrapper = TextWrapper(width=78, break_on_hyphens=False)
        # ... rest of the method implementation ...
