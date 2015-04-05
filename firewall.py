import subprocess

#Block all inbound connections
subprocess.call('netsh advfirewall set allprofiles firewallpolicy blockinbound,allowoutbound', shell=True)
subprocess.call('netsh advfirewall firewall delete rule name=all dir=in', shell=True)

#allow connections over port 80 and 443 tcp
subprocess.call('netsh advfirewall firewall add rule name="allow port 80 tcp in" dir=in localport=80 protocol=tcp action=allow', shell=True)
subprocess.call('netsh advfirewall firewall add rule name="allow port 80 tcp out" dir=out localport=80 protocol=tcp action=allow', shell=True)
subprocess.call('netsh advfirewall firewall add rule name="allow port 443 tcp in" dir=in localport=443 protocol=tcp action=allow', shell=True)
subprocess.call('netsh advfirewall firewall add rule name="allow port 443 tcp out" dir=out localport=443 protocol=tcp action=allow', shell=True)

#allow icmt v4/v6 in/out
subprocess.call('netsh advfirewall firewall add rule name="allow icmpv4 in" dir=in protocol=icmpv4 action=allow', shell=True)
subprocess.call('netsh advfirewall firewall add rule name="allow icmpv6 in" dir=in protocol=icmpv6 action=allow', shell=True)
subprocess.call('netsh advfirewall firewall add rule name="allow icmpv4 out" dir=out protocol=icmpv4 action=allow', shell=True)
subprocess.call('netsh advfirewall firewall add rule name="allow icmpv6 out" dir=out protocol=icmpv4 action=allow', shell=True)

#allow ssh (port 20) via specific subnets
subprocess.call('netsh advfirewall firewall add rule name="allow port 20 in" dir=in localport=20 remoteip =10.0.0.0/8 protocol=tcp action=allow', shell=True)
subprocess.call('netsh advfirewall firewall add rule name="allow port 20 in" dir=in localport=20 remoteip =192.168.0.0/16 protocol=tcp action=allow', shell=True)
subprocess.call('netsh advfirewall firewall add rule name="allow port 20 in" dir=in localport=20 remoteip =172.0.0.0/8 protocol=tcp action=allow', shell=True)

subprocess.call('netsh advfirewall firewall add rule name="allow port 20 out" dir=out localport=20 remoteip =10.0.0.0/8 protocol=tcp action=allow', shell=True)
subprocess.call('netsh advfirewall firewall add rule name="allow port 20 out" dir=out localport=20 remoteip =192.168.0.0/16 protocol=tcp action=allow', shell=True)
subprocess.call('netsh advfirewall firewall add rule name="allow port 20 out" dir=out localport=20 remoteip =172.0.0.0/8 protocol=tcp action=allow', shell=True)

#allow rdp (port 3389) via specific subnets
subprocess.call('netsh advfirewall firewall add rule name="allow port 3389 in tcp" dir=in localport=3389 remoteip =10.0.0.0/8 protocol=tcp action=allow', shell=True)
subprocess.call('netsh advfirewall firewall add rule name="allow port 3389 in tcp" dir=in localport=3389 remoteip =192.168.0.0/16 protocol=tcp action=allow', shell=True)
subprocess.call('netsh advfirewall firewall add rule name="allow port 3389 in tcp" dir=in localport=3389 remoteip =172.0.0.0/8 protocol=tcp action=allow', shell=True)

subprocess.call('netsh advfirewall firewall add rule name="allow port 3389 out tcp" dir=out localport=3389 remoteip =10.0.0.0/8 protocol=tcp action=allow', shell=True)
subprocess.call('netsh advfirewall firewall add rule name="allow port 3389 out tcp" dir=out localport=3389 remoteip =192.168.0.0/16 protocol=tcp action=allow', shell=True)
subprocess.call('netsh advfirewall firewall add rule name="allow port 3389 out tcp" dir=out localport=3389 remoteip =172.0.0.0/8 protocol=tcp action=allow', shell=True)

subprocess.call('netsh advfirewall firewall add rule name="allow port 3389 in udp" dir=in localport=3389 remoteip =10.0.0.0/8 protocol=udp action=allow', shell=True)
subprocess.call('netsh advfirewall firewall add rule name="allow port 3389 in udp" dir=in localport=3389 remoteip =192.168.0.0/16 protocol=udp action=allow', shell=True)
subprocess.call('netsh advfirewall firewall add rule name="allow port 3389 in udp" dir=in localport=3389 remoteip =172.0.0.0/8 protocol=udp action=allow', shell=True)

subprocess.call('netsh advfirewall firewall add rule name="allow port 3389 out udp" dir=out localport=3389 remoteip =10.0.0.0/8 protocol=udp action=allow', shell=True)
subprocess.call('netsh advfirewall firewall add rule name="allow port 3389 out udp" dir=out localport=3389 remoteip =192.168.0.0/16 protocol=udp action=allow', shell=True)
subprocess.call('netsh advfirewall firewall add rule name="allow port 3389 out udp" dir=out localport=3389 remoteip =172.0.0.0/8 protocol=udp action=allow', shell=True)