Dump sqlite3 db to a file
===

Example:

sqlite3 ./db_file .dump > output.dump



Use the conversion script
===

Ref:  https://www.redmine.org/boards/2/topics/12793?r=24983

Example usage:
```
mysql -u user -p -e "create database redmine character set utf8;" 
sqlite3 production.db .dump | sqlite3-to-mysql.py | mysql -u user -p redmine
```


Poor man MySQL backup
===
(AWS RDS has auto-backup, however it is easy to manually dump a backup as well)

Ref: http://webcheatsheet.com/sql/mysql_backup_restore.php#mysqldump

