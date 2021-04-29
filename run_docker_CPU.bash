docker create -it \
    --name erc_remote \
	--env="DISPLAY" \
	--volume="/tmp/.X11-unix:/tmp/.X11-unix" \
    --network=host \
    --volume="/dev:/dev" \
    erc_remote