# vgdefense
1. Protect layer 7 DDos for small server.
- Allow access by whitelist country
- Block access by blacklist IP country.

2. Install CSF

  cd config;
  
  yum -y install wget perl unzip net-tools perl-libwww-perl perl-LWP-Protocol-https perl-GDGraph perl-libwww-perl.noarch perl-Time-HiRes bind-utils  -y
  
  gzip -d csf.tgz
  
  tar -xvzf csf.tar;
  
  cd csf;
  
  sh install.sh


3. Syn flood

  echo 1 > /proc/sys/net/ipv4/tcp_syncookies;
  
  echo 2048 > /proc/sys/net/ipv4/tcp_max_syn_backlog;
  
  echo 3 > /proc/sys/net/ipv4/tcp_synack_retries

  vi /etc/sysctl.conf

net.ipv4.tcp_syncookies = 1

net.ipv4.tcp_max_syn_backlog = 2048

net.ipv4.tcp_synack_retries = 3

4. Check connection

  netstat -nat | grep ESTABLISHED
  
  netstat -nat | grep ESTABLISHED | awk '{print $5}' | cut -d: -f1 |sort | uniq -d | sort -n |tee ips_connection.log

5. Iptables

  iptables-save>/etc/iptables_origin_save
  
  iptables -I INPUT -p tcp --dport 443 -s $line -j DROP
  
  iptables-restore</etc/iptables_origin_save

