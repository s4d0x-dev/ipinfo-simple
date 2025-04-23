import requests

def get_myip():
    raw_ip = (requests.get("http://checkip.dyndns.com/").text)
    return  raw_ip.split(": ") [-1].split("<") [0].strip()

def check_ip(ip):
    url = f"https://ipinfo.io/{ip}/json"
    resp = requests.get(url)
    data = resp.json()

    print(f"\nInfo for IP: {ip}")
    result = [data.get('region'),
              data.get('country'),
              data.get('city'),
              data.get('loc'),
              data.get('org'),
              data.get('postal'),
              data.get('timezone')]
    
    return result

def print_data(data):
    titles = ["Region",
             "Country",
             "City",
             "Geo_Location",
             "Organ",
             "Postal-Code",
             "Time-Zone"]
    for title, value in zip(titles, data):
        print(f"{title}: {value}")

if __name__ == "__main__":
    ip = input(f"Enter your Target IPv4 ({get_myip()}): ")

    if ip.strip() == "":
        print_data(check_ip(get_myip()))
    elif any(char.isalpha() for char in ip):
        print("IPv4 may not contain letters") 
    else:
        parts = ip.split(".")
        if len(parts) != 4:
            print("The IPv4 must contains 4 octets.")
        else:
            print_data(check_ip(ip))
