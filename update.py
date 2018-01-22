import sys
import  os
from config_vg import *
import requests

HOST = Config_Vg().HOST
PATH = os.path.dirname(os.path.realpath(__file__))
class Update(object):

  def __init__(self):
    pass

  def wget_ips(self):
    with open('list_countries') as f:
      lines = f.read().splitlines()
    countries = list(map(lambda x: x.split('\t')[0], lines))
    urls = dict(map(lambda x: ( x , HOST + x + '-aggregated.zone'),countries))
    for key in urls.keys():
      req = requests.get(urls[key])
      file_name = PATH + '/country_blacklist_ip/'+key+'_blacklist'
      f= open(file_name, "w")
      f.write(req.content)
      f.close()

vg_update = Update()
vg_update.wget_ips()