# Generator

Simple markdown to html generator written in Python. The goal of the project is to understand how markdown documents are converted to html documents and used in static site generators like Jekyll or Hugo. This project was inspired by a guided project on [boot.dev](https://www.boot.dev/).

A combonation of Python standard library string operations and tools like os, pathlib, http, and unittest were used to build the generator. Simple OOP classes were used to model markdown text, html parents, html children as objects. Methods and functions were used to break markdown documents into component blocks, transform to text objects, and then generate structured html using a template.

The generator is capable of recusrively converting all markdown documents in a source directory to html and then placing them in a target directory used to serve the documents with a local server. A simple shell script is provided for running the main function and initiating the http server.

The generator has a basic suite of unit tests that cover discrete function, method, and object behavior. No test coverage was written for OS related operations. A simple shell script is provided for running the test suite and cleaning up after.
