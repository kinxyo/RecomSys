# make sure you've run `MLrecommendation.ipynb` OR `ml.py` first to generate the model

from app import app

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)