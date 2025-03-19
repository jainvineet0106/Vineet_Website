from flask import Flask,render_template,request

app = Flask(__name__)

class Contacts:
    def __init__(self,name,phone,address,country,message):
        self.name = name
        self.phone = phone
        self.address = address
        self.country = country
        self.message = message
class Accounts:
    def __init__(self,name,phone,email,password):
        self.name = name
        self.phone = phone
        self.email = email
        self.password = password
class LogIn:
    def __init__(self,email,password):
        self.email = email
        self.password = password
class Forget:
    def __init__(self,phone,password):
        self.phone = phone
        self.password = password

@app.route("/")
@app.route("/front_page")
def front_page():
    return render_template("front page.html")
@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/reffrence")
def reffrence():
    return render_template("reffrence.html")

@app.route("/contact",methods = ["GET","POST"])
def contact():
    if (request.method == "POST"):
        Name = request.form.get("name")
        Phone = request.form.get("phone")
        Address = request.form.get("address")
        Country = request.form.get("country")
        Message = request.form.get("message")
        entry = Contacts(Name,Phone,Address,Country,Message)
        detail = [f"{entry.name},",f"{entry.phone},",f"{entry.address},",f"{entry.country},",f"{entry.message}","\n"]
        with open("contact.txt", "a") as Contact:
            for i in detail:
                if i != ",":
                    Contact.write(i)
                else:
                    Contact.write("none,")

        return "Submit Successfully...<br>" \
               f"Name : {entry.name}<br>" \
               f"Phone: {entry.phone}<br>" \
               f"E-mail: {entry.address}<br>" \
               f"Country: {entry.country}<br>" \
               f"Message: {entry.message}<br>"

    return render_template("contact.html")

@app.route("/create",methods = ["GET","POST"])
def create():
    if (request.method == "POST"):
        Name = request.form.get("name")
        Phone = request.form.get("phone")
        E_mail = request.form.get("email")
        Password = request.form.get("password")
        Accounts_details = Accounts(Name,Phone,E_mail,Password)
        Accounts_detail = [f"{Accounts_details.name},",f"{Accounts_details.phone},",f"{Accounts_details.email},",f"{Accounts_details.password},","0","\n"]
        with open("account.txt", "r") as Login:
            act = Login.readlines()
        act = [line.strip() for line in act[1:]]
        act = [line.split(",") for line in act]
        for i in act:
            if i[2] == Accounts_details.email and i[3] == Accounts_details.password:
                return "<div style = 'font-size:40px; text-align:center;'>Account Already Exists<br><a href = 'front_page'>Go to home in page...</a></div>"
            else:
                with open("account.txt", "a") as Account:
                    for i in Accounts_detail:
                        if i != ",":
                            Account.write(i)
                        else:
                            return "<script>alert('All Nessary');</script>"
                with open("account.txt", "r") as Login:
                    act = Login.readlines()
                act = [line.strip() for line in act[1:]]
                act = [line.split(",") for line in act]
                for i in act:
                    if i[2] == Accounts_details.email and i[3] == Accounts_details.password:
                        name = i[0].title()
                        score = i[4]
                        return render_template("home.html", Name=name, Score=score)

    return render_template("account.html")

@app.route("/login",methods = ["GET","POST"])
def login():
    if (request.method == "POST"):
        E_mail = request.form.get("email")
        Password = request.form.get("password")
        Login_details = LogIn(E_mail,Password)
        with open("account.txt", "r") as Login:
            act = Login.readlines()
        act = [line.strip() for line in act[1:]]
        act = [line.split(",") for line in act]
        for i in act:
            if i[2] == Login_details.email and i[3] == Login_details.password:
                name = i[0].title()
                score = i[4]
                return render_template("home.html",Name = name,Score =score)
        return "<div style = 'font-size:40px; text-align:center;'>try again...<br><a href = 'front_page'>Go to home in page...</a></div>"

    return render_template("login.html")

# @app.route("/forget",methods = ["GET","POST"])
# def forget():
#     if (request.method == "POST"):
#         Phone = request.form.get("phone")
#         Password = request.form.get("password")
#         forget_details = Forget(Phone,Password)
#         with open("account.txt", "r") as forget:
#             act = forget.readlines()
#         act = [line.strip() for line in act[1:]]
#         act = [line.split(",") for line in act]
#         for i in act:
#             if i[1] == forget_details.phone:
#                 send(forget_details.phone)
#                 return front_page()
#         return "<div style = 'font-size:40px; text-align:center;'>try again...<br><a href = 'front_page'>Go to home in page...</a></div>"
#
#     return render_template("forget.html")


if __name__=='__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
