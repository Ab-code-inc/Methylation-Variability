# Third-party sources and licenses

This is a source-code collection for scientific reproduction. Original third-party attribution and license notices remain applicable. The analysis entry point exposes its embedded sources with `--extract-code`; dependencies are installed from the source versions recorded in `renv.lock` and `requirements-analysis.txt`.

## EpiSCORE

Original author: Andrew E. Teschendorff. The pinned EpiSCORE package declares **GPL-2**. Its original functions and reference objects are included for the cell-reference analysis. The source repository and exact commit are recorded in `renv.lock`:

https://github.com/aet21/EpiSCORE

The full GPL version 2 text is provided in `GPL-2.0.txt`. Original source attribution is retained in the extracted files.

## iEVORA

The embedded author-original iEVORA source explicitly declares **GPL-3**, with copyright 2015 Andrew Teschendorff. Original and adapted iEVORA sources retain that attribution. The author-original function is exposed as `core/iEVORA_author_original.txt` by `--extract-code`.

The full GPL version 3 text is provided in `GPL-3.0.txt`. iEVORA is used as a sensitivity analysis; DiffVar is the primary variability method.

## SCDC

SCDC retains its original MIT license and copyright notice, reproduced in `SCDC_LICENSE.txt`. The source commit is recorded in `renv.lock`; the software reference is in `Software_Citations.tsv`.

## Other installed dependencies and data

Installed R and Python packages retain their individual licenses. Public data providers and source studies retain their applicable data-use terms and attribution. The source collection does not apply a blanket MIT license to GPL-covered sources or change a provider's terms.
