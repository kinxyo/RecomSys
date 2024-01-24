from recomsys import app

from ml_recommendation import ml_recommendation

ml_recommendation()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)