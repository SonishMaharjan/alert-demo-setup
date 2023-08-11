pip3 install pipenv

// Go to project folder and run
pip3 install django (this also creates virtual env)

//Start virtual env
pipenv shell

// start django project
django-admin startproject alert // Create alert project and app

// django-admin startproject hospital_management . // this will not create another alert folder inside.

python manage.py runserver

##// Set python interpreter to interpreter in side vnev to VS Code
pipenv --venv # show the directory of interpreter > /home/sonish/.local/share/virtualenvs/alert_app-0uABaTjG
##// the  search 'Select python interpreter'(CTRL + Shift + P) in VS code and, paste the path ( NOTE: append '/bin/python' at end )


// now add '.vscode/settings.json' in root project folder
and in settings.json
{
    "python.pythonPath": "/home/sonish/.local/share/virtualenvs/alert_app-0uABaTjG/bin/python"
}

// When you open terminal in VS code, it automatically start the venv.


// Now start a new app
python manage.py startapp alert


// Setting up debug configuation
Go to view.py/ .py file, then click on Run & debug, icon -> Create new lauch.json -> search for Django Run Debug. and use it.