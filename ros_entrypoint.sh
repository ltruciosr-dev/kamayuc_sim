#!/bin/bash
set -e

# setup ros environment
source "/rover_ws/devel/setup.bash"
exec "$@"