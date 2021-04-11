xhost + local:root

docker create -it \
    --name erc_sim \
    --gpus all \
    --net=host \
	--env="DISPLAY" \
	--volume="/tmp/.X11-unix:/tmp/.X11-unix" \
    --env="NVIDIA_VISIBLE_DEVICES=all" \
    --env="NVIDIA_DRIVER_CAPABILITIES=all" \
	--privileged \
    --volume="/dev:/dev" \
    erc_sim