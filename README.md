# My Molecular Stuffs

This repository born when I decided fuse some of codes that helps me to work with DNA sequences during my PhD. The main idea is to develop a software which do some simple, but extremelly useful things, as: convert the main files types used in molecular analysis(.fasta, .phy, and .nexus) and concatenate sequence files (as .fasta and .phy) in a nexus file. I choose to do it in Python, because it is one of my favorite programming languages and I need to improve my abilities with it.
## Technologies
This software was written in `Python 3.10`, using only Built-in modules, except from `pytest`. The main modules used were:
- abc (Abstract Classes)
- re (Regular Expression)
- typing (to type-hints)

Abstract classes and typing were used to improve coding experience and code readbility. Regular expression were extensively used to catch elements in files when converting files to different extensions (fasta, phy, and nexus).
## How it Works?
There are two main functionalities to this software:
- Convert files
- Concatenate files

These functionalities are divided in three modules: file managers, file converter, and file concatenater.
### FileManager
FileManager is an abstract class which are inherited by **FastaFileManager**, **PhyFileManager**, and **NexusFileManager**. This three children classes are responsable to handle fasta, phyllip, and nexus files, reading and writting them.
### FileConverter
This class manage which file managers and methods will be called based on parameters passed by the user. It will convert by receiving a input path and the kind of extension to output file.
### FileConcatenater
This class are responsable to concat sequences received from a file manager and convert in a single nexus file.
## Future plans
I am planning to do a first release of this software soon. After that, I will continue to improve it based in user's experience. Additionally, some new features could be added, as example:
- A generator of block to MrBayes in nexus file
- A checker to same name taxa during concatenater
- A user CSV file to check taxa name based in GenBank and other codes

## Progress check
### Features
- [x] FileManager modules to read and write files (fasta, phy, and nexus)
- [x] FileConverter module to call necessary methods to each convertion
- [ ] FileConcatenater module to concat all sequences in a nexus file
- [ ] Main module which will receive the commands, from CLI or GUI, and will pass to other modules
- [ ] Semantic and treated exceptions

### Interfaces
Both interfaces will be implemented to this project. The idea is use CLI in the future to do a web version of this project.
- [ ] Command Line Interface (CLI)
- [ ] Graphic User Interface (GUI)
### Tests
Only some modules were tested at this moment. Before the first release, at least all the modules need to be tested.
- [ ] Select good example files to tests
- [ ] All basic modules tested (FileManagers, FileConverter, and Concatenater)
- [ ] CLI tests
- [ ] GUI tests
