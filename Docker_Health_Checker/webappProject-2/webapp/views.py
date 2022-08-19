from django.shortcuts import render
from django.http import HttpResponse
import logging
import os

log = logging.getLogger('log')


def index(request):
    log.warning("Message for warning")
    log.error("Message for error")
    log.critical("Message for critical error")
    log.info("Message for information")
    log.debug("Message for debug")
    return HttpResponse("<h1>This web application generates log files into log/debug.log</h1>")
