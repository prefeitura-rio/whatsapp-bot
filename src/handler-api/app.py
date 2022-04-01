"""
Main script for running the flask application
"""

from handler_api.api import app

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)