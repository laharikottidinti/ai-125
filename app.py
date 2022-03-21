from flask import Flask

app=Flask(__name__)

@app.route('/')

def homePage():
    return('hoi')
if (__name__=="__main__"):
    app.run()