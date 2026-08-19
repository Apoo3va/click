"""
AI Software Engineering Assistant — Proposed Fix
Issue #3362: `HelpFormatter.write_usage` breaks options at a hyphen

The issue is caused by the default behaviour of Python's textwrap.TextWrapper used in click.formatting.HelpFormatter.write_usage, which splits tokens on hyphens when wrapping the usage line. The fix is to explicitly set `break_on_hyphens=False` when creating the TextWrapper inside `write_usage`. This change ensures that options such as `--foo-bar` are treated as a single token and are not broken across lines, regardless of the terminal width. The patch is applied to `src/click/formatting.py` in the `HelpFormatter.write_usage` method.
"""

# src/click/formatting.py
@@
-        wrapper = textwrap.TextWrapper(
-            width=self.width,
-            initial_indent='',
-            subsequent_indent='',
-            break_long_words=False,
-            break_on_hyphens=True,  # default behaviour
-        )
+        # Wrap the usage string.  Options that contain hyphens (e.g. ``--foo-bar``)
+        # should not be split across lines.  The default TextWrapper has
+        # ``break_on_hyphens=True`` which causes this behaviour.  Setting it to
+        # ``False`` preserves the option as a single token.
+        wrapper = textwrap.TextWrapper(
+            width=self.width,
+            initial_indent='',
+            subsequent_indent='',
+            break_long_words=False,
+            break_on_hyphens=False,
+        )
*** End Patch ***
