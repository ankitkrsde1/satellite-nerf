# Satellite-NeRF

A research framework for satellite-image-based 3D reconstruction and novel view synthesis.

## Research Models

- Sat-NeRF
- SPS-NeRF
- EO-NeRF
- EOGS

## Dataset

DFC2019 — JAX_068

The raw dataset is kept outside Git and stored in persistent storage.

## Shared Research Infrastructure

The project is designed around reusable components:

- Dataset handling
- Coordinate systems
- RPC camera model
- Camera geometry
- Ray generation
- Ray sampling
- Solar geometry
- Shadow and visibility
- Neural scene representation
- Gaussian scene representation
- Rendering
- Loss functions
- Training
- Evaluation

The shared infrastructure is implemented once and reused across all research models.

## Compute Environments

The same codebase is designed to run on:

- Google Colab
- Kaggle
- Google Cloud VM
- Offline NVIDIA RTX A4000 workstation

Compute environments are treated as disposable.

## Storage Architecture

Git stores:

- Source code
- Configuration
- Tests
- Documentation
- Docker/environment definitions

Persistent storage stores:

- Raw datasets
- Processed datasets
- Test subsets
- Training checkpoints
- Experiment outputs
- Evaluation results
- Rendered results

## Research Principle

Build infrastructure once -> validate once -> reuse across all models.

## Development Principle

Implement -> Test -> Verify -> Freeze -> Next Step

We do not move to the next subsystem until the current subsystem has been validated.
