#!/bin/bash

SITE="sangeet_site"

echo "🔍 Checking DocTypes against database for site: $SITE"

while read -r doctype; do
  # Remove trailing quote if present
  clean_doctype=$(echo "$doctype" | sed 's/"$//')
  
  # Run SQL query and check result
  result=$(echo "SELECT name FROM tabDocType WHERE name = '$clean_doctype';" | bench --site $SITE mariadb | grep "$clean_doctype")
  
  if [ -z "$result" ]; then
    echo "❌ Missing: $clean_doctype"
  else
    echo "✅ Found: $clean_doctype"
  fi
done < referenced_doctypes.txt
