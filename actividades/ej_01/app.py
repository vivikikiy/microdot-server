from microdot import Microdot, Response, send_file

app = Microdot()

@app.route('/')
def index(request):
    try:
        return send_file('index.html', content_type='text/html')
    except Exception as e:
        print(f"Error al cargar index.html: {e}")
        return "Error al cargar la página", 500

@app.route('/base.css')
def css(request):
    try:
        return send_file('base.css', content_type='text/css')
    except Exception as e:
        print(f"Error al cargar base.css: {e}")
        return "Error al cargar el CSS", 500
    
@app.route('/actividad01.js')
def css(request):
    try:
        return send_file('actividad01.js', content_type='text/css')
    except Exception as e:
        print(f"Error al cargar el scripts: {e}")
        return "Error al cargar el scripts", 500


print("Iniciando servidor en 0.0.0.0:5000...")
app.run(debug=True)
