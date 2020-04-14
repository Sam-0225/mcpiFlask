from mcpi.minecraft import Minecraft
from flask import Flask, render_template, request
mc = Minecraft.create()
app = Flask(__name__)


@app.route('/')
def get_Pos():
    pos = mc.player.getTilePos()
    return render_template("index.html", posit=pos)


@app.route('/tp', methods=['GET', 'POST'])
def set_Pos():
    if request.method == "POST":
        a = request.form
        mc.player.setTilePos(int(a["x"]), int(a["y"]), int(a["z"]))
        pos = mc.player.getTilePos()
        return render_template("index.html", posit=pos)
    else:
        return render_template("tp.html")


app.run()

