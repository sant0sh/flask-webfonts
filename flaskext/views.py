from flask import Blueprint, request, make_response
from flask import render_template, url_for, abort
from fonts import fonts as available_fonts

bp = Blueprint('webfonts', __name__,
               template_folder='templates',
               static_folder='fonts', static_url_path='/webfonts/')


@bp.route('/api/webfonts', methods=['GET'])
def serve():
        try:
                req_fonts = request.args.get('font').split('|')
        except AttributeError:
                abort(400)
        match_request = set(req_fonts).intersection(set(available_fonts.keys()))
        if not match_request:
                abort(400)
        else:
                fonts = [{'family': f,
                          'eot': url_for('webfonts.static', _external=True, filename=available_fonts[f]['eot']),
                          'woff': url_for('webfonts.static',  _external=True, filename=available_fonts[f]['woff']),
                          'ttf': url_for('webfonts.static', _external=True, filename=available_fonts[f]['ttf'])
                          } for f in match_request]
                resp = make_response(render_template('webfonts.css', fonts=fonts))
                resp.mimetype = 'text/css'
                return resp


@bp.route('/webfonts')
def gallery():
        return "Display fonts"
