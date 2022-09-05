# AirBnB Clone
This repository contains resources that culminate into a full web application: the AirBnB clone.
Listed below are some important building blocks of this project:

* Command line Interpreter for backend object management
* Data serialization/deserialization (Instance <-> Dictionary <-> JSON string <-> file)
* Abstracted data storage engine
* Unittests for class and storage engine validation

## Language: Python

## Project Description

To create a sandboxed command line interface through which we can create, modify and delete objects in our file storage. This project currently only implements the back-end console. It is a complete web application, integrates database storage and front-end interfacing in a clone of AirBnB.

## Classes 

AirBnB utilizes the following classes:

* BaseModel
* FileStorage
* User 
* State
* City
* Amenity
* Place
* Review

## Storage 

The above classes and object data are handled by the abstracted storage engine defined in the [FileStorage] (./models/engine/file_storage.py) class.

Every time the backend is initialized, AirBnB creates an instance of the `FileStorage` class called `Storage`. The `Storage` object is loaded/re-loaded from any class instances stored in the JSON file `airbnb_file.json`. As class instances are created, updated, or deleted, the `storage` object is used to register corresponding chnages in the `airbnb_file.json` file.

## Console

The console is a command line interpreter that facilitates the backend management 
of the AirBnB clone web app. It can be used to handle all classes utilized by 
the application.

```
$ echo "help" | ./console.py
(hbnb) 
Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

(hbnb) 
$
```

Alternatively, to use the AirBnB console in interactive mode, run the 
file `console.py` by itself:

```
$ ./console.py
```

While running in interactive mode, the console displays a prompt for input:

```
$ ./console.py
(hbnb) 
```

To quit the console, input the command `quit`, or input an EOF signal 
(`ctrl-D`).

```
$ ./console.py
(hbnb) quit
$
```

```
$ ./console.py
(hbnb) EOF
$
```

### Console Commands

The AirBnB console supports the following commands:

* **create**
  * Usage: `create <class>`

Creates a new instance of a given class. The class' ID is printed and timestamped. Then 
the created instance is saved to the file `file.json`.


## Testing 

Unittests for the AirBnB project are defined in the [tests](./tests) 
directory. To run the complete test suite in an instant, execute the following command:

```
$ python3 unittest -m discover tests
```

Alternatively, you can specify a single test file to run at a time:

```
$ python3 unittest -m tests/test_console.py
```

## Author
* **Trust Eniola**  => [EnnyTee2](https://github.com/EnnyTee2)
