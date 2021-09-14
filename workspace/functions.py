###Functions used for HEIC converter tool####
from click.testing import CliRunner
from heic_to_jpg import cli
import click
import os
import heic_to_jpg

runner = CliRunner()

#Function to cycle through given directory and begin converting files to given filetype[jpg]. Did this for future functionality.
#Starts python script

def commandLineEcho(textToEcho):
    #echos to command line

    zzechoed = runner.invoke(textToEcho)
    assert echoed.exit_code == 0
    assert echoed.output == (textToEcho)

def heic2jpgAutoFunc(dir, format, status=0):
    #return true if successfully completed
    for item in dir:
        try:
            commandLineEcho("Converting {file} to {file}...".format(file = (str(item) - str("." + format))))
            main.jpgFiles += item
        except Exception:
            status = 1
            errorFunc()
    return (status==0)

def errorFunc():
    commandLineEcho("Uh oh, an error must have occurred. Please resort to the log file for more information. :)")



#UNUSED/WIP
"""

def checkForFileFunc(file, output as ""):
    if file in


"""