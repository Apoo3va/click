"""
AI Software Engineering Assistant — Proposed Fix
Issue #3362: `HelpFormatter.write_usage` breaks options at a hyphen

Modify the HelpFormatter.write_usage method to use a custom TextWrapper that disables hyphen breaking (break_on_hyphens=False). This ensures options containing hyphens are wrapped as a single word. The change is applied in src/click/formatting.py where write_usage constructs the wrapper. No other parts of the code need alteration.
"""

class HelpFormatter:
    # ... existing code ...
    def write_usage(self, prog, args, prefix="Usage: "):
        """Write the usage line.

        The original implementation used ``textwrap.TextWrapper`` with the
        default ``break_on_hyphens=True`` which caused options such as
        ``--long-option`` to be split at the hyphen when the line wrapped.
        To preserve the option as a single token we create a wrapper with
        ``break_on_hyphens=False``.
        """
        # Build the usage string
        usage = f"{prefix}{prog} {args}\n"
        # Use a TextWrapper that does not break on hyphens
        wrapper = textwrap.TextWrapper(
            width=self.width,
            initial_indent="",
            subsequent_indent="",
            break_long_words=True,
            break_on_hyphens=False,
        )
        # Wrap the usage line respecting the width
        wrapped = wrapper.fill(usage.rstrip())
        self.write_paragraph()
        self.write_text(wrapped)
        self.write_paragraph()

