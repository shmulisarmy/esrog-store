from flask import Flask, render_template, request, redirect
from esrogimDb import EsrogimDB

app = Flask(__name__)



db = EsrogimDB(f"esrogim.db")
db.create_table()


def log(message):
    with open("log.txt", "a") as f:
        f.write(f"{message}\n")

@app.route("/")
def root():
    return render_template("index.html", request=request, esrogim=db.get_all_available_esrogim())

@app.route("/initiate-reservation/<int:esrog_id>", methods=["GET"])
def initiate_reservation(esrog_id: int):
    result: tuple[str] = db.check_reserved(esrog_id)
    is_reserved = result[0]
    if is_reserved != '__not_reserved__':
        return {"message": "already reserved"}
    
    return {"message": "this esrog is not reserved yet please enter your name to reserve it"}

@app.route("/reserve/<int:esrog_id>/<username>", methods=["PUT"])
def reserve(esrog_id: int, username: str):
    if db.reserve_esrog(esrog_id, username):
        return {"message": "This esrog is now reserved for you until the end of the day. Please come by the store to pick it up."}
    
    return {"message": "Reservation failed"}


@app.route("/upload", methods=["POST", "GET"])
def upload():
    if request.method == "GET":
        return render_template("upload.html", request=request)
    if request.method == "POST":
        esrog_id = request.form["esrog-id"]
        size = request.form["size"]
        clenleaness = request.form["clenleaness"]
        chabad = request.form["chabad"]
        print(f"{esrog_id = }, {size = }, {clenleaness = }, {chabad = }")
        return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
