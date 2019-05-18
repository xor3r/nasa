from flask import Flask, render_template, request, redirect, url_for
from modules.images import search_images
import modules.make_map


app = Flask(__name__, template_folder="../templates", static_folder='../static')


@app.route("/", methods=['GET', 'POST'])
def index():
    """
    Main page indexing.

    :return: rendered index.html page
    """
    return render_template('index.html')


@app.route("/map", methods=['GET', 'POST'])
def map():
    """
    Map page indexing.

    :return: rendered error.html or mars.html page
    """
    if request.method == 'POST':
        if request.form.get('submit_button'):
            #make_map.main()
            return render_template('mars.html')
        else:
            pass
    elif request.method == 'GET':
        return render_template('error.html')


@app.route('/photos', methods=['GET', 'POST'])
def photos():
    """
    Gallery page indexing.

    :return: rendered search.html page
    """
    if request.method == 'POST':
        if request.form.get('submit_button2'):
            return render_template('search.html')


@app.route("/app", methods=['GET', 'POST'])
def application():
    """
    Download page indexing.

    :return: redirect to downloadable file
    """
    if request.method == 'POST':
        if request.form.get('submit_button3'):
            return redirect('https://docs.google.com/uc?export=download&id=14zD9ysWs7XuAw2GdFGbg_HJJwT5J2NDU')


@app.route("/search", methods=["POST"])
def search():
    """
    Searching page indexing.

    :return: rendered gallery.html or no_match.html page
    """
    date = request.form.get("date")
    camera = request.form.get("camera")
    if not date:
        return render_template('no_match.html')
    else:
        images = search_images(date, camera)
        if images:
            return render_template('gallery.html', image_names=images)
        return render_template('no_match.html')


if __name__ == '__main__':
    app.run(debug=False)
