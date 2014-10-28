print ("""Welcome to the Heroku-Django help file!
The following commands are available:

	create [name of project]
		-  Starts a new project in directory [name of project]. 
		 Sets up virutal env, heroku, database; the basics.

	delete [name of project]
		- deletes project from heroku and deletes directory. 
		  NOTE [name of project] is directory name, not heroku
		  app name.


Project specific commands:
	*These commands must be used inside project directory,
	 specifically ../[projec name]/[projectname]

	newapp [name of app]
		- creates a new app [name of app] in directory
		  [name of app]. Updates urls.py and settings.py 
		  accordingly.

""")
