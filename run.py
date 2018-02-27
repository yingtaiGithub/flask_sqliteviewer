#! /usr/bin/env python
import os
from app import app

# db.create_all()

extra_dirs = [os.path.join(os.getcwd(),'app', 'template')]
extra_files = extra_dirs[:]
for extra_dir in extra_dirs:
    for dirname, dirs, files in os.walk(extra_dir):
        for filename in files:
            filename = os.path.join(dirname, filename)
            if os.path.isfile(filename):
                extra_files.append(filename)

app.run(debug=True,host="127.0.0.1",port=8080)