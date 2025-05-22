from setuptools import setup, find_packages


setup(
    name="modular_legs",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "modular_legs",
        "pyyaml",
        "omegaconf",
        "gymnasium",
        "gymnasium[other]",
        "sbx-rl",
        "wandb",
        "mujoco",
        "lxml",
        "pytorch_lightning",
        "imageio",
        "tensorboard",
        "jax[cuda12]",
    ],
    extras_require={
        "full": [
            "ray",
            "mujoco-mjx",
            "tensorflow",
            "trieste",
        ],
    },
)