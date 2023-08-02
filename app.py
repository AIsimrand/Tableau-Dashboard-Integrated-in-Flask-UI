from flask import Flask, render_template

app = Flask(__name__)

@app.route('/tableau_custom_viz')
def tableau_custom_viz():
    return render_template('tableau_custom_viz.html')

if __name__ == "__main__":
    app.run()
