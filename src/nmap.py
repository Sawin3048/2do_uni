import nmap

scanner = nmap.PortScanner()
scanner.scan('127.0.1.1')
print(scanner.all_hosts)
