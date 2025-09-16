app_name = "buopso_forms"
app_title = "Buopso Forms"
app_publisher = "Sangeet Kumar"
app_description = "Customizable and sharable forms"
app_email = "sangeet.kumar@buopso.com"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "buopso_forms",
# 		"logo": "/assets/buopso_forms/logo.png",
# 		"title": "Buopso Forms",
# 		"route": "/buopso_forms",
# 		"has_permission": "buopso_forms.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/buopso_forms/css/buopso_forms.css"
# app_include_js = "/assets/buopso_forms/js/buopso_forms.js"

# include js, css files in header of web template
# web_include_css = "/assets/buopso_forms/css/buopso_forms.css"
# web_include_js = "/assets/buopso_forms/js/buopso_forms.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "buopso_forms/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "buopso_forms/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# automatically load and sync documents of this doctype from downstream apps
# importable_doctypes = [doctype_1]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "buopso_forms.utils.jinja_methods",
# 	"filters": "buopso_forms.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "buopso_forms.install.before_install"
# after_install = "buopso_forms.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "buopso_forms.uninstall.before_uninstall"
# after_uninstall = "buopso_forms.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "buopso_forms.utils.before_app_install"
# after_app_install = "buopso_forms.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "buopso_forms.utils.before_app_uninstall"
# after_app_uninstall = "buopso_forms.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "buopso_forms.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"buopso_forms.tasks.all"
# 	],
# 	"daily": [
# 		"buopso_forms.tasks.daily"
# 	],
# 	"hourly": [
# 		"buopso_forms.tasks.hourly"
# 	],
# 	"weekly": [
# 		"buopso_forms.tasks.weekly"
# 	],
# 	"monthly": [
# 		"buopso_forms.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "buopso_forms.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "buopso_forms.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "buopso_forms.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["buopso_forms.utils.before_request"]
# after_request = ["buopso_forms.utils.after_request"]

# Job Events
# ----------
# before_job = ["buopso_forms.utils.before_job"]
# after_job = ["buopso_forms.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"buopso_forms.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }
after_migrate = "buopso_forms.utils.update_workspace"
app_name = "buopso_forms"
app_title = "Buopso Forms"
# ... (other configs)

# Add this:
doc_events = {}

override_whitelisted_methods = {
    "buopso_forms.api.msg91_webhook.delivery_report": "buopso_forms.api.msg91_webhook.delivery_report"
}
