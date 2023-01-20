# Welcome to throwing away the JVM and still using the code

In this repository, their is code transpiled from java code. I've found a way to remove the jvm altogether and keep it mostly functioning.

The end result will be not needing the jvm, as all the code will already adhere to the equivalent functionality.

# What is the purpose of this repository?

To put the java app inside of python & c/c++. Brython is good enough to run python3 like code with no problem of later intermixing it with javascript defined libraries

The reason to do this is so that it just runs in the web. No real need for too much configuration to get it working. Just put the libraries under the Lib/site-packages subdirectory, then import inside of the browser using brython.

# Is their a way to optimize my code?

Yes, their is. I'd use the https://brython.info editor and copy the javascript it emits from your code into a ".js" file. 
