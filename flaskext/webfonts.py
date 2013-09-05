# -*- coding: utf-8 -*-
"""
    flask.ext.webfonts
    ~~~~~~~~~~~~~~~~~
This extension provides a simple font gallery interface as well as a api for
using the fonts as webfonts.

    :copyright: (c) 2013 by Nithin Saji.
    :license: BSD, see LICENSE for more details.
"""

from .views import (WebfontsApiView, WebfontsListView,
                    WebfontsPreviewTextView, WebfontsGalleryView)
from flask import Blueprint
from text import text
import os.path
import yaml
import sys


class Webfonts(object):
    """
    This class makes flask application serve webfonts from a specified url or
    subdomain. It also comes with an optional interface for showcasing
    webfonts. It supports multiple lamguages.
    """
    def __init__(
            self,
            app=None,
            font_folder='fonts',
            api_url_prefix="/webfonts",
            subdomain=None
    ):

        self.app = app
        try:
            config_fonts = open(os.path.join(self.app.root_path, "fonts.yaml"))
        except IOError:
            print("You must provide a fonts.yaml file with \
                  font configuration. Reffer documentation.")
            sys.exit(0)
        self.fonts = yaml.load(config_fonts)
        try:
            config_text = open(os.path.join(self.app.root_path, "text.yaml"))
        except IOError:
            pass
        else:
            user_text = yaml.load(config_text)
            self.text = dict(text.items() + user_text.items())

        self.url_prefix = api_url_prefix
        self.subdomain = subdomain
        self.font_folder = os.path.join(self.app.root_path, font_folder)
        self.blueprint = Blueprint('bp_api_webfonts', __name__,
                                   static_folder=self.font_folder,
                                   template_folder="templates")
        self.blueprint.add_url_rule('/',
                                    view_func=WebfontsApiView.as_view(
                                        'webfonts_api', self.fonts))
        self.blueprint.add_url_rule('/list',
                                    view_func=WebfontsListView.as_view(
                                        'webfonts_list', self.fonts))
        self.blueprint.add_url_rule('/text',
                                    view_func=WebfontsPreviewTextView.as_view(
                                        'webfonts_text', self.text))
        if app is not None:
            self.init_app(app)
        self.add_gallery()

    def init_app(self, app):

        #register the api blueprint
        app.register_blueprint(self.blueprint,
                               static_folder=self.font_folder,
                               template_folder='templates',
                               url_prefix=self.url_prefix,
                               subdomain=self.subdomain)

    def add_gallery(self):
        self.gallery_bp = Blueprint('bp_webfonts_gallery', __name__,
                                    static_folder="static",
                                    template_folder='templates')
        self.gallery_bp.add_url_rule('/gallery',
                                     view_func=WebfontsGalleryView.as_view(
                                        'webfonts_gallery'))
        self.app.register_blueprint(self.gallery_bp,
                                    url_prefix=self.url_prefix)

    def list_fonts(self, *languages):
        font_list = []
        for i in self.fonts:
            if self.fonts[i]["Language"] in languages:
                font_list.append({i: self.fonts[i]})
        return font_list
