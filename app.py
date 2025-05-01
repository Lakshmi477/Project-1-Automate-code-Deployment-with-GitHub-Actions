from flask import Flask
app= Flask(__name__)
@app.route("/")
def home():
  return "Automate-code-Deployment-with-GitHub-Actions"
if __name__ == "__main__":
  app.run()
