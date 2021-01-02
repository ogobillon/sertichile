from bottle import route, run, static_file, error

@route(['/','/index.html'])
def index():
    return static_file('index.html', root='./static/html')

@route('/ventas.html')
def ventas():
    return static_file('ventas.html', root='./static/html')

@route('/servicios.html')
def servicios():
    return static_file('servicios.html', root='./static/html')

@route('/img/<filepath:path>')
def imagenes(filepath):
    return static_file(filepath, root='./static/img')

@route('/css/<filepath:path>')
def estilos(filepath):
    return static_file(filepath, root='./static/css')

@error(404)
def error404(error):
    return 'Nothing here, sorry'

run(host='localhost', port=8080)