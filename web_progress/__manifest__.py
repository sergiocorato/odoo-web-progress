{
    "name": "Dynamic Progress Bar",
    "summary": """
        Progress bar for operations that take more than 5 seconds.
    """,
    "author": "Grzegorz Marczyński, Sergio Corato",
    "category": "Productivity",
    "website": "https://github.com/sergiocorato/odoo-web-progress",
    "version": "14.0.2.0.0",
    "depends": [
        "web",
        "bus",
        "base_import",
    ],
    "data": [
        "views/templates.xml",
        "security/ir.model.access.csv",
    ],
    "qweb": [
        "static/src/xml/progress_bar.xml",
        "static/src/xml/web_progress_menu.xml",
    ],
    "demo": [],
    "images": [
        "static/description/progress_bar_loading_compact.gif",
        "static/description/progress_bar_loading_cancelling.gif",
        "static/description/progress_bar_loading_systray.gif",
    ],
    "license": "LGPL-3",
    "installable": True,
}
