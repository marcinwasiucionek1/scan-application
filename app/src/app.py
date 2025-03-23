from flask import Flask, request, render_template
import subprocess

app = Flask(__name__)

def run_command(cmd):
    try:
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True, encoding='utf-8')
        output = process.communicate()[0]
        return output
    except Exception as e:
        return str(e)

@app.route('/')
def home():
    return render_template('index.html', results="")

@app.route('/search', methods=['POST'])
def execute_command():
    user_cmd = request.form['city']
    cmd = f'grep {user_cmd} cities.txt'
    results = run_command(cmd)
    print("Command: " + cmd)
    return render_template('index.html', results=results)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
