# CS10 Beauty and Joy of Computing

PrairieLearn (PL) course setup for CS10

For template README, please direct to [ACE-LAB README](https://github.com/ace-lab/pl-ucb-csxxx/blob/master/README.md)

## Table of Contents

- [CS10 Beauty and Joy of Computing](#cs10-beauty-and-joy-of-computing)
  - [Table of Contents](#table-of-contents)
  - [Basic Setup](#basic-setup)
  - [Basic Usage](#basic-usage)
  - [Examples](#examples)
  - [Contributing](#contributing)

## Basic Setup

For detailed instructions to set up PrairieLearn, please direct to [Installing and running PrairieLearn](https://prairielearn.readthedocs.io/en/latest/installing/)

*You must have Docker installed on your system for the following to work!* For Docker download and startup guide, direct to [here](https://docs.docker.com/)


1. Start Docker application on your machine.

If you have already cloned the course repo, skip to Step 3

2. Clone the course repo to your machine e.g. your desktop

```bash
% cd ~/Desktop
% git clone git@github.com:ace-lab/pl-ucb-cs10.git
```

3. Mount PL to course repo. If you cloned the repo to your desktop, it will look like this:

```bash
docker run -it --rm -p 3000:3000 -v ~/Desktop/pl-ucb-cs10:/course prairielearn/prairielearn
```

or

```bash
docker run -it --rm -p 3000:3000 -v <Directory Location>/pl-ucb-cs10:/course prairielearn/prairielearn
```

4. Once the Docker Container has been initialized, go to [http://localhost:3000/pl](http://localhost:3000/pl)

5. Click `Load from disk` on top-right corner of the page. As long as no error is raised, you can navigate to your desired page.

## Basic Usage

For each new question you author, place the folder containing relevant files and directories inside `questions/`

## Examples

Some examples can be found inside ACE-LAB [template](https://github.com/ace-lab/pl-ucb-csxxx)
or inside the official codebase under [exampleCourse](https://github.com/PrairieLearn/PrairieLearn/tree/master/exampleCourse)

## Contributing

Please refer to [CONTRIBUTING.md](CONTRIBUTING.md)
