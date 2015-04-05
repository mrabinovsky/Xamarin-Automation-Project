import subprocess

#allow connections over port 80 and 443 tcp
subprocess.call('netsh advfirewall firewall delete rule name="allow port 80 tcp in"', shell=True)
subprocess.call('netsh advfirewall firewall delete rule name="allow port 80 tcp out"', shell=True)
subprocess.call('netsh advfirewall firewall delete rule name="allow port 443 tcp in"', shell=True)
subprocess.call('netsh advfirewall firewall delete rule name="allow port 443 tcp out"', shell=True)

#allow icmt v4/v6 in/out
subprocess.call('netsh advfirewall firewall delete rule name="allow icmpv4 in"', shell=True)
subprocess.call('netsh advfirewall firewall delete rule name="allow icmpv6 in""', shell=True)
subprocess.call('netsh advfirewall firewall delete rule name="allow icmpv4 out"', shell=True)
subprocess.call('netsh advfirewall firewall delete rule name="allow icmpv6 out""', shell=True)

#allow ssh (port 20) via specific subnets
subprocess.call('netsh advfirewall firewall delete rule name="allow port 20 in"', shell=True)

subprocess.call('netsh advfirewall firewall delete rule name="allow port 20 out"', shell=True)

#allow rdp (port 3389) via specific subnets
subprocess.call('netsh advfirewall firewall delete rule name="allow port 3389 in tcp"', shell=True)

subprocess.call('netsh advfirewall firewall delete rule name="allow port 3389 out tcp"', shell=True)

subprocess.call('netsh advfirewall firewall delete rule name="allow port 3389 in udp"', shell=True)

subprocess.call('netsh advfirewall firewall delete rule name="allow port 3389 out udp"', shell=True)