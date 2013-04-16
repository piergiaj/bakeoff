#!/usr/bin/env python
import os
os.system("rm db/recipe.db")
os.system("manage.py syncdb")
os.system("populateDB.py")