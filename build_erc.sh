build_erc(){
    echo "Building ERC UR3"
    docker build -f Dockerfile --no-cache --tag erc_remote .
}

build_erc