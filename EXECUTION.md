# Execution

Run commands from the repository root. Replace `Rscript` with the path to the recorded R installation if several R versions are installed. Use a new output directory for each code/input version.

## Download and unpack data

```sh
python3 download_data.py --out archives
python3 reproduce_study.py --unpack-data archives --data-dir inputs
```

Downloads stream to disk; every completed ZIP is checked against its recorded size and SHA256. Existing verified archives are reused. Extraction verifies each data object's checksum. The extracted folder contains `inputs/data/`.

## Check inputs and libraries

```sh
environment/python/bin/python reproduce_study.py \
  --inputs inputs.json --data-dir inputs --out results-preflight \
  --python environment/python/bin/python \
  --rscript Rscript --r-library environment/R-primary \
  --check-inputs
```

## Run the analysis

```sh
environment/python/bin/python reproduce_study.py \
  --inputs inputs.json --data-dir inputs --out results \
  --python environment/python/bin/python \
  --rscript Rscript --r-library environment/R-primary
```

This selects the public default stages and their dependencies. Stages run sequentially. Analysis outputs, extracted producers, logs, temporary files and caches are written under `results/`.

## Select stages

```sh
python3 reproduce_study.py --list-stages
```

`Analysis_Stages.tsv` describes the stage IDs and dependencies. Add `--stages` to the run command to select individual stages or components. Examples:

```sh
# Primary mean/variability analysis and its RNA preprocessing dependency
# Append these arguments to the run command above:
--stages core.S01

# Primary analysis plus iEVORA sensitivity
--stages core.S01,core.iEVORA
```

A full run can be substantially longer and use more memory than a selected-stage run. Running stages separately is supported; do not replace participant-level independence with cell or repeated-specimen counts.

## Resume a run

Append `--resume` to reuse authenticated completed checkpoints from the same output directory. Input, code and runtime changes invalidate checkpoint reuse. Failed attempts are preserved. Append `--resume --rerun-failed` to archive a failed stage and attempt it again.

Completion and qualifications are recorded in `results/audit/Run_Summary.json`. A successful program exit or integrity check is not certification that every scientific model is appropriate.

## Optional analyses

- **Saved figures:** append `--stages FIGURES_SAVED`. This renders authenticated saved figure source data without refitting statistics. Add `--font-dir /path/to/fonts` if the original Arial font styles are not installed; font files are not distributed.
- **Discovery raw-data route:** select `core.raw_preprocessing` along with the intended core stages. Its acquisition dependency precedes preprocessing, which precedes matrix consumers. This downloads additional public raw files and requires extra storage and time.
- **Non-distributed annotated single-cell extension:** uses the embedded study analysis code but requires separately supplied, approved inputs and a dedicated R decoder. Supplied original scripts are excluded from this public code. It is not part of the public default run, and the release does not claim that this final component can be fully reproduced from the public archives alone. See the optional reader section in INSTALLATION.md.

## Inspect the code and change filenames

```sh
python3 reproduce_study.py --extract-code extracted-code
```

This exposes the embedded R/Python producers without fitting. To relocate or rename inputs, edit only the `file` paths in `inputs.json`, preserving each role, size and checksum. Alternatively omit `--inputs` and use `--data-dir` to discover the identical objects by size and SHA256. The statistical settings and sampling rules remain in the embedded producers.
