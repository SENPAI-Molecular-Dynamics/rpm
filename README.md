# SENPAI RPM packaging

Contains the SPEC files required to build the SENPAI RPM packages.

The packages have been tested on **Alma Linux 8.5**.

## Requirements

The build process requires `git`, `rpm-build`, `make` and `gcc`:

`# dnf install git rpm-build make gcc`

## Getting sources

Clone the repo and cd into it:

`# git clone https://github.com/SENPAI-Molecular-Dynamics/rpm && cd rpm`

## Building

Use `rpmbuild` to generate an RPM package:

`# rpmbuild -ba senpai.spec`

## Installing

Use the `rpm` tool to install the package:

`rpm -i ~/rpmbuild/RPMS/x86_64/senpai-*.rpm`

## Usage

You can now call SENPAI from your terminal:

```
╭─root@almadev ~/packaging 
╰─# senpai
   _____ _______   ______  ___    ____
  / ___// ____/ | / / __ \/   |  /  _/
  \__ \/ __/ /  |/ / /_/ / /| |  / /  
 ___/ / /___/ /|  / ____/ ___ |_/ /   
/____/_____/_/ |_/_/   /_/  |_/___/   

<< 2018-2022 SENPAI Molecular Dynamics >>
<< SENPAI and its source code are licensed under the terms of the GPLv3 license >>
<< https://senpaimd.org | https://github.com/SENPAI-Molecular-Dynamics/senpai >> 

[2022-05-03 11:13:10] [FAILED] args_model: Invalid model path... (sources/args.c:48)
[2022-05-03 11:13:10] [FAILED] args_parse: Arguments couldn't be parsed (sources/args.c:210)
[2022-05-03 11:13:10] [FAILED] SENPAI failed to execute properly (sources/main.c:33)
```
