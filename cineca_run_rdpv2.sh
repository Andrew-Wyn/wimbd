#!/bin/bash
### THIS SHOULD BE CHANGED ?
#SBATCH --job-name=wimbd_rdpv2                   # Job name
#SBATCH -o wimbd_rdpv2-job.out                   # Name of stdout output file
#SBATCH -e wimbd_rdpv2-job.err                   # Name of stderr error file
##SBATCH --nodes=1                              # number of nodes
##SBATCH --ntasks-per-node=1                    # number of tasks per node
##SBATCH --cpus-per-task=4                      # number of threads per task
##SBATCH --time 4:00:00                         # format: HH:MM:SS
#SBATCH --mem 30GB
##SBATCH -A IscrB_medit

module load profile/deeplrn red_pajama/2.0

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

source $SCRIPT_DIR/wimbd-env/bin/activate

export PYTHONPATH="$SCRIPT_DIR"

echo "Running WIMBD on RPV2 ITALIAN partition"
bash wimbd/compound_script/run.sh \
    $1 \
    json \
    redpajamav2_it_wimbd_res \
    redpajamav2 \
    $(find /leonardo/prod/data/ai/red_pajama/2.0/it/documents/ -name '*.json')

echo "Running WIMBD on RPV2 ENGLISH partition"
bash wimbd/compound_script/run.sh \
    $1 \
    json \
    redpajamav2_en_wimbd_res \
    redpajamav2 \
    $(find /leonardo/prod/data/ai/red_pajama/2.0/en/documents/ -name '*.json')