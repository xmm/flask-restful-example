#! /bin/bash

full_path=`readlink -f "$0"`
TOP_DIR=${full_path%%/bin/runner.sh}
PROJ_DIR=$TOP_DIR

source $TOP_DIR/venv/bin/activate

export PYTHONPATH=$PYTHONPATH:$PROJ_DIR
cd $PROJ_DIR

exec python $@
