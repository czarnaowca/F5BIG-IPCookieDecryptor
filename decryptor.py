import sys
import re


def decrypt(big_ip_cookie):
    """
    Decrypting BIG-IP cookie to XXX.XXX.XXX.XXX:XX format
    :param big_ip_cookie: big-ip cookie to decrypt
    :return:
    """
    print(f"[+] Decrypting cookie: {big_ip_cookie}")

    if "=" in big_ip_cookie:
        cookie = big_ip_cookie.split("=")[1].strip()
    else:
        cookie = big_ip_cookie.strip()

    encoded_ip = cookie.split(".")[0]
    encoded_port = cookie.split(".")[1]

    ip_as_hex = hex(int(encoded_ip))
    port_as_hex = hex(int(encoded_port))

    ip_as_hex = re.findall("..", ip_as_hex[2:])[::-1]
    port_as_hex = re.findall("..", port_as_hex[2:])[::-1]

    ip = ""
    for octet in ip_as_hex:
        ip += str(int(octet, 16))
        ip += "."
    ip = ip[:-1]

    port = ""
    for val in port_as_hex:
        if val.startswith("00"):
            continue
        port += str(int(val, 16))

    print(f"[*] Decoded cookie: {ip}:{port}")


if __name__ in "__main__":
    print("Author: Czarna Owca")
    print("Source: https://github.com/czarnaowca/F5BIG-IPCookieDecryptor")
    print("Contact: czarna.owca.mail@gmail.com\n")

    if len(sys.argv) != 2:
        print("\nCookie content is missing!")
        exit(0)

    decrypt(sys.argv[1])
