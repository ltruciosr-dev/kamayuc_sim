build_erc(){
    echo "Building ERC UR3"
    docker build -f Dockerfile --no-cache --tag erc_sim .
}

build_erc