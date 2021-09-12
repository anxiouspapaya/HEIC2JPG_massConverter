import click
import os

#initialized variables
#directory that stores heic files.
srcDir = "C:\Users\jjaud\AppData\Roaming\JetBrains\PyCharmCE2021.2\scratches\heic"
#should be empty
newFiles = []

##optimize
####windows environment variable
####

#Creates command with two options. -s to specify directory in which HEIC files reside. -o to specify directory in
#which converted jpg files are to get outputted to.
@click.command()
@click.option("-s", "-source_directory", type=click.Path(exists=True), required=True)
@click.option("-o", "-output_directory", type=click.Path(exists=True))
def main(directory):

    #Functions
    def singleConvert(filename):

    #Converter

        try:
            for file in os.listdir(srcDir):
                if(os.name(file).endswith(".heic")):
                    newFiles.insert(file.)

















#with open("heic") as selected_directory:
#    target_directory = selected_directory.read()
