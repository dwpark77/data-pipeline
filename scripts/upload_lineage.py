#!/usr/bin/env python3
"""CLI to upload Pentaho lineage to Open Metadata."""

import argparse
import json
import os
import requests

from pentaho_parser import parse_pentaho_xml


def send_lineage(lineage, api_base, token=None):
    """Send lineage information to Open Metadata."""
    headers = {"Content-Type": "application/json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"

    url = f"{api_base.rstrip('/')}/lineage"
    response = requests.post(url, headers=headers, data=json.dumps({"lineage": lineage}))
    response.raise_for_status()
    return response.json()


def main():
    parser = argparse.ArgumentParser(description="Upload Pentaho lineage to Open Metadata")
    parser.add_argument("xml_path", help="Path to Pentaho transformation XML")
    parser.add_argument("--api", required=True, help="Open Metadata API base URL")
    parser.add_argument("--token", help="Authentication token (or set OM_TOKEN env var)")
    args = parser.parse_args()

    token = args.token or os.getenv("OM_TOKEN")
    lineage = parse_pentaho_xml(args.xml_path)
    resp = send_lineage(lineage, args.api, token)
    print("Lineage upload successful:")
    print(json.dumps(resp, indent=2))


if __name__ == "__main__":
    main()
