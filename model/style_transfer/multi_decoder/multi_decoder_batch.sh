#!/bin/sh
#BATCH -A schowdhury
#SBATCH -n 1
#SBATCH --gres=gpu:1
#SBATCH --mem-per-cpu=12G
#SBATCH --time=20:00:00
#SBATCH --mail-type=ALL
#SBATCH --reservation=cvit-trial


module load cuda/9.0
module load cudnn/7-cuda-9.0
module load openmpi/2.1.1-cuda9



# source ~/v_python/bin/activate
export THEANO_FLAGS=device=cuda,floatX=float32,lib.cnmem=0.8

# export CUDA_ROOT=~/cuda/cuda-9.0
# export CUDA_HOME=~/cuda/cuda-9.0
# export PATH=${CUDA_HOME}/bin:$PATH
# export LD_LIBRARY_PATH=${CUDA_HOME}/lib64:$LD_LIBRARY_PATH


bash ~/style_transfer/style_transfer_in_text/model/style_transfer/session_multi_decoder/train.sh


