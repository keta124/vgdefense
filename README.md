# vgdefense
1. Protect layer 7 DDos for small server.
- Allow access by whitelist country
- Block access by blacklist IP country.

2. Install CSF

  cd config;
  
  yum -y install wget perl unzip net-tools perl-libwww-perl perl-LWP-Protocol-https perl-GDGraph perl-libwww-perl.noarch perl-Time-HiRes bind-utils python2-pip git
  
  gzip -d csf.tgz
  
  tar -xvzf csf.tar;
  
  cd csf;
  
  sh install.sh

3. Vgdefense as service

  pip install -r requirements.txt
  
  cp systemctl/vgdefense.service /etc/systemd/system/
  
  systemctl daemon-reload
  
  cp config/csf.conf /etc/csf/
  
  *** Edit testing => 0
  
 4. Crontab
 
  systemctl start crond; systemctl enable crond
 
  0 1 * * * > /etc/csf/csf.deny
  
  */10 * * * * /usr/sbin/csf -r
 

5. Syn flood

  echo 1 > /proc/sys/net/ipv4/tcp_syncookies;
  
  echo 2048 > /proc/sys/net/ipv4/tcp_max_syn_backlog;
  
  echo 3 > /proc/sys/net/ipv4/tcp_synack_retries

  vi /etc/sysctl.conf

net.ipv4.tcp_syncookies = 1

net.ipv4.tcp_max_syn_backlog = 2048

net.ipv4.tcp_synack_retries = 3

6. Check connection

  netstat -nat | grep ESTABLISHED
  
  netstat -nat | grep ESTABLISHED | awk '{print $5}' | cut -d: -f1 |sort | uniq -d | sort -n |tee ips_connection.log

7. Iptables

  iptables-save>/etc/iptables_origin_save
  
  iptables -I INPUT -p tcp --dport 443 -s $line -j DROP
  
  iptables-restore</etc/iptables_origin_save

