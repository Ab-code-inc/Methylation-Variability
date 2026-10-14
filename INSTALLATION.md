# Installation

The recorded numerical environment uses **Python 3.12.14**, **R 4.6.1** and **Bioconductor 3.23**. Installation needs internet access. Keep the repository, input archives, extracted inputs, environments and results on a disk with sufficient free space.

## 1. Obtain the repository

```sh
git clone https://github.com/Ab-code-inc/Methylation-Variability.git
cd Methylation-Variability
```

Alternatively, download and extract the repository ZIP from GitHub.

## 2. Install Python libraries

Install Python 3.12, preferably the recorded patch version. Create an isolated environment:

```sh
python3.12 -m venv environment/python
environment/python/bin/python -m pip install --upgrade pip
environment/python/bin/python -m pip install -r requirements-analysis.txt
```

The requirements file pins the 45 distributions recorded in the macOS environment. Linux/Windows may introduce platform-specific dependencies; those environments have not been independently verified. On Windows, use `environment\python\Scripts\python.exe` in place of `environment/python/bin/python`.

## 3. Restore R libraries

Install R 4.6.1. Run from the repository root:

```sh
mkdir -p environment/R-primary
Rscript -e 'options(repos=c(CRAN="https://cloud.r-project.org")); install.packages("renv", lib="environment/R-primary")'
Rscript -e '.libPaths(c(normalizePath("environment/R-primary"), .libPaths())); options(repos=c(CRAN="https://cloud.r-project.org")); renv::restore(lockfile="renv.lock", library=normalizePath("environment/R-primary"), prompt=FALSE)'
```

The lock records 238 package/version/source identities, including `renv`; it retains Bioconductor metadata and pinned GitHub commits. It includes missMethyl/DiffVar, limma, DMRcate, minfi, edgeR, annotation resources, single-cell libraries and figure libraries. Do not substitute a different Bioconductor release without treating it as a changed environment.

Source builds may require a C/C++ compiler, Fortran, curl/SSL, XML, HDF5 and font/image system libraries. Install the relevant system dependencies for your operating system when an installer reports them missing. The restored numerical environment has been exercised on macOS; a fresh installation on every operating system has not been verified.

The public default analysis does not require the separate older R/`qs` reader used for the non-distributed annotated single-cell objects.

## 4. Verify installation

After downloading and unpacking the inputs, run the `--check-inputs` command in [EXECUTION.md](EXECUTION.md#check-inputs-and-libraries). It verifies selected data identities and installed library metadata without fitting models. An input check is not a fresh scientific reproduction.

## Optional reader for separately supplied inputs

The optional `supplied_extract` stage uses **R 4.5.3** and the eight packages recorded in `renv-reader.lock`. Restore this lock with that R installation into a separate `environment/R-reader` library, using the same bootstrap/restore procedure above. The primary analysis library remains R 4.6.1. Do not load the older reader into the primary R runtime.

The raw annotated objects are not part of this release. If you have approved copies, create an additional input manifest using the same schema and code-spec identity as `inputs.json`, retaining the public entries and adding the three documented supplied input roles from the extracted specification. Preserve their required SHA256/size identities. Then add these arguments to the run command:

```sh
--inputs inputs-with-approved-supplied-data.json \
--stages supplied_extract,supplied_models,supplied_check \
--rscript-profile supplied_reader=/path/to/R-4.5.3/bin/Rscript \
--r-library-profile supplied_reader=environment/R-reader
```

Reader package versions, use and citations are listed separately in `Optional_Reader_Dependency_Evidence.json` and `Optional_Reader_Software_Citations.tsv`. These are unnecessary for the public default analysis.
