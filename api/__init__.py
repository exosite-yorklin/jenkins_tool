# coding: utf-8
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('/var/www/jenkins_tool/api/templates/ForInput.html')

@app.route('/ans', methods=['POST'])
def ans():
    data = str(request.form.get('All case'))
    data_list = data.split("\r\n")
    print(len(data_list))
    case = ""
    for item in data_list:
        case +='-O -t="%s" ' % item
    case = case[0:len(case)-1]
    ans = "sudo python dqa-env/exo-robot-runner run -I dqa-semi-vert %s -i api -i solution -D hamv" % (case)

    print(ans)

    return ans

if __name__ == '__main__':
    app.run()