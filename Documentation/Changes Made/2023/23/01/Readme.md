# Updates made:

* New files added ("__init__.py") so the directory for the package could be viewed by python & brython for importing
   at runtime.
* More directories for "sun." subpackage modules
* Updated test replit.co container files to further test functionality
* Corrected for unneeded 500 gateway error caused by splitting a hair.....
* All missing files that initially triggered a 500 and 404 server signal all return 302 200 requests teling brython that the file was not found.

# Notes

* The developer of brython may have used some signal handling for imitating some of linux in the web. 
* Continues to run until it fails or the tab is suddenly closed, or it ran correctly and did what it was told, as it should have.
* When it can't find the class at one URL handle, it then tries to find the the directory and find the __init__.py file of that directory. It then searches where it
   thinks the libraries should be. 
* "brython/3.11.0/Lib/site-packages/" and its current layout should be the area where modules you want to run in the web go. Even translated java code should go in
    this directory. Once it loads, runs, and executes, you can see what files import what or at least where it thinks the files should be imported from. It is a great
     way to do dependency checking. If you're missing a module, installation is as simple as cloning a repo and pointing to it with git_importer.py module.
* The more code that is transpiled/translated from java to c/c++ & python code, the more one can test the code by just reloading the webpage. I tested my theories on
   whether or not it would work. Thus far, the __init__.py are their to make the directories and other modules with those directories visible to brython & the web. It
    imitates how jvm has to look at java packages. The only difference is the syntax used. Once you know the 
