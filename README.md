img2pdf
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
> pip install img2pdf
~~~

Usage
------------------------------------------------------------------------


### join

Join multiple images into one PDF file.

~~~shell
Usage: i2p join [OPTIONS] [[IMG] IMG...]

  join images into one PDF file

Options:
  -c, --config <cfg>  Configuration File (default: img2pdf.yml)
  -o, --out <out>     output filename for the generated PDF
  -t, --toc <toc>     toc file to populate PDF outline
  -e, --ext <ext>     file extensions to pick up when parsing directories
  -d, --dpi <dpi>     pixel density of input image in dpi
  -v, --verbose       output in verbose mode
  -h, --help          Show this message and exit.
~~~

* -c, --config <cfg>
    * Configuration File (default: img2pdf.yml)
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

Subcommand to just add toc to already created pdf.

### Configuration file

YAML based configuration file (default file name: img2pdf.yaml)
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

consist of dictionary with following structure:

~~~yaml
pagenum:
    Level: Num
    Title: Title
~~~

Known Issues
------------------------------------------------------------------------

* TODO: TOC implementation
* Refactor code

Development
------------------------------------------------------------------------

### Building an Executable

Install pyinstaller and package the project.
May want to use venv when executing the pyinstaller.

First, enter venv and install the local package and pyinstaller

~~~shell
>. .venv/Scripts/activate
(.venv) >pip install .
Processing /path/to/proj/img2pdf
~snip~
Installing collected packages: img2pdf
    Running setup.py install for img2pdf ... done
Successfully installed img2pdf-0.1.0

(.venv) >pip install pyinstaller
~snip~
Successfully installed pyinstaller-3.6
~~~

Use pyinstaller to build the exe file.

~~~shell
(.venv) >pyinstaller img2pdf\cli.py --onefile --name i2p
~snip~
13691 INFO: Building EXE from EXE-00.toc completed successfully.
~~~

Executable should be ready in dist/i2p.exe

### Versioning

The project will follow the [semver2.0](http://semver.org/) versioning scheme.  
With initial development phase starting at 0.1.0 and increasing
minor/patch versions until we deploy the tool to production
(and reach 1.0.0).
The interface relevant to versioning is whatever defined in this
document's "Usage" section (includes all (sub)commands, their cli arguments,
and the format of the configuration file "img2pdf.yaml").

Version History
------------------------------------------------------------------------

Date        | Version   | Changes
:--         | --:       | :--
2022.10.17  | 0.1.0     | First Release
