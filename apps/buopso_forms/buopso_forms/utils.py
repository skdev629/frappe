import frappe


def update_workspace():
    """Auto-update Buopso Forms workspace with grouped DocTypes, Reports, Dashboards"""

    # --- Collect DocTypes ---
    if not frappe.db.exists("Workspace", "Buopso Forms"):
        return  # exit early
    masters = frappe.get_all(
        "DocType", filters={"module": "Buopso Forms", "custom": 0}, pluck="name"
    )
    custom_forms = frappe.get_all(
        "DocType", filters={"module": "Buopso Forms", "custom": 1}, pluck="name"
    )

    # --- Collect Reports ---
    reports = frappe.get_all("Report", filters={"module": "Buopso Forms"}, pluck="name")

    # --- Collect Dashboards ---
    dashboards = frappe.get_all(
        "Dashboard", filters={"module": "Buopso Forms"}, pluck="name"
    )

    # --- Build Workspace Content ---
    content = []

    if masters or custom_forms:
        content.append(
            {
                "type": "card",
                "label": "Masters",
                "links": [
                    {"type": "doctype", "name": dt, "label": dt}
                    for dt in masters + custom_forms
                ],
            }
        )

    if reports:
        content.append(
            {
                "type": "card",
                "label": "Reports",
                "links": [
                    {"type": "report", "name": rpt, "label": rpt} for rpt in reports
                ],
            }
        )

    if dashboards:
        content.append(
            {
                "type": "card",
                "label": "Dashboards",
                "links": [
                    {"type": "dashboard", "name": db, "label": db} for db in dashboards
                ],
            }
        )

    # --- Fetch Workspace ---
    ws = frappe.get_doc("Workspace", "Buopso Forms")

    ws.content = frappe.as_json(content)
    ws.save(ignore_permissions=True)

    frappe.db.commit()
    frappe.clear_cache()
