#!/usr/bin/env python
import os
os.system("heroku pg:reset DATABASE_URL --confirm recicopy")
os.system("python manage.py syncdb")
os.system("python populateDB.py")
