from frappe import _


def get_data():
    return [
        {
            "module_name": "Buopso Forms",
            "color": "blue",
            "icon": "octicon octicon-file-directory",
            "type": "module",
            "label": _("Buopso Forms"),
        },
        {
            "label": _("Custom Documents"),
            "items": [
                {
                    "type": "doctype",
                    "name": "Custom Form",
                    "label": _("Custom Form"),
                    "description": _("Manage all custom forms."),
                },
                {
                    "type": "doctype",
                    "name": "Form Response",
                    "label": _("Form Response"),
                    "description": _("Responses collected from forms."),
                },
            ],
        },
    ]
