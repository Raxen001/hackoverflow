# importing needed libraries
import pyotp
from flask import *
from flask_bootstrap import Bootstrap

# configuring flask application
app = Flask(__name__)
# change this
app.config["SECRET_KEY"] = "APP_SECRET_KEY"
Bootstrap(app)


# homepage route
@app.route("/")
def index():
    return "Welcome to the reader's club"


@app.route("/profile")
def profile():
    return "this is your profile"


# 2FA page route
@app.route("/login")
def login_2fa():
    # get secret from db
    secret = "helloworld"
    return render_template("login_2fa.html", secret=secret)


# 2FA form route
@app.route("/login", methods=["POST"])
def login_2fa_form():
    secret = "helloworld"
    otp = int(request.form.get("otp"))

    # verifying submitted OTP with PyOTP
    if pyotp.TOTP(secret).verify(otp):
        # inform users if OTP is valid
        flash("The TOTP 2FA token is valid", "success")
        return redirect(url_for("profile"))
    else:
        # inform users if OTP is invalid
        flash("You have supplied an invalid 2FA token!", "danger")
        return redirect(url_for("login_2fa"))


@app.route("/signup")
def signup():
    return render_template("signup.html")


@app.route("/signup", methods=["POST"])
def signup_form():
    import mail
    import qrcode

    email = request.form.get("email")
    secret = pyotp.random_base32()
    # change hello world to db
    totp = pyotp.TOTP("helloworld")
    account_name = email
    issuer = "Reader's Club"
    provisioning_uri = totp.provisioning_uri(
        name=account_name, issuer_name=issuer)

    img = qrcode.make(provisioning_uri)
    file_name = "qrcodes/" + email + ".png"
    img.save(file_name)
    mail.gmail_send_message(email, file_name, provisioning_uri)

    return redirect(url_for('login_2fa'))


# running flask server
if __name__ == "__main__":
    app.run(debug=True)
