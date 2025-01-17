FROM osrf/ros:melodic-desktop

# Install some tools
RUN apt-get update && apt-get -y upgrade && apt-get install -y \
    python-rosdep \
    python-catkin-tools \
    python-vcstool \
    python-pip \
    htop \
  && rm -rf /var/lib/apt/lists/*

# Clone the source code
WORKDIR /sim_ws
COPY *.repos ./
RUN vcs import < dependencies.repos
RUN vcs import < kamayuc-erc.repos
RUN vcs import < leo-erc.repos

# Install dependencies
RUN apt-get update \
  && rosdep update \
  && rosdep install --from-paths src -iy \
  && rm -rf /var/lib/apt/lists/*

# Build the workspace
RUN catkin config --extend /opt/ros/melodic --no-install && catkin build

# Modify the entrypoint file
COPY ros_entrypoint.sh /