# ERC PACHACUTEC Simulation

This repository contains simulations of the Kamayuc and Leo rovers created for the ERC competition. You need to install [docker](https://docs.docker.com/engine/install/ubuntu/) and [nvidia-docker](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html)

# 1. Docker Setup

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

# 2. ERC Simulation

---
**NOTE**

Run the following command every time your computer is restarted.
```
xhost +local:root
```
---

## Docker local

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

## Docker vscode

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
