import frappe
import json


@frappe.whitelist(allow_guest=True)
def delivery_report():
    raw_body = frappe.request.get_data(as_text=True)
    # Try parsing JSON
    try:
        payload = json.loads(raw_body)
    except Exception:
        payload = dict(frappe.local.form_dict)

    # Insert into MSG91 Delivery Log
    try:
        doc = frappe.get_doc(
            {
                "doctype": "MSG91 Delivery Log",
                "message_id": payload.get("requestId") or payload.get("messageId"),
                "status": int(payload.get("status", 0)),
                "full_data": json.dumps(payload),
            }
        )
        doc.insert(ignore_permissions=True, ignore_mandatory=True)
        frappe.db.commit()
    except Exception as e:
        frappe.log_error(title="MSG91 Webhook Insert Error", message=str(e))

    return {"status": "ok"}
