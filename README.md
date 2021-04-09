# ERC 2021 Workspace

This repository contains simulations of the Kamayuc and Leo rovers developed from the [Kamayuc Team](https://www.facebook.com/Kamayuc) for the ERC2021 Challengue.

## Requirements

The simulation is mainly developed and tested on [Ubuntu 18.04 Bionic Beaver](https://releases.ubuntu.com/18.04/) with [ROS Melodic Morenia](http://wiki.ros.org/melodic/Installation/Ubuntu), so it is a recommended setup. 

The rest of the tools used in this guide can be installed with apt:
```
sudo apt install python-rosdep python-catkin-tools python-vcstool
```

There is also a dockerized version which should work on most Linux distributions running X Window Server (See [Docker Setup](#docker-setup) section).

## Building

It is recommended to create a dedicated workspace for the competition and copy there the `repos` files.
```
mkdir -p ~/ros/kamayuc_ws/
cp *.repos ~/ros/kamayuc_ws/
cd ~/ros/kamayuc_ws/
```

Use the `vcstool` tool to clone the required packages:
```
vcs import < kamayuc-erc.repos
vcs import < leo-erc.repos
```
---
**NOTE**

If your account has a SSH agent connected to the [Kamayuc Gitlab project](https://gitlab.com/team-kamayuc/rover_navigation/kamayucrover), import `kamayuc-erc-ssh.repos` instead of `kamayuc-erc.repos`.

---

Use the `rosdep` tool to install any missing dependencies. If you are running `rosdep` for the first time, you might have to run:
```
sudo rosdep init
```

first. Then, to install the dependencies, type:
```
rosdep update
sudo apt update
rosdep install --rosdistro melodic --from-paths src -iy
```

Now, use the `catkin` tool to build the workspace:
```
catkin config --extend /opt/ros/melodic
catkin build
```

## Updating

The list of the repositories may change, so make sure you have pulled the latest commit:
```
git pull
```

Use `vcstool` tool to clone any new repositories:
```
vcs import < kamayuc-erc.repos
vcs import < leo-erc.repos
```
---
**NOTE**

If your account has a SSH agent connected to the [Kamayuc Gitlab project](https://gitlab.com/team-kamayuc/rover_navigation/kamayucrover), import `kamayuc-erc-ssh.repos` instead of `kamayuc-erc.repos`.

---

And pull the new commits on the already cloned ones:
```
vcs pull src
```

Then, make sure you have all the dependencies installed:
```
rosdep install --rosdistro melodic --from-paths src -iy
```

And rebuild the workspace:
```
catkin build
```

## Docker Setup

It is needed to install [docker](https://docs.docker.com/engine/install/ubuntu/) and [nvidia-docker](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html)

---
**NOTE**

The commands in this section should be executed as the `root` user, unless you have configured docker to be [managable as a non-root user](https://docs.docker.com/engine/install/linux-postinstall/).

---

Make sure the [Docker Engine](https://docs.docker.com/engine/install/#server) is installed and the `docker` service is running:
```
systemctl start docker
```

Edit the file [kamayuc-erc.repos](kamayuc-erc.repos) and add your gitlab credentials, to be able to install kamayuc private repositories.
```
url: https://<username>:<password>@gitlab.com/team-kamayuc/rover_navigation/<package>.git
```

Build the docker image by executing:
```
./build_erc.sh 
```

To use an Nvidia card, you need to previously install proprietary drivers and Nvidia Container Toolkit (https://github.com/NVIDIA/nvidia-docker). Next execute command:
``` 
bash run_docker_NVIDIA.bash
```

There are two ways to execute nodes and interact with the simulation inside the docker:

1. The docker container should be visibile inside the vscode `remote-container` [pluggin](#docker-vscode), you can start the docker there.

2. The typical docker configuration via linux [terminal](#docker-local).

## Docker Run

---
**NOTE**

Run the following command every time your computer is restarted.
```
xhost +local:root
```
---

### **1. Local Docker**

Start the container:
```
docker start erc_sim
```

To start any other ROS nodes inside the container, type:
```
docker exec -it erc_sim /ros_entrypoint.sh <COMMAND>
```

For example:
```
docker exec -it erc_sim /ros_entrypoint.sh roslaunch leo_gazebo leo_marsyard.launch
```

To update the docker image, you need to rebuild it with `--no-cache` option:
```
docker build --no-cache -t erc_sim .
```

### **2. VSCode Docker**

VSCode has the `Remote - Containers` pluggin, which can be used to dorectly interact with the Docker container. This tool is needed to download private repositories, because of the necessity of input credentials.

After installing [VSCode](https://code.visualstudio.com/docs/setup/linux), let's add the [Remote - Containers](https://github.com/Microsoft/vscode-remote-release) pluggin.

Follow this [tutorial](https://code.visualstudio.com/docs/remote/containers) to add your docker into VSCODE.

Once inside a Docker terminal, to start any ROS nodes type:
```
/ros_entrypoint.sh <COMMAND>
```

For example:
```
/ros_entrypoint.sh roslaunch leo_gazebo leo_marsyard.launch
```

Moreover, you can source the workspace and explore all the available launchs.
```
source /sim_ws/devel/setup.bash
roslaunch <package> <launch>
```
