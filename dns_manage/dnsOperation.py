import os
from flask import render_template,request,url_for,redirect

class dnsOperation:

    def __init__(self,account):
        self.account = account

    def _list_zone():
