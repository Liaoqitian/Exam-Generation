# Exam Generation

PrairieLearn (PL) course setup for CS10


## Table of Contents
  - [Interface Demonstration](#Interface-Demonstration)
  - [Basic Setup](#basic-setup)
  - [Basic Usage](#basic-usage)
  - [Examples](#examples)
  - [Contributing](#contributing)

## Interface Demonstration 
![alt text](https://github.com/Liaoqitian/Exam-Generation/blob/master/Interface%20Demo/latest.png "Interface Demo")
## Basic Setup

For detailed instructions to set up PrairieLearn, please direct to [Installing and running PrairieLearn](https://prairielearn.readthedocs.io/en/latest/installing/)

*You must have Docker installed on your system for the following to work!* For Docker download and startup guide, direct to [here](https://docs.docker.com/)


1. Start Docker application on your machine.

2. Clone the course repo to your machine e.g. your desktop

3. Mount PL to course repo. If you cloned the repo to your desktop, it will look like this:

```bash
docker run -it --rm -p 3000:3000 \
    -v "$PWD":/course `# Map your current directory in as course content` \
    -v "$HOME/Desktop/pl-cs10/pl_ag_jobs:/jobs" `# Map jobs directory into /jobs` \
    -e HOST_JOBS_DIR="$HOME/Desktop/pl-cs10/pl_ag_jobs" \
    -v /var/run/docker.sock:/var/run/docker.sock `# Mount docker into itself so container can spawn others` \
    prairielearn/prairielearn
```

4. Once the Docker Container has been initialized, go to [http://localhost:3000/pl](http://localhost:3000/pl)

5. Click `Load from disk` on top-right corner of the page. As long as no error is raised, you can navigate to your desired page.

## Basic Usage

For each new question you author, place the folder containing relevant files and directories inside `questions/`

## Examples

Examples can be found inside the official codebase under [exampleCourse](https://github.com/PrairieLearn/PrairieLearn/tree/master/exampleCourse)

