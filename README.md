# fastAPI-template

## Introduction
This is a template for FastApi with Postgresql.


## Folder tree
```
fastAPI-template
│   .gitignore
│   docker-compose.yaml
│   Dockerfile_Back
│   Dockerfile_Base
│   Makefile
│   README.md
│
├───env
│       requirements.txt
│
└───src
    │   main.py
    │   run.py
    │
    ├───config
    │       EnumApp.py
    │
    ├───model
    │       rename.py
    │
    └───schema
            schema.py
```

### env 
Write your packages name in requirements.txt.You can use this cmd to install all packages in requirements.txt.
```
pip install -r requirements.txt
```

### src
Develop here, run.py is your endpoint, just run it.

#### config 
Put your config file here.

#### model
Control database here, crtl + F "rename" to rename what you want.

#### schema
Define database schema, request Body and every schema you need here.




