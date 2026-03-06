# SPDX-FileCopyrightText: 2026-present Mark Hall <mark.hall@work.room3b.eu>
#
# SPDX-License-Identifier: MIT
"""μTheme extension setup."""

from uedition_theme.ext import video


def setup(app):
    """Set up the uTheme extension."""
    video.setup(app)
