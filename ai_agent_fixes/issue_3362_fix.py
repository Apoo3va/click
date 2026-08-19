"""
AI Software Engineering Assistant — Proposed Fix
Issue #3362: `HelpFormatter.write_usage` breaks options at a hyphen

The issue arises because Click’s HelpFormatter uses textwrap.TextWrapper with its default `break_on_hyphens=True`, causing options that contain hyphens (e.g., `--long-option`) to be split across lines. The formatter delegates line wrapping to the `wrap_text` method in `src/click/formatter.py`. By updating `wrap_text` to instantiate TextWrapper with `break_on_hyphens=False`, we preserve each option as a single token while still respecting the configured width. This change is isolated to the formatter module and does not affect other parts of Click.
"""

# src/click/formatter.py
@@
-    def wrap_text(self, text: str, width: int | None = None) -> list[str]:
-        """Wrap a string to the configured width."""
-        if width is None:
-            width = self.width
-        wrapper = textwrap.TextWrapper(width=width, replace_whitespace=False)
-        return wrapper.wrap(text)
+    def wrap_text(self, text: str, width: int | None = None) -> list[str]:
+        """Wrap a string to the configured width.
+
+        The default ``textwrap.TextWrapper`` splits words on hyphens, which
+        breaks command‑line options such as ``--long-option``.  To keep each
+        option intact, ``break_on_hyphens`` is explicitly set to ``False``.
+        """
+        if width is None:
+            width = self.width
+        wrapper = textwrap.TextWrapper(
+            width=width,
+            replace_whitespace=False,
+            break_on_hyphens=False,  # Preserve options containing hyphens
+        )
+        return wrapper.wrap(text)

