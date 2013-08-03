# -*- coding: utf-8 -*-
"""
    flask.ext.webfonts
    ~~~~~~~~~~~~~~~~~
This extension provides a simple font gallery interface as well as a api for
using the fonts as webfonts.

    :copyright: (c) 2013 by Nithin Saji.
    :license: BSD, see LICENSE for more details.
"""

from .views import bp
from .fonts import fonts

class Webfonts(object):
    """
    This class makes flask application serve webfonts from a specified url or
    subdomain. It also comes with an optional interface for showcasing
    webfonts. It supports multiple lamguages.
    """
    def __init__(self, app=None):
        self.app = None
        if app is not None:
            self.init_app(app)

    def init_app(self, app):

        #register the api blueprint
        app.register_blueprint(bp)

    def list_fonts(*languages):
        pass
