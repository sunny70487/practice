from flask import Flask,url_for,redirect,request,render_template
app = Flask(__name__)
books = [
    {"id":1,"context":"西遊記"},
    {"id":2,"context":"三國演義"},
    {"id":3,"context":"水滸傳"},
    {"id":4,"context":"紅樓夢"},
    ]
@app.route("/Flask")
def flask():
    print("a")
    return "Hello Flask!"
@app.route('/<int:book_id>',methods = ['POST','GET'])
def test2(book_id):
    for book in books:4
        if book_id == book["id"]:
            return f"您的id為：{book}"
        else:
            return f'查無資料'
@app.route('/')
def index():
    return render_template('test.html')
@app.route('/login/',methods = ['GET',"POST"])
def login():
    return 'login page'
@app.route('/profile/',methods = ['GET','POST'])
def profile():
    name = request.args.get('name') #?name=名稱
    if not name:
        return redirect(url_for('login'))
    else:
        return name


