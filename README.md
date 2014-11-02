#Heroku-Django Wrapper
###Lucas Simpson

Heroku-Django-Wrapper is a collection of scripts that makes creating a django project hosted on Heroku a whole bunch easier.
A list of commands can be found lower under 'Help File'.

There are a few key differences between a regular Django projec and a Heroku-Django-Wrapper project. First and foremost is the directory structure. 
The directory structure is as follows:
    [projectname]
        venv
        [projectname]
            static
            _static
            templates
            _templates
                includes
            media
            [projectname]
            auxilary
            manage.py
            Procfile
            .git
            .gitignore
            .hdw_init
            requirements.txt

What they all are:
    venv
        This is the directory of the virtualenv used for this project.

    static
        Working static folder. Site will fetch css/js files from here.

    _static
        Folder for base css/cscc/js files. cscc will be built from here, 
        and copied to static along with any other css and js files.

    templates
        Working templates folder. Site will fetch html files from here. 

    _templates
        This is where all base html files are found. Includes will be built 
        from here, and copied with any other html files.

    includes
        This is where any blocks of html can be found. In any html file 
        in _templates, you can use the tag {% include [filename] %}, and 
        when the site is built the contents of [filename] will be copied
        into the html file, replaces the {% include %} tag.

    media
        Working directory for media files. This includes all pictures/videos/music.

    PROJECTNAME
        Regular django folder. Where settings.py and base urls.py can be found.

    auxilary
        This folder contains the auxilary app, which serves the home page.

    manage.py
        Django manage.py file.

    Procfile
        Procfile for heroku.

    .git
        git repository.

    .gitignore
        gitignore file for git repository.

    .hdw_init
        Contains data about the Heroku-Django-Wrapper project. Do not touch.

    requirements.txt
        Result of a pip freeze, for heroku.

* * *

###Things to note/TL;DR
_static and _templates folder are where you should put all static/html files. When hdw build is called, all contents will be copied over into the working directories, _static and _templates. This is to keep the includes and lass files in seperate directories while still keeping things simple.

Any file in templates may include a {% include [filename] %} tag. When hdw build is called, all html files will be scanned for a tag like this. Whenever a tag is found, [filename] is searched for inside the includes directory. if [filename] is found, the include tag is deleted and replaced with the contents of [filename]

Note that html inside the includes directory may NOT use this tag.

* * *

###Help File
This is the official help file for Heroku-Django-Wrapper.
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
     specifically ..../[projectname]/[projectname]

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

