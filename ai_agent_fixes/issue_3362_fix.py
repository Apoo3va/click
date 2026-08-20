"""
AI Software Engineering Assistant — Proposed Fix
Issue #3362: `HelpFormatter.write_usage` breaks options at a hyphen

Modify the `wrap_text` helper to accept a `break_on_hyphens` flag (defaulting to True for backward compatibility). Then, in `HelpFormatter.write_usage`, call `wrap_text` with `break_on_hyphens=False` so that options containing hyphens are not split when the usage line is wrapped. This keeps existing behavior for other formatting paths while fixing the specific issue with usage lines.
"""

# src/click/formatting.py
@@
-def wrap_text(
-    body: str,
-    width: int,
-    *,
-    initial_indent: str = "",
-    subsequent_indent: str = "",
-    preserve_paragraphs: bool = False,
-    **kwargs: t.Any,
-) -> str:
-    """Wrap a string of text to a given width.
-
-    The function is a thin wrapper around :class:`textwrap.TextWrapper`.
-    """
-    wrapper = textwrap.TextWrapper(
-        width=width,
-        initial_indent=initial_indent,
-        subsequent_indent=subsequent_indent,
-        replace_whitespace=False,
-        drop_whitespace=False,
-        **kwargs,
-    )
-    return wrapper.fill(body)
+def wrap_text(
+    body: str,
+    width: int,
+    *,
+    initial_indent: str = "",
+    subsequent_indent: str = "",
+    preserve_paragraphs: bool = False,
+    break_on_hyphens: bool = True,
+    **kwargs: t.Any,
+) -> str:
+    """Wrap a string of text to a given width.
+
+    The function is a thin wrapper around :class:`textwrap.TextWrapper`.
+    ``break_on_hyphens`` controls whether words containing hyphens are
+    split when wrapping.  It defaults to ``True`` for backward
+    compatibility but can be overridden by callers.
+    """
+    wrapper = textwrap.TextWrapper(
+        width=width,
+        initial_indent=initial_indent,
+        subsequent_indent=subsequent_indent,
+        replace_whitespace=False,
+        drop_whitespace=False,
+        break_on_hyphens=break_on_hyphens,
+        **kwargs,
+    )
+    return wrapper.fill(body)
@@
     def write_usage(
         self,
         prog: str,
         args: str,
         prefix: str | None = None,
         *,
         width: int | None = None,
     ) -> None:
@@
-        self.write(
-            wrap_text(
-                args,
-                text_width,
-                initial_indent=usage_prefix,
-                subsequent_indent=indent,
-            )
-        )
+        self.write(
+            wrap_text(
+                args,
+                text_width,
+                initial_indent=usage_prefix,
+                subsequent_indent=indent,
+                break_on_hyphens=False,
+            )
+        )
*** End of File ***

