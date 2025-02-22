"""Search selected text on Google."""

import tkinter as tk
import urllib.parse
import webbrowser

from porcupine import menubar, tabs


def google_search(tab: tabs.FileTab) -> None:
    try:
        selected_text = tab.textwidget.get("sel.first", "sel.last")
    except tk.TclError:
        # nothing selected
        return

    # Check multi line or text with only spaces
    if selected_text.strip() and "\n" not in selected_text:
        url = "https://www.google.com/search?q={}".format(urllib.parse.quote_plus(selected_text))
        webbrowser.open_new_tab(url)


def setup() -> None:
    menubar.add_filetab_command("Tools/Search selected text on Google", google_search)
