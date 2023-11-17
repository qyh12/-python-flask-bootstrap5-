#导入Flash对象
from flask import Flask,render_template,request,redirect

#使用Flask对象创建一个qpp对象
app = Flask(__name__)

students = [
    {'studentid': '2023','name':'张一','chinese':'60','math':'60','english':'60'},
    {'studentid': '2022','name':'张二','chinese':'60','math':'60','english':'60'},
    {'studentid': '2021','name':'张三','chinese':'60','math':'60','english':'60'},
    {'studentid': '2020','name':'张四','chinese':'60','math':'60','english':'60'},
]

#路由
@app.route('/') #访问的路径
def hello_world():
    return 'Hello World!'

@app.route('/login',methods=['GET','POST'])
def login():
    #全栈项目 前后端不分离
    # return '实现登录'
    #request 对象可拿到浏览器传递给服务器的所有数据
    if request.method == 'POST':
        username=request.form.get('username')
        password=request.form.get('password')
        #登录成功后，连接数据库，检验账号密码
        print('从服务器接收到的数据:',username,password)
        #登录成功，跳转到管理页面
        return redirect('/admin')
    return render_template("login.html")

@app.route('/admin')
def admin():
    return render_template('admin.html',students=students)

@app.route('/add',methods=["GET","POST"])
def add():
    if request.method == 'POST':
        studentid=request.form.get('studentid')
        name = request.form.get('name')
        chinese = request.form.get('chinese')
        math = request.form.get('math')
        english = request.form.get('english')
        print('获取的学员信息:',studentid,name,chinese,math,english)
        students.append({'studentid': studentid,'name':name,'chinese':chinese,'math':math,'english':english})
        return redirect('/admin')
    return render_template('add.html')

@app.route('/delete')
def delete():
    #后端需要拿到要删除的数据
    print(request.method)
    username=request.args.get('name')
    #找到学员删除
    for stu in students:
        if stu['name']==username:
            students.remove(stu)
    return redirect('/admin')

@app.route('/change',methods=["GET","POST"])
def change():
    #先显示学员的数据，在浏览器修改，提交到服务器保存
    username=request.args.get('name')

    if request.method == 'POST':
        studentid=request.form.get('studentid')
        username = request.form.get('name')
        chinese = request.form.get('chinese')
        math = request.form.get('math')
        english = request.form.get('english')

        for stu in students:
            if stu['name']==username:
               stu['studentid'] = studentid
               stu['chinese'] = chinese
               stu['math'] = math
               stu['english'] = english
        return redirect('/admin')

    for stu in students:
        if stu['name']==username:
            return render_template('change.html',student=stu)

if __name__ == '__main__':
    app.run()
