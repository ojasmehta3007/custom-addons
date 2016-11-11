import base64
import csv
import functools
import glob
import imghdr
import itertools
import jinja2
import logging
import operator
import datetime
import hashlib
import os
import re
import json
import sys
import time
import zlib
from xml.etree import ElementTree
from cStringIO import StringIO

import babel.messages.pofile
import werkzeug.utils
import werkzeug.wrappers
from openerp.api import Environment

import openerp
import openerp.modules.registry
from openerp.addons.base.ir.ir_qweb import AssetsBundle, QWebTemplateNotFound
from openerp.modules import get_resource_path
from openerp.tools import topological_sort
from openerp.tools.translate import _
from openerp.tools import ustr
from openerp.tools.misc import str2bool
from openerp import http
from openerp.http import request, serialize_exception as _serialize_exception
from openerp.exceptions import AccessError


class Home(http.Controller):

    @http.route('/', type='http', auth="none")
    def index(self, s_action=None, db=None, **kw):
        return http.local_redirect('/web', query=request.params, keep_hash=True)

