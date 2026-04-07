# 01-setup.js — line-by-line analysis

## Lines 1-8
- Notes init script purpose, switches to `nasiko` database, and starts createUser call.

## Lines 9-16
- Defines admin username/password and assigns dbOwner role for `nasiko`.

## Lines 17-24
- Adds global admin roles userAdminAnyDatabase and dbAdminAnyDatabase.

## Lines 25-32
- Adds readWriteAnyDatabase and clusterAdmin roles, closes roles list.

## Lines 33-36
- Closes createUser call and prints success message.
