import os
HOST_UPDATE ='http://www.ipdeny.com/ipblocks/data/aggregated/'
# IP_WHITELIST = ['ng', 'ne', 'gb', 'cm', 'dz', 'fr', 'cm', 'do', 'ma', 'us', 'es', 'gh' ]
# IP_BLACKLIST = ['my' , 'in', 'vi']
IP_BLACKLIST = 'config/blacklist_countries'
IP_WHITELIST = 'config/whitelist_countries'

AUTO_DETECT_IP = 1
PORT_SCAN = 443
class Config_Vg(object):
  def __init__(self):
    path = os.path.dirname(os.path.realpath(__file__))
    self.HOST =HOST_UPDATE
    self.AUTO_DETECT_IP = AUTO_DETECT_IP
    self.PORT_SCAN =PORT_SCAN
    with open(path + '/' + IP_BLACKLIST) as f:
      self.IP_BLACKLIST = [line.rstrip('\n') for line in f]
    with open(path + '/' + IP_WHITELIST) as f:
      self.IP_WHITELIST = [line.rstrip('\n') for line in f]
path = os.path.dirname(os.path.realpath(__file__))
print path