# vgdefense
1. Protect layer 7 DDos for small server.
- Allow access by whitelist country
- Block access by blacklist IP country.
http://www.ipdeny.com/ipblocks/data/aggregated/

2. Syn flood
#echo 1 > /proc/sys/net/ipv4/tcp_syncookies
#echo 2048 > /proc/sys/net/ipv4/tcp_max_syn_backlog
#echo 3 > /proc/sys/net/ipv4/tcp_synack_retries

Edit /etc/sysctl.conf
net.ipv4.tcp_syncookies = 1
net.ipv4.tcp_max_syn_backlog = 2048
net.ipv4.tcp_synack_retries = 3

3. Check connection
#netstat -nat | grep ESTABLISHED
#netstat -nat | grep ESTABLISHED | awk '{print $5}' | cut -d: -f1 |sort | uniq -d | sort -n |tee ips_connection.log

4. Iptables
#iptables-save>/etc/iptables_origin_save
#iptables -I INPUT -p tcp --dport 443 -s $line -j DROP
#iptables-restore</etc/iptables_origin_save
