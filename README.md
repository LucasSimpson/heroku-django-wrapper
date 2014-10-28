#Heroku-Django Wrapper
###Lucas Simpson

Simple command line interface that greatly eases setting up a Django project on Heroku. Commands are:
    hwd create [project name]
        -Starts a new project. Creates the virtual env, sets up the
	directories, and sets up the home view.

    hwd delete [project name]
        -Completely deletes project. Deletes local files and heroku app.

    hwd newapp [app name]
        -Creates a new app. Sets up files, adds app to settings, and
        initializes the default view for that app.

    hwd --help
        -Shows the help file.
