from flask import *

app = Flask(__name__)
# Session Key 
app.secret_key = "money"
import pymysql
from functions import *
from mpesa import *

@app.route("/")
def Homepage():
    # Connect to DB
    connection  = pymysql.connect(host="localhost",user="root",password="",database="jumia_mini")
    sql = "select* from Products where product_category = 'phones' "
    sql1 = "select* from Products where product_category = 'electronics' "
    sql2 = "select* from Products where product_category = 'beds' "
    sql3 = "select* from Products where product_category = 'beauty' "
    sql4 = "select* from Products where product_category = 'Media' "

    # You need to have a cursor 
    # cursor- is used to run/execute above SQL 
    Cursor = connection.cursor()
    Cursor1 = connection.cursor()
    Cursor2 = connection.cursor()
    Cursor3 = connection.cursor()
    Cursor4 = connection.cursor()

    # Execute
    Cursor.execute(sql)
    Cursor1.execute(sql1)
    Cursor2.execute(sql2)
    Cursor3.execute(sql3)
    Cursor4.execute(sql4)

    # Fetch all phone rows
    phones = Cursor.fetchall()
    electronics = Cursor1.fetchall()
    beds = Cursor2.fetchall()
    beauty = Cursor3.fetchall()
    Media = Cursor4.fetchall()
    return render_template("index.html", phones=phones, electronics=electronics, beds=beds, beauty=beauty, Media=Media)


# Route for a single item
@app.route("/single/<product_id>")
def single(product_id):

#  connect to DB 
    connection  = pymysql.connect(host="localhost",user="root",password="",database="jumia_mini")

    # Create SQL Query 
    sql = "select * from Products where product_id = %s "

    # Create a Cursor
    cursor = connection.cursor()

    # Execute
    cursor.execute(sql, product_id)

    # Get the Single product
    product  = cursor.fetchone()
    return render_template("single.html", product=product)
 

# Upload products
@app.route("/upload", methods = ['POST', 'GET'])
def upload():
    if request.method == 'POST':
        # user can add the products
        product_name = request.form['product_name']
        product_desc = request.form['product_desc']
        product_cost = request.form['product_cost']
        product_category = request.form['product_category']
        product_image_name = request.files['product_image_name']
        product_image_name.save('static/images/' + product_image_name.filename)

        # Connect to DB
        connection  = pymysql.connect(host="localhost",user="root",password="",database="jumia_mini")
        

        # Create a cursor
        Cursor = connection.cursor()
        sql = "insert into Products (product_name, product_desc, product_cost, product_category, product_image_name) value (%s, %s, %s, %s, %s)"

        data = (product_name, product_desc, product_cost, product_category, product_image_name.filename)



        Cursor.execute(sql, data)

        # Save changes
        connection.commit()


        return render_template("upload.html", message = "Product Added Successfully")
    else:
     return render_template("upload.html", error = "Please add a product")
    
# FAshion Route
    # Helps you to see all the fashions
@app.route("/fashion")
def Fashion():
     # Connect to DB
    connection  = pymysql.connect(host="localhost",user="root",password="",database="jumia_mini")
    sql = "select* from Products where product_category = 'dresses' "
    sql1 = "select* from Products where product_category = 'handbags' "
    sql2 = "select* from Products where product_category = 'caps' "
    sql3 = "select* from Products where product_category = 'socks' "
    sql4 = "select* from Products where product_category = 'belt' "

    # You need to have a cursor 
    # cursor- is used to run/execute above SQL 
    Cursor = connection.cursor()
    Cursor1 = connection.cursor()
    Cursor2 = connection.cursor()
    Cursor3 = connection.cursor()
    Cursor4 = connection.cursor()

    # Execute
    Cursor.execute(sql)
    Cursor1.execute(sql1)
    Cursor2.execute(sql2)
    Cursor3.execute(sql3)
    Cursor4.execute(sql4)

    # Fetch all phone rows
    dresses = Cursor.fetchall()
    handbags = Cursor1.fetchall()
    caps = Cursor2.fetchall()
    socks = Cursor3.fetchall()
    belt = Cursor4.fetchall()
    return render_template ("fashion.html", dresses= dresses, handbags= handbags, caps=caps, socks=socks, belt=belt )

