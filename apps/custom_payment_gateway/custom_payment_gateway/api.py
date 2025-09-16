import frappe


@frappe.whitelist(allow_guest=True)
def payment_callback():
    """
    Endpoint for gateway to call after payment.
    Updates Payment Request status.
    """
    payment_id = frappe.form_dict.get("payment_id")
    if not payment_id:
        frappe.throw("Payment ID not provided")

    payment_request = frappe.get_doc("Payment Request", payment_id)
    gateway_class = frappe.get_attr(
        "custom_payment_gateway.payment_gateway.MyGateway"
    )()
    result = gateway_class.verify_payment(payment_request)

    if result.status == "success":
        payment_request.db_set("status", "Paid")
    else:
        payment_request.db_set("status", "Failed")

    return "OK"
