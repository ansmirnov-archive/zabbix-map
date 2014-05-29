Dump
====

`echo '.dump main_switch' | python manage.py dbshell > main_switch.sql`

`echo '.dump main_point' | python manage.py dbshell > main_point.sql`


Delete old tables
=================

`python manage.py dbshell`

`DROP TABLE main_point`

`DROP TABLE main_switch`

... GIT PULL ...


Restore
=======

`python manage.py dbshell`

`.read main_point.sql`

`.read main_switch.sql`