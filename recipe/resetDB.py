#!/usr/bin/env python
import os
os.system("rm db/recipe.db")
os.system("python manage.py syncdb")
os.system("python populateDB.py")
