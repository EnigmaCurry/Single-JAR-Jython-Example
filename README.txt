################################################################################
## A self contained, executable, Jython Excel dohicky.
## 
## By Ryan McGuire
## www.EnigmaCurry.com
################################################################################

The only thing that this application does is spit out a silly Excel
file using the Apache POI java library. It's means to be an example of
how to package your own Jython application in a manner that requires
no external dependancies other than a JVM on the host computer.

To base your own project off this example you should understand how
this package is organized:

 * /src 
    Put all of your Jython source code here

 * /lib
    Put any .jar dependancies in this directory. Any .jar in this
    directory will automatically be loaded when the application starts
    so there is no need to mess with a CLASSPATH.

    This sample project has two dependancies:

      * Jython itself (jython-full.jar)
      * Apache POI for the excel capabilities (poi-3.5-beta5-20090219.jar). 
        Obviously if your project doesn't work with excel files, 
	you'd delete this file from your project.
    
    Since this is a Jython project, the jython jar is required in this
    directory. For most applications, you will want a "full" or self
    contained Jython .jar which contains the entire Jython /Lib
    directory inside. This jar should be called jython-full.jar to
    differentiate it from the one that the regular Jython installer builds.

    See the Jython build instructions below for more details.

 * /java-src
    This is meant to be a Python project, but since this is Jython,
    there's no reason you can't include some Java code as well, so put
    that in this directory.

    One thing that is required in this directory is some sort of
    bootstrap mechanism to start your Jython code. You can do that
    however you want, but a sample Main.java is included. If you call
    yours something different, you need to update the Manifest.MF
    option One-Jar-Main-Class.

 * /onejar-src
    Part of the technology which powers this application is the OneJar
    platform (http://one-jar.sourceforge.net/). This takes care of
    loading "jars within jars" which is a problem for the regular Java 
    classloader. You shouldn't need to touch this code unless
    you want to upgrade to a later version for some reason.

    OneJar is accompanied by it's own free license called
    one-jar-license.txt. In order to comply with this license, the
    license is automatically built into any .jar that this package builds.

