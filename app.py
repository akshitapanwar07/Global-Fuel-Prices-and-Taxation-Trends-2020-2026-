from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    """Render the Global Fuel Analytics website."""
    return render_template("index.html")


if __name__ == "__main__":
    # Debug is convenient for local development. Do not use Flask's
    # development server as the production server when deploying publicly.
    app.run(debug=True)
