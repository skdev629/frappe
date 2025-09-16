import frappe
from frappe.payment_gateway.doctype.payment_gateway.payment_gateway import (
    PaymentGateway,
)


class MyGateway(PaymentGateway):
    def get_payment_url(self, payment_request):
        """
        Constructs the payment URL for redirection.
        """
        gateway_doc = frappe.get_doc("Custom Payment Gateway", "My Gateway")
        amount = payment_request.amount
        ref = payment_request.name
        # Example URL, replace with your gateway's actual payment URL
        return f"https://sandbox.gateway.com/pay?amount={amount}&ref={ref}&key={gateway_doc.api_key}"

    def verify_payment(self, payment_request):
        """
        Verifies payment status from gateway API.
        """
        import requests

        gateway_doc = frappe.get_doc("Custom Payment Gateway", "My Gateway")
        response = requests.get(
            f"https://sandbox.gateway.com/verify?ref={payment_request.name}&key={gateway_doc.api_key}"
        ).json()

        if response.get("status") == "success":
            return frappe._dict({"status": "success"})
        return frappe._dict({"status": "failed"})
