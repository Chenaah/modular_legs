
# Reconfigurable Legged Metamachines that Run on Autonomous Modular Legs

This repository contains the codebase for the paper "Reconfigurable Legged Metamachines that Run on Autonomous Modular Legs" (under review). The code is currently undergoing active development and cleanup. In the coming updates, we will release additional training examples, debugging tools, pretrained models, tutorials, a more user-friendly API, and documentation for customizing the morphology optimization pipeline.

Stay tuned for improvements and expanded functionality. If you run into any issues or have suggestions, we welcome your feedback and contributions!


## Installation

Create a Conda environment with Python 3.10
```bash
conda create -n modular_legs python=3.10
conda activate modular_legs
```

Install the full version (including Bayesian optimization support):
```bash
pip install -e .[full]
```

Or install the minimal version without Bayesian optimization:
```bash
pip install -e .
```


## Usage

### Train a specific metamachine

Train a single module:
```bash
python modular_legs/scripts/train_sbx.py sim_train_m3air1s
```

Train a quadruped using curriculum learning:
```bash
python modular_legs/scripts/train_sbx.py curriculum/quadrupedX4air1s
```
Training logs and checkpoints will be saved to the `exp` directory.


### Run a policy on the real metamachines
```bash
python modular_legs/scripts/train_sbx.py real_play_quadrupedX4air1s
```

### Generate custom metamachines
Example of generating a Mujoco XML from a configuration encoding:
```bash
python modular_legs/sim/scripts/homemade_robots_asym.py
```

### Run bayesian optimiation 
```
python modular_legs/scripts/evolve.py evolution_vae_asym_air1s
```


## Citation

If you find this work useful, please cite:

```bibtex
@misc{yu2025reconfigurable,
  title={Reconfigurable Legged Metamachines that Run on Autonomous Modular Legs},
  author={Chen Yu and David Matthews and Jingxian Wang and Jing Gu and Douglas Blackiston and Michael Rubenstein and Sam Kriegman},
  year={2025},
  eprint={2505.00784},
  archivePrefix={arXiv},
  primaryClass={cs.RO}
}
```