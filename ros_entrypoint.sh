#!/bin/bash
set -e

# setup ros environment
source "/sim_ws/devel/setup.bash"
exec "$@"