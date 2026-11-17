from flask import Flask, request, render_template
import joblib

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/main", methods=["POST"])
def main():
    # q 对应 HTML 中的 name="q"
    name = request.form.get("q", "").strip() or "访客"
    return render_template("index.html", name=name)


if __name__ == "__main__":
    app.run()
