imgmerge
========================================================================

Convert set of images to PDF.

This tool is intended to merge multiple scanned images into one PDF file.
The tool will take multiple images in order, a directory of images or 
both and merge them into a PDF file in the order it is given.
Images in the directory will be searched by specified extensions and
sorted by name.

Installation
------------------------------------------------------------------------

~~~shell
> pip install imgmerge
~~~

Usage
------------------------------------------------------------------------


### join

Join multiple images into one PDF file.

~~~shell
Usage: i2p join [OPTIONS] [[IMG] IMG...]

  join images into one PDF file

Options:
  -c, --config <cfg>  Configuration File (default: i2p.yml)
  -o, --out <out>     output filename for the generated PDF
  -t, --toc <toc>     toc file to populate PDF outline
  -e, --ext <ext>     file extensions to pick up when parsing directories
  -d, --dpi <dpi>     pixel density of input image in dpi
  -v, --verbose       output in verbose mode
  -h, --help          Show this message and exit.
~~~

* -c, --config <cfg>
    * Configuration File (default: i2p.yml)
* -o, --out <out>
    * output filename for the generated PDF
* -t, --toc <toc>
    * toc file to populate PDF outline (TBD)
* -e, --ext <ext>
    * file extensions to pick up when parsing directories.
      directories will be searched for all files using this extensions.
    * can set multiple items.
* -d, --dpi <dpi>
    * pixel density of input image in dpi.  used to calculate image width and 
      height in mm.
* -v, --verbose
    * output in verbose mode
    * specify twice to get debug messages
* -h, --help
    * Show help message

### addtoc

T.B.D.
Subcommand to just add toc to already created pdf? (may need to use some other library.)

### Configuration file

YAML based configuration file (default file name: i2p.yaml)
is used to store default settings for the tool.
The command line options will take precedence over the configuration parameters.

following shows the default settings of the configuration

~~~yaml
out: output.pdf
toc: toc.yml
dpi: 96
ext:
  - jpg
  - jpeg
  - png
~~~

### TOC File

consist of dictionary with following structure, where `level` is the 
outline level (starting from 0), and `title` is the title of the 
outline and will be inserted at `pagenum`.  The keys are case 
sensitive.

~~~yaml
pagenum:
    - level: Num
      title: 'Title'
~~~

Note, each entry inside the page must be an array of dictionaries.
This is to allow multiple ToC item to be inserted in one page.

Example may be as follows:

~~~yaml
1:
    - level: 0
      title: 'Getting Started'
    - level: 1
      title: 'Installation'
3:
    - level: 1
      title: 'Hello, World'
5:
    - level: 0
      title: 'Programming a Guessing Game'
~~~

Known Issues
------------------------------------------------------------------------

* Code needs refactoring

Development
------------------------------------------------------------------------

### Building an Executable

Install pyinstaller and package the project.
May want to use venv when executing the pyinstaller.

First, enter venv and install the local package and pyinstaller

~~~shell
>. .venv/Scripts/activate
(.venv) >pip install .
Processing /path/to/proj/imgmerge
~snip~
Installing collected packages: imgmerge
    Running setup.py install for imgmerge ... done
Successfully installed imgmerge-0.1.0

(.venv) >pip install pyinstaller
~snip~
Successfully installed pyinstaller-3.6
~~~

Use pyinstaller to build the exe file.

~~~shell
(.venv) >pyinstaller imgmerge\cli.py --onefile --name imgmerge
~snip~
13691 INFO: Building EXE from EXE-00.toc completed successfully.
~~~

Executable should be ready in dist/imgmerge.exe

### Versioning

The project will follow the [semver2.0](http://semver.org/) versioning scheme.  
With initial development phase starting at 0.1.0 and increasing
minor/patch versions until we deploy the tool to production
(and reach 1.0.0).
The interface relevant to versioning is whatever defined in this
document's "Usage" section (includes all (sub)commands, their cli arguments,
and the format of the configuration file "imgmerge.yaml").

Version History
------------------------------------------------------------------------

Date        | Version   | Changes
:--         | --:       | :--
2022.10.17  | 0.1.0     | First Release
