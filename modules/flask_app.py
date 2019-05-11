from flask import Flask, render_template, request, redirect, url_for
from images import search_images


app = Flask(__name__, template_folder="../templates", static_folder='../static')


@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route("/map", methods=['GET', 'POST'])
def map():
    if request.method == 'POST':
        if request.form.get('submit_button'):
            #make_map.main()
            return render_template('mars.html')
        else:
            pass
    elif request.method == 'GET':
        return 'bye'


@app.route('/photos', methods=['GET', 'POST'])
def photos():
    if request.method == 'POST':
        if request.form.get('submit_button2'):
            return render_template('search.html')


@app.route("/app", methods=['GET', 'POST'])
def statistics():
    if request.method == 'POST':
        if request.form.get('submit_button3'):
            return redirect('https://docs.google.com/uc?export=download&id=14zD9ysWs7XuAw2GdFGbg_HJJwT5J2NDU')


@app.route("/search", methods=["POST"])
def search():
    date = request.form.get("date")
    camera = request.form.get("camera")
    if not date:
        return 'Failed'
    else:
        images = search_images(date, camera)
        if images:
            return render_template('gallery.html', image_names=images)
        return 'No images found :('


if __name__ == '__main__':
    app.run(debug=True)
