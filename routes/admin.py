from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    session,
    flash
)

from config import Config

admin = Blueprint(
    "admin",
    __name__,
    url_prefix="/admin"
)


@admin.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")

        if (
            username == Config.ADMIN_USERNAME
            and
            password == Config.ADMIN_PASSWORD
        ):

            session["admin"] = True

            return redirect("/admin/dashboard")

        flash("اسم المستخدم أو كلمة المرور غير صحيحة.")

    return render_template("admin_login.html")


@admin.route("/dashboard")
def dashboard():

    if not session.get("admin"):

        return redirect("/admin/login")

    return "Admin Dashboard"