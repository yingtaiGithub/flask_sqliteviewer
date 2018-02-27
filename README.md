## Prepearing
There are 4 tables, Threshold, Offset, Cache and Final. You can put the data into front 3 tables. 


## Instructions
As always ensure you create a virtual environment for this application and install
the necessary libraries from the `requirements.txt` file.

```
$ virtualenv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

Then make a scheduling job to run get_finaltable.py periodically. This will update final table  by combining 3 tables you provide periodically. 


Then start the development server

```
$ python run.py
```

Browse to http://0.0.0.0:8080
