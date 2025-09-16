#!/bin/bash

SITE_NAME="sangeet_site"
APPS_PATH=~/frappeApp/test_frappe/apps
PAYMENTS_APP="$APPS_PATH/payments"

echo "Checking if 'payments' app exists..."

if [ ! -d "$PAYMENTS_APP" ]; then
    echo "'payments' app not found. Creating minimal placeholder app..."
    mkdir -p "$PAYMENTS_APP/payments"
    
    # Create minimal __init__.py
    echo "__version__ = '0.0.1'" > "$PAYMENTS_APP/payments/__init__.py"
    
    # Create empty hooks.py
    echo "# hooks for payments" > "$PAYMENTS_APP/payments/hooks.py"

    # Create minimal app.json
    cat <<EOL > "$PAYMENTS_APP/payments/app.json"
{
    "app_name": "payments",
    "app_title": "Payments",
    "app_publisher": "Placeholder",
    "app_description": "Minimal placeholder for payments",
    "app_icon": "octicon octicon-file-directory",
    "app_color": "#589494",
    "app_email": "placeholder@example.com",
    "app_license": "MIT"
}
EOL

    echo "Minimal 'payments' app created."
else
    echo "'payments' app already exists."
fi

# Install the app on your site
echo "Installing 'payments' app on site $SITE_NAME..."
bench --site $SITE_NAME install-app payments

# Run migrations
echo "Running migrations..."
bench --site $SITE_NAME migrate

# Clear caches
echo "Clearing caches..."
bench --site $SITE_NAME clear-cache
bench --site $SITE_NAME clear-website-cache

echo "Done. 'payments' module placeholder installed and site migrated."

