# Vulnerable XSS Application
> In this application contains 3 types XSS vulnerabilities examples

* DOM Based XSS
* Stored XSS
* Reflected XSS

## Installation

```commandline
docker run -d -p 5060:5060 we45/vulnerable_xss:latest
```

Or 

```commandline
git clone https://github.com/we45/vulnerable_xss.git
```

* Create and activate Virtualenv

```commandline
virtualenv -p python3 venv
```

```commandline
source venv/bin/activate
```

* cd into the `vulnerable_xss/app` directory

```commandline
cd vulnerable_xss/app
```

* Install python requirements

```commandline
pip install -r requirements.txt
```

* Now run the application

```commandline
python3 app.py
```

* Open Browser and run `http://127.0.0.1:5060`, The Vulnerable XSS application ready now


### Follow the documentation to exploit the XSS vulnerabilities

[DOM Based XSS](DOMBASEDXSS.md)
[Stored XSS](STOREDXSS.md)
[Reflected XSS](REFLECTEDXSS.md)

