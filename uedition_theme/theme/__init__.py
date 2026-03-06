# SPDX-FileCopyrightText: 2026-present Mark Hall <mark.hall@work.room3b.eu>
#
# SPDX-License-Identifier: MIT
"""μTheme theme setup."""

from pathlib import Path


def setup(app):
    """Set up the μTheme."""
    app.add_html_theme("uedition-theme", Path(__file__).resolve().parent)
