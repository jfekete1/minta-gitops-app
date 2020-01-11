from flask import Flask
app = Flask('minta-gitops')

@app.route('/')
def hello():
  return "Gitops minta!\n"

if __name__ == '__main__':
  app.run(host = '0.0.0.0', port = 8080)
