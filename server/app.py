
from functools import wraps
import pyotp
from flask import *
from flask_bootstrap import Bootstrap
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager
from flask_jwt_extended import verify_jwt_in_request
from flask_jwt_extended import get_jwt

# configuring flask application
app = Flask(__name__)
# change this
app.config["SECRET_KEY"] = "APP_SECRET_KEY"
# Change this to a random, secure secret key
app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'
jwt = JWTManager(app)
Bootstrap(app)

# Custom decorator for user authentication


def admin_required():
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            verify_jwt_in_request()
            claims = get_jwt()
            if claims["is_administrator"]:
                return fn(*args, **kwargs)
            else:
                return jsonify(msg="Admins only!"), 403

        return decorator

    return wrapper


def user_required():
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            verify_jwt_in_request()
            claims = get_jwt()
            if claims["is_user"]:
                return fn(*args, **kwargs)
            else:
                return jsonify(msg="LOGIN ! to access this"), 403

        return decorator

    return wrapper


@app.route("/")
def index():
    return "Welcome to the reader's club"


@app.route("/profile")
@user_required()
def profile():
    return "this is your profile"


@app.route("/admin-profile")
@admin_required()
def admin_profile():
    return "Admin pannel"


# 2FA page route
@app.route("/login")
def login_2fa():
    return render_template("login_2fa.html")


# 2FA form route
@app.route("/login", methods=["POST"])
def login_2fa_form():
    import db

    email = request.form.get("username")
    otp = int(request.form.get("otp"))

    secret = db.get_user_secret(email)

    print(otp)
    print("Secret is: ", secret)

    # verifying submitted OTP with PyOTP
    if pyotp.TOTP(secret).verify(otp):
        # inform users if OTP is valid
        flash("The TOTP 2FA token is valid", "success")
        role = db.get_role(email)
        print("role", role)

        access_token = create_access_token(
            identity=email, additional_claims={"is_user": True})

        if role == "admin":
            access_token = create_access_token(
                identity=email, additional_claims={"is_administrator": True}
            )
        return jsonify(access_token=access_token, role=role), 200
        # return redirect(url_for("profile"))
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
    import db

    email = request.form.get("email")
    if db.check_user_exists(email):
        flash("User already exists, redirecting to login page")
        return redirect(url_for('login_2fa'))

    secret = pyotp.random_base32()

    # change hello world to db
    totp = pyotp.TOTP(secret)

    account_name = email
    issuer = "Reader's Club"
    provisioning_uri = totp.provisioning_uri(
        name=account_name, issuer_name=issuer)

    db.add_user(email, secret)

    img = qrcode.make(provisioning_uri)
    file_name = "qrcodes/" + email + ".png"
    img.save(file_name)
    mail.gmail_send_message(email, file_name, provisioning_uri)

    return redirect(url_for('login_2fa'))


# running flask server
if __name__ == "__main__":
    app.run(debug=True)
