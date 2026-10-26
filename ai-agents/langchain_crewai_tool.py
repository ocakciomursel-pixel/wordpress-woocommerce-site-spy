"""
WordPress & WooCommerce Theme, Plugin & Agency Lead Spy — LangChain, CrewAI & OpenAI Assistants Tool
Official Apify Actor: https://apify.com/lucacelli/wordpress-woocommerce-site-spy ($0.80 / 1,000 sites)
"""
import os
import requests
from typing import Dict, Any, List

APIFY_TOKEN = os.getenv("APIFY_TOKEN", "YOUR_APIFY_TOKEN")
ENDPOINT = "https://api.apify.com/v2/acts/lucacelli~wordpress-woocommerce-site-spy/run-sync-get-dataset-items"

def run_wordpress_woocommerce_site_spy(custom_input: Dict[str, Any] = None) -> List[Dict[str, Any]]:
    """
    Executes WordPress & WooCommerce Theme, Plugin & Agency Lead Spy on Apify Cloud ($0.80/1k sites).
    Detect active WordPress themes, installed plugins, WooCommerce cart status, exposed wp-json REST API namespaces, and agency contact details across any list of domains.
    """
    default_payload = {
    "domains": [
        "techcrunch.com",
        "woocommerce.com"
    ],
    "detectPlugins": True
}
    payload = custom_input if custom_input else default_payload
    res = requests.post(f"{ENDPOINT}?token={APIFY_TOKEN}", json=payload, timeout=300)
    res.raise_for_status()
    return res.json()
