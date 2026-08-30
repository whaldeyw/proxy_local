#!/usr/bin/env python3
import os
import urllib.request
import json
import sys
import subprocess

def get_external_ip():
    services = [
        'https://api.ipify.org?format=json',
        'https://ifconfig.me/json',
        'https://icanhazip.com'
    ]
    
    for service in services:
        try:
            with urllib.request.urlopen(service, timeout=5) as response:
                data = response.read().decode()
                if 'ipify' in service or 'ifconfig' in service:
                    ip = json.loads(data).get('ip')
                else:
                    ip = data.strip()
                if ip:
                    return ip
        except:
            continue
    
    return None

def main():
    port = os.environ.get('PORT', '8444')
    secret = os.environ.get('SECRET')
    external_ip = os.environ.get('EXTERNAL_IP')
    local_mode = os.environ.get('LOCAL_MODE', 'false').lower() == 'true'
    
    # Определяем внешний IP
    if external_ip:
        print(f"📌 Using EXTERNAL_IP from .env: {external_ip}")
    elif local_mode:
        external_ip = '127.0.0.1'
        print("🔹 Local mode (LOCAL_MODE=true): using 127.0.0.1")
    else:
        external_ip = get_external_ip()
        if not external_ip:
            external_ip = '127.0.0.1'
            print("⚠️ Could not detect external IP, using 127.0.0.1")
        else:
            print(f"🌐 Server mode: external IP is {external_ip}")
    
    print("========================================")
    print("  Telegram MTProto WS Bridge Proxy")
    print("========================================")
    print(f"  PORT: {port}")
    print(f"  SECRET: {secret}")
    print(f"  EXTERNAL_IP: {external_ip}")
    print(f"  LOCAL_MODE: {local_mode}")
    print("========================================")
    print("")
    print("🔗 Connect:")
    print(f"  tg://proxy?server={external_ip}&port={port}&secret=dd{secret}")
    print("")
    print("========================================")
    print("📡 Proxy running...")
    print("")
    
    os.chdir('/app/proxy')
    cmd = [
        'python3', 'tg_ws_proxy.py',
        '--host', '0.0.0.0',
        '--port', port,
        '--secret', secret
    ]
    
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    
    for line in process.stdout:
        if '172.19.0.2' in line or 'tg://proxy?server=172' in line:
            continue
        print(line, end='')

if __name__ == '__main__':
    main()
