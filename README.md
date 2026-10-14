# Methylation variability in gingival tissue

Code, processed input data and figure source data for a reanalysis of publicly available gingival methylation and matched RNA measurements. The discovery dataset contains 36 independent participants: 12 healthy, 12 with gingivitis and 12 with Stage III periodontitis.

The study asks how methylation varies between people, alongside the conventional comparison of average methylation. **DiffVar is the primary variability analysis; iEVORA is a sensitivity analysis.** Candidate-level analyses cover GHDC, LYPLAL1, SIM2 and ZNF155. Additional analyses examine participant structure, omission sensitivity, nuisance variables, pathways, external disease contexts, public single-cell expression and machine-learning transfer.

## Start here

1. [Install Python, R and the recorded libraries](INSTALLATION.md).
2. [Download, verify and unpack the data](EXECUTION.md#download-and-unpack-data).
3. [Run the analysis or selected stages](EXECUTION.md#run-the-analysis).

The large data ZIPs are attached to [release v1.0.0](https://github.com/Ab-code-inc/Methylation-Variability/releases/tag/v1.0.0), rather than committed to Git. `download_data.py` downloads them sequentially and checks their SHA256 hashes. `Data_Release_Assets.tsv` gives every filename, byte count, checksum and download URL.

`reproduce_study.py` is the single analysis entry point. It contains the R/Python analysis producers and extracts them into the selected output directory. Statistical calculations use the specialist libraries listed in `Dependencies.json`, `requirements-analysis.txt`, `renv.lock` and `Software_Citations.tsv`. Data roles are mapped through `inputs.json`; no original project directory or computer-specific path is required.

## Reproduction scope

The standard starting point is the processed methylation/RNA matrices and processed external-cohort/public-atlas inputs. The optional discovery raw-data route is documented in [EXECUTION.md](EXECUTION.md#optional-analyses). Original provider preprocessing for every external resource is not reconstructed.

The final analysis of separately supplied, annotated single-cell objects is excluded from the public default run. Those objects and their supplied scripts are not distributed. The study's own aggregate result tables may be retained as figure source data; rendering those saved tables is distinct from rerunning the underlying single-cell analysis.

Freshly computed outputs are written to a new directory, with stage logs, input identities and checkpoints. `--resume` continues authenticated completed stages; it does not turn a failed analysis into a successful one. The code retains recorded statistical qualifications and unsuccessful tests. External disease and single-cell expression findings provide context; they are not independent replication of gingival variability or proof of a cellular mechanism.

See `Reproduction_Scope.tsv` and `Validation_Status.json` for the analyses and verification limits included in this release. A complete clean installation and every transfer-model refit have not been independently repeated for this release. Recorded runtimes were tested on macOS; Linux and Windows have not been verified.

## Data and software attribution

`Data_Inputs.tsv` records the input roles and file identities. `Data_Sources.md` describes data provenance and use. `Software_Citations.tsv` provides software references. Third-party software retains its own licensing; the bundled SCDC license is included. Original source publications and data providers should be cited when reusing their data.
