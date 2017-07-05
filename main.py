from flask import Flask, request, redirect, render_template

app = Flask(__name__)

app.config['DEBUG'] = True




# meant to be added to an independant module but for now this method
# makes sure that a specific item doesnt occur twice
def isIn(val, str):
    count = 0
    for i in str:
        if val == i:
            count += 1
    if count >= 2:
        return True
    else:
        return False


@app.route('/', methods=['POST', 'GET'])
def add_user():



    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        verify = request.form['password_repeat']
        email = request.form['email']

        invalid_user = ""
        invalid_password = ""
        verification = ""
        email_error = ""

        usr_er = False
        pss_er = False
        verification_er = False
        empty_er = False
        email_er = False

        # usrname error
        if 4 > len(username) or len(username) > 20 or ' ' in username:
            invalid_user = "Invalid username, It has to be between 4-20 characters without spaces"
            usr_er = True

        if 4 > len(password) or len(password) > 20 or ' ' in password:
            invalid_password = "Invalid password, Must be between 4-20 characters without spaces"
            pss_er = True

        if password != verify:
            verification = "Passwords have to match"
            verification_er = True


        if email == '':
            email_error = "can only contain 1 . and 1 @ symbol and must be between 4-20 charecters without spaces"
            email_er = True

        if isIn('.', email) or isIn('@', email):
            email_error = "can only contain 1 . and 1 @ symbol and must be between 4-20 charecters without spaces"
            email_er = True

        if usr_er == False and pss_er == False and email_er == False and verification_er == False:
            return redirect('/welcome?username={0}'.format(username))

        else:

            return render_template('form.html', invalid_user = invalid_user, invalid_password = invalid_password,
            email_error = email_error, verification = verification)

    return render_template('form.html')



@app.route('/welcome')
def index():
    username = request.args.get('username')
    return render_template('welcome.html', username = username)



if __name__ == '__main__':
    app.run()
