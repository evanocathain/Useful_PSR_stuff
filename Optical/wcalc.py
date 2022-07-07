#!/opt/homebrew/opt/python@3.10/bin/python3.10

from pprint import pprint
import requests
import os
import sys
import urllib.parse

appid = os.getenv('WA_APPID','...')

# Read in command line arguments
freq_Hz = sys.argv[1]  
mag     = sys.argv[2]
dist_pc  = sys.argv[3]

equation = f"(((boltzmann constant)/(planck constant*{freq_Hz} Hz))*ln(1+ ((34.657*({freq_Hz} Hz/(10^(12) Hz))^3*pi*(30km/{dist_pc} pc)^2*(60*60*(180/pi))^2)/(10^(-6)*10^((23.9-{mag})/2.5)))))^(-1) in K"

query = urllib.parse.quote_plus(f"solve {equation}")
query_url = f"http://api.wolframalpha.com/v2/query?" \
            f"appid={appid}" \
            f"&input={query}" \
            f"&includepodid=Result" \
            f"&output=json"

r = requests.get(query_url).json()

data = r["queryresult"]["pods"][0]["subpods"][0]
plaintext = data["plaintext"]

#print(f"Result of {equation} is '{plaintext}'.")
print(f"Result = '{plaintext}'.")
