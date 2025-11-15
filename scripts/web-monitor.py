#!/usr/bin/env python3
import requests
import os
import sys

# Configuration
URL = "http://localhost/index.php"

try:
    # Check server status
    response = requests.get(URL, timeout=5)
    response.raise_for_status() # Raise exception for bad status codes (4xx or 5xx)

    # Check if deployment message is present (application-level check)
    if "LAMP Stack Deployment Successful!" not in response.text:
        raise Exception("Application status check failed: Deployment message not found.")

    print(f"[{os.path.basename(sys.argv[0])}] SUCCESS: Web application is running and responsive.")

except requests.exceptions.RequestException as e:
    # Handle network or HTTP errors
    MESSAGE = f"CRITICAL ALERT! Web service {URL} FAILED. Error: {e.__class__.__name__}"
    print(f"[{os.path.basename(sys.argv[0])}] {MESSAGE}")
    os.system(f'notify-send "CRITICAL ALERT: LAMP WEB FAILED" "{MESSAGE}"')

except Exception as e:
    # Handle application logic errors
    MESSAGE = f"CRITICAL ALERT! Application logic failed. Error: {e}"
    print(f"[{os.path.basename(sys.argv[0])}] {MESSAGE}")
    os.system(f'notify-send "CRITICAL ALERT: LAMP APP FAILED" "{MESSAGE}"')

except Exception as e:
    # Catch any other unexpected errors
    MESSAGE = f"UNEXPECTED ERROR: {e}"
    print(f"[{os.path.basename(sys.argv[0])}] {MESSAGE}")

