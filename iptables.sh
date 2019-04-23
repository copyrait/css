sudo apt-get install iptables

sudo iptables -A INPUT -i eth0 -j ACCEPT
sudo iptables -I INPUT -i eth0 -p icmp -j DROP
sudo iptables -I INPUT -i lo -j DROP -p tcp -s 127.0.0.1 --dport 8009
sudo iptables -I INPUT  -j DROP -p tcp -s example.com

sudo iptables -S # view list of iptable rules for your firewall you can see that above 4 rules has been added in the list.
