from click.testing import CliRunner
import click
import os
import heic_to_jpg
from click.testing import CliRunner


#initialized variables
#directory that stores heic files.
srcDir = "C:\Users\jjaud\AppData\Roaming\JetBrains\PyCharmCE2021.2\scratches\HEIC2JPG Mass Converter\heic"
destDir2 = "C:\Users\jjaud\AppData\Roaming\JetBrains\PyCharmCE2021.2\scratches\HEIC2JPG Mass Converter"
#should be empty
heicFiles = []
jpgFiles = []
motto = "Thank you for using my converter:) "
complete = False

##optimize
####windows environment variable
####

#Creates command with two options. -s to specify directory in which HEIC files reside. -o to specify directory in
#which converted jpg files are to get outputted to.
@click.command()
@click.option("-s", "-source_directory", type=click.Path(exists=True), required=True)
@click.option("-o", "-output_directory", type=click.Path(exists=True))
@click.option("-f", "-file_type", type=click.Path(exists=True))
    ############################################################
def main(srcDir, outDir):





















#with open("heic") as selected_directory:
#    target_directory = selected_directory.read()
