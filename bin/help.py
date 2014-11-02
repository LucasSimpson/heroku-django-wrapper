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

	syncdb
		- migrates all apps with using south.
		  Applies any changes that have been made to the
		  app model.

	build
		- Copies contents of _static, processes Lass files,
		  and copies it all to static. 
		- Copies contents of _templates, processes any
		  includes, and copies it all to templates
		Please note that any contents of _static and _templates
		are deleted and overwritten.

""")
