"""
Shared storage configuration for Satellite NeRF research.

The same code is used on Colab, Kaggle and the local RTX A4000 machine.
GCS is the persistent source of truth for datasets, checkpoints and outputs.
"""

GCS_BUCKET = "sn-project-dataset-2026-0604"

DATASET_ROOT = f"gs://{GCS_BUCKET}/datasets"
RAW_DATASET_ROOT = f"{DATASET_ROOT}/raw"
PROCESSED_DATASET_ROOT = f"{DATASET_ROOT}/processed"

OUTPUT_ROOT = f"gs://{GCS_BUCKET}/outputs"
EXPERIMENT_ROOT = f"{OUTPUT_ROOT}/experiments"

SCENE = "JAX_068"

RAW_SCENE_ROOT = f"{RAW_DATASET_ROOT}/{SCENE}"
IMAGE_ROOT = f"{RAW_SCENE_ROOT}/images"
METADATA_ROOT = f"{RAW_SCENE_ROOT}/metadata"


def experiment_root(experiment_name: str) -> str:
    """Return the persistent GCS root for an experiment."""
    return f"{EXPERIMENT_ROOT}/{experiment_name}"


def checkpoint_root(experiment_name: str) -> str:
    """Return the persistent checkpoint directory."""
    return f"{experiment_root(experiment_name)}/checkpoints"


def metrics_root(experiment_name: str) -> str:
    """Return the persistent metrics directory."""
    return f"{experiment_root(experiment_name)}/metrics"


def renders_root(experiment_name: str) -> str:
    """Return the persistent render directory."""
    return f"{experiment_root(experiment_name)}/renders"


def logs_root(experiment_name: str) -> str:
    """Return the persistent logs directory."""
    return f"{experiment_root(experiment_name)}/logs"


def configs_root(experiment_name: str) -> str:
    """Return the persistent experiment configuration directory."""
    return f"{experiment_root(experiment_name)}/configs"
