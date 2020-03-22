from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

# initialization
app = Flask(__name__)

# MySQL connection details
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flaskcrud'
mysql = MySQL(app)

# settings
app.secret_key = "mysecretkey"


@app.route("/")
def Index():
    return render_template('index.html')


@app.route("/user/add_user")
def add_user():
    if request.method == 'POST':
        user_name = request.form['user_name']
        password = request.form['password']
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        phone_number = request.form['phone_number']
        billing_address_line_1 = request.form['billing_address_line_1']
        billing_address_line_2 = request.form['billing_address_line_2']
        billing_city = request.form['billing_city']
        billing_state = request.form['billing_state']
        billing_zip_code = request.form['billing_zip_code']
        shipping_address_line_1 = request.form['shipping_address_line_1']
        shipping_address_line_2 = request.form['shipping_address_line_2']
        shipping_city = request.form['shipping_city']
        shipping_state = request.form['shipping_state']
        shipping_zip_code = request.form['shipping_zip_code']

        cursor = mysql.connection.cursor()
        cursor.execute(
            "INSERT INTO user (user_name, password, first_name, last_name, email, phone_number, billing_address_line_1, billing_address_line_2"
            ", billing_city, billing_state, billing_zip_code, shipping_address_line_1, shipping_address_line_2, shipping_city, shipping_state, shipping_zip_code)"
            " VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
            (user_name, password, first_name, last_name, email, phone_number, billing_address_line_1,
             billing_address_line_2, billing_city, billing_state, billing_zip_code, shipping_address_line_1,
             shipping_address_line_2, shipping_city, shipping_state, shipping_zip_code))

        mysql.connection.commit()
        flash('Contact Added successfully')
    # return redirect(url_for('Index'))


@app.route("/customer/add_customer")
def add_customer():
    if request.method == 'POST':
        first_name = request.form['user_name']
        last_name = request.form['last_name']
        email = request.form['email']
        phone_number = request.form['phone_number']
        billing_address_line_1 = request.form['billing_address_line_1']
        billing_address_line_2 = request.form['billing_address_line_2']
        billing_city = request.form['billing_city']
        billing_state = request.form['billing_state']
        billing_zip_code = request.form['billing_zip_code']
        shipping_address_line_1 = request.form['shipping_address_line_1']
        shipping_address_line_2 = request.form['shipping_address_line_2']
        shipping_city = request.form['shipping_city']
        shipping_state = request.form['shipping_state']
        shipping_zip_code = request.form['shipping_zip_code']

        cursor = mysql.connection.cursor()
        cursor.execute(
            "INSERT INTO user (first_name, last_name, email, phone_number, billing_address_line_1, billing_address_line_2, billing_city, billing_state, "
            "billing_zip_code, shipping_address_line_1, shipping_address_line_2, shipping_city, shipping_state, shipping_zip_code)"
            " VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
            (first_name, last_name, email, phone_number, billing_address_line_1, billing_address_line_2, billing_city, billing_state, billing_zip_code, 
             shipping_address_line_1, shipping_address_line_2, shipping_city, shipping_state, shipping_zip_code))

        mysql.connection.commit()
        flash('Contact Added successfully')
        # return redirect(url_for('Index'))


@app.route("/product/add_product")
def add_product():
    if request.method == 'POST':
        description = request.form['description']
        price = request.form['price']
        image_url = request.form['image_url']

        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO product (description, price, image_url) VALUES(%s,%s,%s)", (description, price, image_url))

        mysql.connection.commit()
        flash('Product Added successfully')
        # return redirect(url_for('Index'))

