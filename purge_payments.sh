#!/bin/bash

# Set your Frappe project root
ROOT="$HOME/frappeApp/test_frappe"
APPS="$ROOT/apps"
SITES="$ROOT/sites"

echo "🔍 Scanning for ghost references to 'payments'..."

# 1. Remove 'payments' from apps.txt
sed -i '/^payments$/d' "$SITES/apps.txt"

# 2. Remove from common_site_config.json
sed -i '/payments/d' "$SITES/common_site_config.json"

# 3. Remove from all site_config.json files
find "$SITES" -name site_config.json -exec sed -i '/payments/d' {} \;

# 4. Delete Python bytecode
find "$APPS" -name "*.pyc" -delete

# 5. Scan for internal code references
echo "📁 Searching app code for 'payments' imports..."
grep -Ri "payments" "$APPS" | grep -E 'import|from|payments' > /tmp/payments_refs.txt

if [[ -s /tmp/payments_refs.txt ]]; then
    echo "⚠️ Found internal references to 'payments':"
    cat /tmp/payments_refs.txt
    echo "🛠️ Please manually remove or comment out these lines."
else
    echo "✅ No internal references found."
fi

# 6. Rebuild bench metadata
echo "🔄 Running bench cleanup..."
cd "$ROOT"
bench setup requirements
bench clear-cache
bench build
bench restart

echo "🎉 Cleanup complete. If errors persist, check /tmp/payments_refs.txt for unresolved imports."
