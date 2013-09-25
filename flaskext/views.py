from flask import request, make_response
from flask import render_template, url_for, abort, jsonify
from flask.views import View


class WebfontsApiView(View):
        def __init__(self, fonts):
                self.fonts = fonts

        def dispatch_request(self):
                try:
                        req_fonts = request.args.getlist('font')
                except AttributeError:
                        abort(400)
                match_request = set(req_fonts).intersection(set(self.fonts.keys()))
                if not match_request:
                        abort(400)
                else:
                        fonts = [{'family': f, 'eot':
                                  url_for('bp_api_webfonts.static',
                                  _external=True,
                                  filename=self.fonts[f]['eot']),
                                  'woff':
                                  url_for('bp_api_webfonts.static',
                                  _external=True,
                                  filename=self.fonts[f]['woff']),
                                  'ttf':
                                  url_for('bp_api_webfonts.static',
                                  _external=True,
                                  filename=self.fonts[f]['ttf'])}
                                 for f in match_request]
                        resp = make_response(render_template('flask_webfonts/webfonts.css', fonts=fonts))
                        resp.mimetype = 'text/css'
                        return resp


class WebfontsListView(View):
        def __init__(self, fonts):
                self.fonts = fonts

        def dispatch_request(self):
                req_lang = request.args.getlist('language')
                if req_lang:
                        print(req_lang)
                        resp = {i: self.fonts[i] for i in self.fonts
                                if self.fonts[i]['Language'] in req_lang}
                        print(resp)
                        return jsonify(result=resp)
                else:
                        resp = {i: self.fonts[i] for i in self.fonts}
                        return jsonify(result=resp)


class WebfontsPreviewTextView(View):
        def __init__(self, text):
                self.text = text

        def dispatch_request(self):
                if request.args.has_key('language'):
                        try:
                                languages = request.args.getlist('language')
                                resp = {}
                                for i in languages:
                                        resp[i] = self.text[i]
                                        return jsonify(result=resp)
                        except ValueError:
                                abort(400)
                else:
                        return jsonify(result=self.text)


class WebfontsGalleryView(View):
        def __init__(self, template=None):
                if template is None:
                        self.template = "flask_webfonts/webfontsgallery.html"
                else:
                        self.template = template

        def dispatch_request(self):
                return render_template(self.template)

#def init_blueprint(fonts):
#        bp = Blueprint('webfonts',__name__, template_folder='templates')
#        return  bp
