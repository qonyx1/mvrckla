import socket
import requests
import time
from pystyle import Colors, Colorate, Center, System, Box
from pyfiglet import Figlet
import sys

def print_centered(text):
    centered_text = Center.XCenter(text)
    print(centered_text)

texx = """
Welcome to
PapingRemake v1
"""

def print_header():
    f = Figlet(font='slant')
    header_text = f.renderText(texx)
    colored_header = Colorate.Color(Colors.red, texx, True)
    print_centered(colored_header)

def get_ip_info(ip):
    try:
        url = f"http://ipinfo.io/{ip}/json"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            ip = data.get('ip', '')
            hostname = data.get('hostname', '')
            city = data.get('city', '')
            region = data.get('region', '')
            country = data.get('country', '')
            location = data.get('loc', '')
            org = data.get('org', '')
            postal = data.get('postal', '')
            timezone = data.get('timezone', '')
            asn = data.get('asn', '')

            return ip, hostname, city, region, country, location, org, postal, timezone, asn
        else:
            return "", "", "", "", "", "", "", "", "", ""
    except Exception as e:
        return "", "", "", "", "", "", "", "", "", ""

def ping_ip(ip, port):
    try:
        socket.setdefaulttimeout(1)
        while True:
            start_time = time.time()
            socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((ip, int(port)))
            end_time = time.time()
            time_taken = (end_time - start_time) * 1000  # in milliseconds
            resulta = f"Connected to {ip}: time={time_taken:.2f}ms protocol=TCP port={port}"
            resultb = Center.XCenter(resulta)
            result = Colorate.Color(Colors.green, resultb, True)

            yield result
    except Exception as e:
        yea = "Connection timed out"
        resulta = Colorate.Color(Colors.red, yea, True)
        print_centered(resulta)
        

def main():
    if len(sys.argv) != 2:
        print("Usage: python ip_location.py <ip_address>")
        return

    input_ip = sys.argv[1]

    try:
        socket.inet_aton(input_ip)
    except socket.error:
        try:
            input_ip = socket.gethostbyname(input_ip)
        except Exception as e:
            print("Invalid input")
            return

    ip, hostname, city, region, country, location, org, postal, timezone, asn = get_ip_info(input_ip)

    if asn == "" or asn == " ":
        asn = "Not Found"

    lol = str(f"{ip} / {hostname}")
    print_centered(lol)

    tex = f"""

ISP/Organization: {org}
Country: {country}
Region: {region}
City: {city}
Location: {location}
Postal Code: {postal}
Timezone: {timezone}

"""
    
    te = Center.XCenter(tex)

    tel = Colorate.Color(Colors.light_red, te, True)
    print(tel)


    while True:
        try:
            print("\n")
            port = input(Center.XCenter("Enter port number: "))
            if not port:
                port = "443"  # default port
            int(port)  # check if valid integer
            break
        except ValueError:
            print(Center.XCenter("Invalid port number. Please enter a valid integer."))

    sys.stdout.write("\033[F")
    sys.stdout.write("\033[K")
    ping_generator = ping_ip(input_ip, port)

    try:
        while True:
            result = next(ping_generator)
            sys.stdout.write("\033[F")
            sys.stdout.write("\033[K")
            print_centered(result)
            time.sleep(1)
    except KeyboardInterrupt:
        System.Clear()
        print("\n\nProgram terminated by user.")
    except Exception as e:
        pass

if __name__ == "__main__":
    try:
        System.Clear()
        sdf = Center.Center("Analyzing Hostname")


        co = Colorate.Color(Colors.red, sdf, True)
        print(co)
        time.sleep(1)
        System.Clear()
        print_header()
        main()
    except KeyboardInterrupt:
        System.Clear()
        print("\n\nProgram terminated by user.")
    except Exception as e:
        print(f"Error: {str(e)}")
