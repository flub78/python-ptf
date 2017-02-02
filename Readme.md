# Python test framework

## Objective:

The objective is to provide a set of modules and libraries to structure and make easy the development of integration tests.

The idea is to use a high level scripting language to describe the test scenarios. And to provide or gather the library that we need to interface the components under test. 

## Requirements:


  * The framework must provides services to write automated tests of individual Unix processes or set of Unix processes. It is a set of interface libraries and ways to organize tests and tests suites. It is a set of libraries written in a high level scripting language that will be the glue between the components
  * Tests must be documented or self-described. At the minimal every test should contain a comment with
  
    * Scenario ID
    * Given preconditions
    * When actions
    * Then results

  * Tests must be runnable individually or inside test suites
  * Test must be assertion based and use one unit test library of the host scripting language (to provide assertion check routines, jenkins interface, test suite management, etc).
  * The host scripting language is python

## Dependencies:

Some of the framework libraries uses external python modules:

    Pexpect - https://sourceforge.net/projects/pexpect/files/pexpect/
              sudo apt-get install python-pexpect

## Components:

The components will be developed on demand, depending on the needs of the tested projects. 

### Initial components:

  * a CLI script template, with arguments parsing and online help
  * a test template, self documented
  * a test suite template
  * a wrapper for CLI tools


  * Module to analyze logs


### Possible components to develop later:

  * Modules to address component interfaces, SOAP, REST, DVB interfaces, 
  * Modules to modify, query, save and restore databases
  * State machines, events, timeout
  * Containers management

## Tests and tests suite.

For clarify and ease of the test suite maintainance it is recommende to:
  * Have only one test per test file
  * Every test file should only contains:
  
  1. the test description
  2. the import of libraries of the utilities required by the test
  3. The setting of the pre-conditions
  4. The trigering of the actions
  5. the check of the expected result

It is recommended to gather the actions required by the tests in libraries with very descriptive function names, so the test file by itself is just the description of a high level scenario

### Test execution

Any test can be run individualy

    python test.py
    ...
    ----------------------------------------------------------------------
    Ran 3 tests in 0.000s

    OK

Or all the tests from a directory

    python -m unittest discover
    ...setupModule, restore database into initial state
    Setup, preparing for testing
    tearDown, cleaning local mess
    .Setup, preparing for testing
    tearDown, cleaning local mess
    .Cleaning global mess

    ----------------------------------------------------------------------
    Ran 5 tests in 0.000s

    OK

To generate junit style xml results
    
### Using Jenkins

The project has been designed to map easily with a jenkins job. The tests directory is the test suite of the libraries provided inside the framework as long as some test examples.

It uses py.test to generate the results in a format recognised by jenkins. py.test is test framework

on debian based linux disttribution it can be installed with
   
    sudo apt-get install python-pytest

to run the tests and generate an XML report usable by jenkins:

    py.test --junitxml results.xml *.py
    
(note that some investigation could still be done to find the most convenient python framework, but the idea is there, having individual tests generating Junit XML files)

## Python documentation

All libraries, scripts and tests are documented using pydoc.
To browse the documentation

    pydoc -p 7777
    
The documentation can then be accessed at http://localhost:7777
