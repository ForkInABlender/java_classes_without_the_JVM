# Welcome to throwing away the JVM and still using the code

In this repository, their is code transpiled from java code. I've found a way to remove the jvm altogether and keep it mostly functioning.

The end result will be not needing the jvm, as all the code will already adhere to the equivalent functionality.

# What is the purpose of this repository?

To put the java app inside of python & c/c++. Brython is good enough to run python3 like code with no problem of later intermixing it with javascript defined libraries

The reason to do this is so that it just runs in the web. No real need for too much configuration to get it working. Just put the libraries under the Lib/site-packages subdirectory, then import inside of the browser using brython.

# Is their a way to optimize my code?

Yes, their is. I'd use the https://brython.info editor and copy the javascript it emits from your code into a ".js" file. If you want it really optimized, hand tuning is gonna be your best bet before compiling & using web assembly blobs.

# Do ajax and other javascript libraries work?

From what I could tell, yes. It seemed to work well and little to no issue using it in python. The only difference is the syntatic reference replacement for "$" in javascript. You don't have to change anything within the ajax libraries.

# Can this be used with nodejs?

Yes but why would you waste your time with nodejs for something that javascript and a python interface can do?

And the CPython implementation of the ctypes module for loading c/c++ binaries will need to be translated to python to be used with brython.

# Does the translated java & c/c++ code only run inside of flask & brython?

Currently it runs everywhere including the web except for what hasn't been translated of the ctypes module for cpython3. When that is done it will likely be able to load and run compiled linux libraries. This will also mean reverse engineering the linux interpreter and binary loader/parser. 

"And the simplest way to win is to simply not play. Hello, Phelix, would you like to play a game?" -- war games
