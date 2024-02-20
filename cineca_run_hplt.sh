#!/bin/bash
### THIS SHOULD BE CHANGED ?
#SBATCH --job-name=wimbd_hplt                   # Job name
#SBATCH -o wimbd_hplt-job.out                   # Name of stdout output file
#SBATCH -e wimbd_hplt-job.err                   # Name of stderr error file
##SBATCH --nodes=1                              # number of nodes
##SBATCH --ntasks-per-node=1                    # number of tasks per node
##SBATCH --cpus-per-task=4                      # number of threads per task
##SBATCH --time 4:00:00                         # format: HH:MM:SS
#SBATCH --mem 30GB
##SBATCH -A IscrB_medit

module load profile/deeplrn hplt-datasets/1.2

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

source $SCRIPT_DIR/wimbd-env/bin/activate

export PYTHONPATH="$SCRIPT_DIR"

echo "Running WIMBD on HPLT ITALIAN partition"
bash wimbd/compound_script/run.sh \
    $1 \
    json \
    hplt_it_wimbd_res \
    hplt \
    /leonardo/prod/data/ai/hplt-datasets/1.2/it/*.jsonl

echo "Running WIMBD on HPLT ENGLISH partition"
bash wimbd/compound_script/run.sh \
    $1 \
    json \
    hplt_en_wimbd_res \
    hplt \
    /leonardo/prod/data/ai/hplt-datasets/1.2/en/*.jsonl