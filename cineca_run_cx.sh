#!/bin/bash
### THIS SHOULD BE CHANGED ?
#SBATCH --job-name=wimbd_cx                   # Job name
#SBATCH -o wimbd_cx-job.out                   # Name of stdout output file
#SBATCH -e wimbd_cx-job.err                   # Name of stderr error file
##SBATCH --nodes=1                              # number of nodes
##SBATCH --ntasks-per-node=1                    # number of tasks per node
##SBATCH --cpus-per-task=4                      # number of threads per task
##SBATCH --time 4:00:00                         # format: HH:MM:SS
#SBATCH --mem 30GB
##SBATCH -A IscrB_medit

module load profile/deeplrn culturax/2309

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

source $SCRIPT_DIR/wimbd-env/bin/activate

export PYTHONPATH="$SCRIPT_DIR"

echo "Running WIMBD on CULTURAX ITALIAN partition"
bash wimbd/compound_script/run.sh \
    $1 \
    arrow \
    culturax_it_wimbd_res \
    culturax \
    /leonardo/prod/data/ai/culturax/2309/it/train/*.arrow

echo "Running WIMBD on CULTURAX ENGLISH partition"
bash wimbd/compound_script/run.sh \
    $1 \
    arrow \
    culturax_en_wimbd_res \
    culturax \
    /leonardo/prod/data/ai/culturax/2309/en/train/*.arrow