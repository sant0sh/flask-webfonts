#Flask-Webfonts

##Usage

the extension currently registers the following paths on the app
you can select the font_folder by passing fontfolder keyword argument
you can also pass in api_url_prefix argument as a url prefix, defaults to /webfonts


###Url Rules
```text
<Rule '/webfonts/list?language=Malayalam&language=Tamil' (HEAD, OPTIONS, GET) -> bp_api_webfonts.webfonts_list>


 <Rule '/webfonts/text?language=Malayalam' (HEAD, OPTIONS, GET) -> bp_api_webfonts.webfonts_text>,


 <Rule '/webfonts?font=Meera' (HEAD, OPTIONS, GET) -> bp_api_webfonts.webfonts_api>,
serves the css files from here

 <Rule '/webfonts/fonts/<filename>' (HEAD, OPTIONS, GET) -> bp_api_webfonts.static>,
 serves the font files from this location


 <Rule '/static/webfonts.html' (HEAD, OPTIONS, GET) -> static>
A temporary interface decoupled from the extension
```