# A route to upload Fashion
@app.route("/uploadfashion", methods = ['POST', 'GET'])
def uploadfashion():
    if request.method == 'POST':
        # user can add the products
        product_name = request.form['product_name']
        product_desc = request.form['product_desc']
        product_cost = request.form['product_cost']
        product_category = request.form['product_category']
        product_image_name = request.files['product_image_name']
        product_image_name.save('static/images/' + product_image_name.filename)

        # Connect to DB
        connection  = pymysql.connect(host="localhost",user="root",password="",database="jumia_mini")
        

        # Create a cursor
        Cursor = connection.cursor()
        sql = "insert into Products (product_name, product_desc, product_cost, product_category, product_image_name) value (%s, %s, %s, %s, %s)"

        data = (product_name, product_desc, product_cost, product_category, product_image_name.filename)



        Cursor.execute(sql, data)

        # Save changes
        connection.commit()


        return render_template("uploadfashion.html", message = "Fashion Added Successfully")
    else:
     return render_template("uploadfashion.html", error = "Please add a fashion")
    

@app.route("/about")
def About():
    return "This is about page"

# User Registration
@app.route("/register",methods = ['POST', 'GET'])
def Register():
    if request.method == 'POST':
        # user can add the details
        username = request.form['username']
        email = request.form['email']
        gender = request.form['gender']
        phone = request.form['phone']
        password = request.form['password']

        # session['username'] = username

        # # Validate User password
        # response = Verifypassword(password)
        # if response == True:
        #     # password met the required conditions
        # else:
        #     # password did not meet all the conditions
        #     return render_template ("register.html", message = "Registration successfull")


        # Connect to DB
        connection  = pymysql.connect(host="localhost",user="root",password="",database="jumia_mini")
        

        # Create a cursor
        Cursor = connection.cursor()
        sql = "insert into users (username, email, gender, phone, password) value (%s, %s, %s, %s, %s)"

        data = (username,  email, gender, phone, password)



        Cursor.execute(sql, data)

        # Save changes
        connection.commit()
        return render_template ("register.html", message = "Registration successfull")
    else:
        return render_template("register.html", error = "Please register")
# Password  

@app.route("/login", methods = ['POST', 'GET'])
def Login():
    if request.method ==  'POST':
        # user can add the details
        email = request.form['email']
        password = request.form['password']
        connection  = pymysql.connect(host="localhost",user="root",password="",database="jumia_mini")
        Cursor = connection.cursor()

        # check if user email exist
        sql = "select * from users where email= %s and password = %s"
        data = ( email, password)
        Cursor.execute(sql, data)
        # check if any result found
        if Cursor.rowcount == 0:
            # It means the username and password not found
            return render_template("login.html", error = "Invalid Login Credentials")
        else:
            session['key'] = email
            return redirect("/")
    return render_template('login.html')


    # Mpesa
    # implement STK PUSH 
@app.route("/mpesa", methods = ['POST'])
def mpesa():
    phone = request.form["phone"]
    amount = request.form["amount"]

    # Use Mpesa_payment function mpesa.py
    # It accepts the phone and amount as arguments
    #  mpesa_payment("1", phone) - Payment to be deducted from mpesa
    mpesa_payment("amount", phone)
    return '<h1> Please complete payment in your phone</h1>' \
    '<a href="/" class="btn btn-dark btn-sm"> Go Back to Products </a> '


@app.route("/logout")
def Logout():
    session.clear()
    return redirect("/login")

if __name__ == "__main__":
    app.run(debug=True, port=4000)