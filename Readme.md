# Python test framework

## Objective:

The objective is to provide a set of modules and libraries to structure and make easy the development of integration tests.

The idea is to use a high level scripting language to describe the test scenarios. And to provide or gather the library that we need to interface the components under test. 

## Requirements:


    * The framework must provides services to write automated tests of individual Unix processes or set of Unix processes. It is a set of interface libraries and ways to organize tests and tests suites. It is a set of libraries written in a high level scripting language that will be the glue between the components
    * Tests must be documented or self-described. At the minimal every test should contain a comment with
    * 
        * Scenario ID
        * Given preconditions
        * When actions
        * Then results

    * Tests must be runnable individually or inside test suites
    * Test must be assertion based and use one unit test library of the host scripting language (to provide assertion check routines, jenkins interface, test suite management, etc).
    * The host scripting language is python


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

