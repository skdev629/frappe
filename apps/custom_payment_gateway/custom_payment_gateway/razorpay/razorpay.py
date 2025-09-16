import frappe
from payments.payment_gateway import PaymentGatewayController


class RazorpayController(PaymentGatewayController):
    def validate_transaction_currency(self, currency):
        if currency != "INR":
            frappe.throw("Razorpay only supports INR transactions.")

    def get_payment_url(self, **kwargs):
        amount = kwargs.get("amount")
        reference_doc = kwargs.get("reference_doc")
        reference_docname = kwargs.get("reference_docname")

        # Replace with actual Razorpay API call later
        return f"https://razorpay.com/pay?amount={amount}&ref={reference_docname}"
