from flask import Flask, render_template
import pandas as pd
import random

app = Flask(__name__)

def generate_data(n=100):
    return pd.DataFrame({
        'ID': range(1, n+1),
        'Value': [random.randint(10, 100) for _ in range(n)],
        'Category': [random.choice(['A', 'B', 'C']) for _ in range(n)]
    })

df = generate_data(100)

@app.route("/")
def dashboard():
    stats = {
        "total_rows": len(df),
        "avg_value": round(df["Value"].mean(), 2),
        "cat_a": int((df["Category"] == "A").sum()),
        "cat_b": int((df["Category"] == "B").sum()),
    }
    return render_template(
        "dashboard.html",
        stats=stats,
        ids=df["ID"].tolist(),
        values=df["Value"].tolist(),
        table=df.to_dict(orient="records")
    )

if __name__ == "__main__":
    app.run(debug=True)
