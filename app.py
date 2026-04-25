from flask import Flask, render_template, request

app = Flask(__name__)

skills_db = ["python", "java", "sql", "html", "css", "javascript", "react", "excel", "machine learning"]

@app.route('/', methods=['GET', 'POST'])
def home():
    result = ""
    score = 0

    if request.method == 'POST':
        resume = request.form['resume'].lower()

        found = []
        for skill in skills_db:
            if skill in resume:
                found.append(skill)

        score = len(found) * 10
        result = ", ".join(found)

    return render_template("index.html", result=result, score=score)

if __name__ == '__main__':
    app.run(debug=True)
