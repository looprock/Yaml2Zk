About:

This is a simple script for importing yaml configurations into zookeeper. 

Requirements: python2, PyYaml, kazoo

Usage: yaml2zk [zookeeper server] [zookeeper base znode (NO TRAILING SLASH!)] [yaml file]

Example: 
[ bash ~] yaml2zk zookeeper.machine.com '/test' ~/config.yaml
Adding: /test/backup_dir, value: /tmp/
Adding: /test/new_deploy/remote_copy_mode, value: rsync
Adding: /test/new_deploy/skip_backup, value: True
Adding: /test/new_deploy/uncompressed_downloads, value: False
Adding: /test/new_deploy/enabled, value: True
Adding: /test/new_deploy/skip_local_snapshot_verify, value: True

Caveats: 
Sorry, I didn't incorporate zk ports or auth into this but that should be trivial to implement.
All the values are converted into strings. Not sure if this is a limitation on zookeeper or kazoo but if I tried to load any other type I got an error.
