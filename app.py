from flask import Flask, render_template, request,url_for
import joblib

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':

        # Offensive stats
        offTurnover = request.form['offTurnover']
        offRebound = request.form['offRebound']
        offFreeThrow = request.form['offFreeThrow']
        off2Point = request.form['off2Point']
        off3Point = request.form['off3Point']
        gameTempo = request.form['gameTempo']

        # Defensive stats
        defTurnover = request.form['defTurnover']
        defRebound = request.form['defRebound']
        defFreeThrow = request.form['defFreeThrow']
        def2Point = request.form['def2Point']
        def3Point = request.form['def3Point']

        model = joblib.load('trainedBasketballModel.pkl')

        Season_Path = [

        offTurnover,    # Turnover Percentage Allowed  **Offense
        defTurnover,    # Turnover Percentage Committed  **Defense
        offRebound,     # Offense Rebounds Rate  **Offense
        defRebound,     # Offense Rebounds Rate Allowed  **Defense
        offFreeThrow,   # Free Throw Rate  **Offense
        defFreeThrow,   # Free Throw Rate Allowed  **Defense
        off2Point,      # 2-Point Shooting Percentage  **Offense
        def2Point,      # 2-Point Shooting Percentage Allowed **Defense
        off3Point,      # 3-Point Shooting Percentage  **Offense
        def3Point,      # 3-Point Shooting Percentage Allowed  **Defense
        gameTempo       # Adjusted Tempo(quantity of possesions per 40 minutes)
            
        ]

        outlooks = [
            Season_Path
        ]

        predicted_season_outlook = model.predict(outlooks)

        predicted_outlook = predicted_season_outlook[0]
 
        if predicted_outlook == 1.0:
            return render_template('playoffs.html') 
        else:
            return render_template('noPlayoffs.html') 


if __name__=="__main__":
    app.debug = False
    app.run()