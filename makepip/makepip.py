#!/usr/bin/env python

import os
from pathlib import Path
home = str(Path.home())
import datetime
now = datetime.datetime.now()

def main():
  name = input("Enter a pip name: ")
  description = input("Enter a description: ")
  author_name = input("Author name: ")
  author_website = input("Author website: ")
  author_email = input("Author email: ")
  git_repo = input("Git repository: ")
  input_script = input("Enter a python script (absolute path) to package (code should be wrapped in a `def main():` function): ")
  pypi_username = input("Your pypi username: ")
  if name=="" or name==None:
    return

  os.system(f"mkdir -p {name}/{name}")

  f = open(f"{name}/{name}/__init__.py", "w")
  f.write("")
  f.close()

  f = open(f"{name}/{name}/__main__.py", "w")
  f.write(f"from .{name} import main\n")
  f.write("main()")
  f.close()

  setup_file = f"""
import setuptools

setuptools.setup(
    name='{name}',  
    version='0.1',
    author="{author_name}",
    author_email="{author_email}",
    description="{description}",
    long_description="{description}",
    url="{git_repo}",
    packages=["{name}"],
    entry_points = {{
        "console_scripts": ['{name} = {name}.{name}:main']
    }},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
"""

  f = open(f"{name}/setup.py", "w")
  f.write(setup_file)
  f.close()


  licence_file = f"""
Copyright (c) {now.year} {author_name} {author_website}

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

  f = open(f"{name}/LICENCE", "w")
  f.write(licence_file)
  f.close()

  readme_file = f"""
#{name}

{description}
"""

  f = open(f"{name}/README.md", "w")
  f.write(readme_file)
  f.close()

  pypirc_file = f"""
[distutils] 
index-servers=pypi

[pypi] 
repository = https://upload.pypi.org/legacy/ 
username = {pypi_username}
"""

  f = open(f"{home}/.pypirc", "w")
  f.write(pypirc_file)
  f.close()


  f = open(input_script, "r")
  script = f.read()
  f.close()

  if not script:
    return None

  f = open(f"{name}/{name}/{name}.py", "w")
  f.write(script)
  f.close()
  
  os.chdir(name)
  os.system("python -m pip install --upgrade pip setuptools wheel")
  os.system("python -m pip install tqdm")
  os.system("python -m pip install twine")
  os.system("python setup.py bdist_wheel")
  os.system("python -m twine upload dist/*")

  if git_repo:
    os.system("git init")
    os.system(f"git add LICENCE README.md {name}/ setup.py")
    os.system(f"git commit -m 'Pushing code for {name} version 0.1'")
    os.system(f"git remote add origin {git_repo}")
    os.system("git push -u origin master")

if __name__ == "__main__":
  main()
