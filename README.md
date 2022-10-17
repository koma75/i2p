img2pdf
========================================================================

Convert set of images to PDF.

ADD MY CLI DETAIL DESCRIPTION HERE

Installation
------------------------------------------------------------------------

~~~shell
> pip install img2pdf
~~~

Usage
------------------------------------------------------------------------


### Subcmd 1

Subcmd description

~~~shell
> i2p subcmd1 --option1 --argopt1 arg -v
~~~

* -o, --option1
    * description
* -a, --argopt1 ARG
    * description
* -c, --config CFG
    * CFG: Path to Configuration File (default: img2pdf.yml)
* -v, --verbose
    * verbosity

### Configuration file

YAML based configuration file (default file name: img2pdf.yaml)
is used to store default settings for the tool.
The command line options will take precedence over the configuration parameters.

following shows the default settings of the configuration

~~~yaml
option1: option1param
option2: option2param
optionArray:
  - item1
  - item2
optionDict:
  key1: item1
  key2: item2
  key3: item3
~~~

Known Issues
------------------------------------------------------------------------

Need to be implemented.

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
