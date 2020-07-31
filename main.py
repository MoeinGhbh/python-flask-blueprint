from flask import Flask
from second import second1

app=Flask(__name__)
app.register_blueprint(second1, url_prefix='')

@app.route('/')
def main():
    return '<h3>rose raeein</h3>'

if __name__=='__main__':
    app.run(debug=True)