# Data sources and use

## Gingival discovery measurements

- DNA methylation: [GSE173081](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE173081).
- Matched bulk RNA: [GSE173078](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE173078).
- Original study: [Kim and colleagues, 2021](https://pmc.ncbi.nlm.nih.gov/articles/PMC8376779/).

These are measurements from 36 independent people, with 12 participants in each of the healthy, gingivitis and Stage III periodontitis groups. They are not 12 people measured in three conditions. The release contains authenticated processed inputs used for the reanalysis; the optional discovery raw-data route retrieves public original assay files.

## External contexts and paired-source models

External analyses use public methylation cohorts, adult-tissue references and paired methylation–RNA resources. The broad transfer analysis includes TCGA head-and-neck, lung adenocarcinoma and lung squamous-cell cohorts, and GTEx tissue references. The inflammatory transfer analysis uses source cohorts with verified participant/specimen pairing. Clinical classifications within the gingival cohort and externally trained RNA-transfer models are different analyses.

Accession numbers, source URLs, specimen/donor pairing, inclusion/exclusion decisions and study limits are retained in the relevant source registries and manifests exposed by:

```sh
python3 reproduce_study.py --extract-code extracted-code
```

`Data_Inputs.tsv` links every distributed object's identity to its scientific input role and analysis stages. Public participant/sample identifiers are retained where needed to reproduce donor grouping and prevent repeated specimens from being treated as independent people.

External disease comparisons provide biological context. They do not constitute independent gingival periodontitis replication, establish uniform U.S. ancestry, or demonstrate that a methylation finding has the same cause across diseases. Frozen literature and mQTL records are evidence inputs; the code does not reconstruct historical searches or perform a new genetic association study.

## Public single-cell and reference inputs

The public periodontal expression route includes [GSE171213](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE171213). The supplied, manually annotated single-cell objects used in the final additional analysis are not distributed. Their separate scripts are also excluded. The study's own aggregate effect estimates and figure source statistics are distinct from those non-distributed inputs.

EpiSCORE reference objects and original functions come from the pinned [EpiSCORE source repository](https://github.com/aet21/EpiSCORE), under its declared GPL-2 license. See `renv.lock`, `Software_Citations.tsv` and `THIRD_PARTY_NOTICES.md` for source versions and attribution. Independent RNA localisation is compatible-expression evidence, not measured cell-specific DNA methylation or proof of causal cellular origin.

## File identities and source terms

`inputs.json` records public input roles, filenames, sizes and SHA256 hashes. `Data_Release_Assets.tsv` records ZIP-level identities and download URLs. Each ZIP contains an `ARCHIVE_CONTENTS.json` identifying every member. Computer-specific filesystem metadata has been removed from public copies without changing numerical measurements or original scientific qualifications.

Processed study derivatives are distinguished from provider files through their input roles and provenance. Cite the original studies and observe their applicable data-use terms. Third-party software and reference objects retain their published licenses; this release does not replace them with a new blanket license.
