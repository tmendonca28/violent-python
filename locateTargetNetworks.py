from winreg import *
import pdb

def valueToAddress(val):
    return ':'.join('{:02X}'.format(b) for b in val)


def showPreviouslyConnectedNetworks():
    network = "SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\NetworkList\\Signatures\\Unmanaged"
    key = OpenKey(HKEY_LOCAL_MACHINE, network)
    print("\n[*] Target joined the following networks.")
    for i in range(100):
        try:
            guid = EnumKey(key, i)
            netKey = OpenKey(key, str(guid))
            (_, addr, _) = EnumValue(netKey, 5)
            (_, name, _) = EnumValue(netKey, 4)
            macAddress = "No MAC Found"
            if addr:
                macAddress = valueToAddress(addr)
            netName = str(name)
            print(f"[+] {netName} || {macAddress}")
            CloseKey(netKey)
        except:
            break


def main():
    showPreviouslyConnectedNetworks()


if __name__ == "__main__":
    main()