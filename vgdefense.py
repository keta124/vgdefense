import sys
import  os
from config_vg import *
import time
import maxminddb


IP_BLACKLIST = Config_Vg().IP_BLACKLIST
IP_WHITELIST = Config_Vg().IP_WHITELIST
AUTO_DETECT_IP = Config_Vg().AUTO_DETECT_IP
PORT_SCAN = Config_Vg().PORT_SCAN
PATH = os.path.dirname(os.path.realpath(__file__))

class Vg_Defense(object):

  def __init__(self):
    pass

  def geo_country(self, ip):
    reader = maxminddb.open_database(PATH+'/config/geo_country.mmdb')
    geo_ip = reader.get(ip)
    if geo_ip:
      if unicode('country') in geo_ip :
        if unicode('iso_code') in geo_ip['country']:
          return geo_ip['country']['iso_code']

  def blacklist_country(self):
    output= str(os.popen("netstat -nat | grep ESTABLISHED | awk '{print $5}' | cut -d: -f1 |sort | uniq|sort").read())
    # with open('config/list_ip_test') as f:
    #   ips_connect = [line.rstrip('\n') for line in f]
    ips_connect = output[:-1].split('\n')
    result = {}
    for ip in ips_connect:
      geo = self.geo_country(ip)
      if geo:
        if geo in result:
          result[str(geo)] += 1
        else :
          result[str(geo)] = 1
    # print result
    result_filter =  dict(filter(lambda x:x[1]>30, result.items()))
    countries = list(IP_BLACKLIST)
    for key in result_filter.keys():
      key_ = key.lower()
      if key_ not in countries:
        countries.append(key_)

    blacklist_countries =[]
    for country in countries:
      if country not in IP_WHITELIST:
        blacklist_countries.append(country)
    file = open(PATH + "/config/blacklist_countries", "r+")
    lines = [line.rstrip('\n') for line in file]
    adds =[]
    for blc in blacklist_countries:
      if blc not in lines :
        adds.append(blc)
    file.writelines( list( "%s\n" % item for item in adds ) ) 
    file.close()
    return blacklist_countries

  def execute(self):
    ips =[]
    blacklist = self.blacklist_country()
    for country in blacklist:
      file_name = PATH + '/country_blacklist_ip/'+country+'_blacklist'
      with open(file_name) as f:
        lines = [line.rstrip('\n') for line in f]
        ips.extend(lines)
    file = open("/etc/csf/csf.deny", "r+")
    csf = [line.rstrip('\n') for line in file]
    ips_ = []
    for ip in ips_:
      if ip not in csf:
        ips_.append(ip)
    file.writelines( list( "%s\n" % item for item in ips_ ) )
    file.close()

if __name__ == '__main__':
  try:
    while True:
      vgd = Vg_Defense()
      vgd.execute()
      time.sleep(600)
    # vgd = Vg_Defense()
    # vgd.execute()
    #time.sleep(600)
  except Exception as e: 
    print(e)
