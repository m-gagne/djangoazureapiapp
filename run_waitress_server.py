import os, sys
from waitress import serve

from app.wsgi import application

if __name__ == '__main__':
    serve(application, host="0.0.0.0", port=os.getenv("PORT", 8000))