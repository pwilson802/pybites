import requests
import json

def get_ip_country(ip_address):
    """Receives ip address string, use IPINFO_URL to get geo data,
       parse the json response returning the country code of the IP"""
    url = f'http://ipinfo.io/{str(ip_address)}/json'
    ip_data = json.loads(requests.get(url).text)
    return ip_data['country']