# pop-fundamentals:

a collection of implementation of data structures, algorithms and problems for general applications

## setup:
in order to use this project create a directory named ".devlinks" in root dir of the repository along with similar such symlinks.

```
python -> /Library/Frameworks/Python.framework/Versions/3.10/bin/python3.10
java_home -> /Users/6harat/installations/jdk-17.jdk/Contents/Home
```

change the "/path/to/repo/" path in the following line in gradle.properties.
```
org.gradle.java.home=/path/to/repo/.devlinks/java_home
```

and then execute
```
./gradlew
```
