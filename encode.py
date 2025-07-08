"""VCF Encoding Module for SecureGenomics Protocol - Alzheimer's Disease Allele Frequency Analysis."""

from typing import List, Dict, Any, TextIO
import pysam


# These are the most clinically significant and population-variable SNPs for AD research
TARGET_VARIANTS_ALZHEIMERS = [
    ("rs429358", 12.0),    # APOE ε4 homozygotes, OR up to ~12× for late-onset AD :contentReference[oaicite:1]{index=1}
    ("rs7412", 0.62),      # APOE ε2 is protective (~38% reduced risk) :contentReference[oaicite:2]{index=2}
    ("rs2075650", 2.0),    # TOMM40 – linked to APOE ε4, OR ~2–4×  
    ("rs199768005", 4.0),  # Rare APOE variant, pathogenic significance  
    ("rs6857", 1.3),       # NECTIN2 – age-at-onset modifier
    ("rs11136000", 1.19),  # CLU, OR≈1.19  
    ("rs3851179", 1.18),   # PICALM, OR≈1.18  
    ("rs6733839", 1.22),   # BIN1, OR=1.22  
    ("rs6656401", 1.18),   # CR1, OR≈1.18  
    ("rs3764650", 1.23),   # ABCA7, OR≈1.23  
]


TARGET_VARIANTS_SCHIZOPHRENIA = [
    ("rs1344706", 1.12),  # ZNF804A – meta-analysis shows OR~1.12 for A allele :contentReference[oaicite:3]{index=3}
    ("rs13194053", 1.10), # MHC/HLA region, immune-linked variant  
    ("rs1006737", 1.15),  # CACNA1C – common calcium-channel SNP  
    ("rs10994336", 1.10), # ANK3 – modest effect  
    ("rs6994992", 1.10),  # NRG1 – developmental gene  
    ("rs13242038", 1.10), # GRM3 – glutamate receptor  
    ("rs4570625", 1.10),  # TPH2 – serotonin biosynthesis  
    ("rs4680", 1.15),     # COMT Val158Met – dopamine metabolism  
    ("rs6265", 1.15),     # BDNF Val66Met – neurotrophic factor  
    ("rs1800497", 1.10),  # DRD2 – dopamine receptor  
]

TARGET_VARIANTS_BREAST_CANCER = [
    ("rs2981579", 1.43),  # FGFR2 – proxy for rs1219648, OR≈1.43 :contentReference[oaicite:4]{index=4}
    ("rs3803662", 1.28),  # TOX3 – OR≈1.28  
    ("rs1045485", 1.10),  # CASP8 – apoptosis gene  
    ("rs2981582", 1.19),  # FGFR2 intron 2, OR≈1.19 :contentReference[oaicite:5]{index=5}
    ("rs1801516", 1.10),  # ATM – DNA repair  
    ("rs17879961", 1.50), # CHEK2 I157T – moderate penetrance  
    ("rs11515", 1.10),    # CDKN2A – tumor suppressor  
    ("rs25487", 1.10),    # XRCC1 – DNA repair  
    ("rs80357713", 5.0),  # BRCA1 truncating mutation  
    ("rs11571833", 5.0),  # BRCA2 truncating mutation  
    ("rs180177102", 3.0), # PALB2 – moderate-to-high risk  
    ("rs555607708", 3.0), # CHEK2 1100delC – moderate penetration  
]


TARGET_VARIANTS_PROSTATE_CANCER = [
    ("rs10993994", 1.20),  # MSMB T allele, meta‑analysis shows OR ≈ 1.20 in Caucasians:contentReference[oaicite:4]{index=4}
    ("rs10896449", 1.10),  # Chr11q13 variant, OR ≈ 1.10
    ("rs4245739", 1.12),   # MDM4 3′‑UTR, OR ≈ 1.12
    ("rs16901979", 1.44),  # 8q24 region 2, OR ≈ 1.44 in East Asians
    ("rs1447295", 1.20),   # 8q24 region 1, OR ≈ 1.20
    ("rs10086908", 1.10),  # 8q24 region 5
    ("rs1512268", 1.10),   # 8p21 region
]

TARGET_VARIANTS_TYPE2_DIABETES = [
    ("rs7903146", 1.40),   # TCF7L2 T allele, OR ≈ 1.37–1.45:contentReference[oaicite:0]{index=0}:contentReference[oaicite:1]{index=1}
    ("rs13266634", 1.15),  # SLC30A8 C allele, common ZnT8 variant:contentReference[oaicite:2]{index=2}
    ("rs1801282", 1.14),  # PPARG Pro12Ala, OR ≈ 1.14 (protective A allele)
    ("rs10923931", 1.12),  # IGF2BP2, OR ≈ 1.12–1.15 in multiple studies:contentReference[oaicite:3]{index=3}
    ("rs4402960", 1.12),  # IGF2BP2 alternate, similar effect
    ("rs5215", 1.10),     # KCNJ11 E23K, OR ≈ 1.10
]

TARGET_VARIANTS_CORONARY_ARTERY_DISEASE = [
    ("rs1333049", 1.47),   # 9p21 C allele, OR ≈ 1.47 for heterozygotes; homozygotes ~1.9 risk:contentReference[oaicite:5]{index=5}
    ("rs662799", 1.15),    # APOA5 variant affecting triglycerides, OR ≈ 1.15
    ("rs6922269", 1.10),   # MTHFD1L, OR ≈ 1.10
    ("rs2943634", 1.10),   # 2q36.3 intergenic, OR ≈ 1.10
    ("rs501120", 1.10),    # CXCL12 upstream, OR ≈ 1.10
    ("rs17228212", 1.10),  # SMAD3, OR ≈ 1.10
    ("rs9818870", 1.10),   # MRAS, OR ≈ 1.10
    ("rs9982601", 1.10),   # SLC5A3 region, OR ≈ 1.10
    ("rs11556924", 1.10),  # ZC3HC1, OR ≈ 1.10
    ("rs3869109", 1.10),   # HLA-C region, OR ≈ 1.10
    ("rs11206510", 1.15),  # PCSK9, LDL-related, OR ≈ 1.15
    ("rs599839", 1.15),    # SORT1, LDL-related, OR ≈ 1.15
    ("rs17465637", 1.10),  # MIA3, OR ≈ 1.10
    ("rs3184504", 1.10),   # SH2B3, OR ≈ 1.10
]

TARGET_VARIANTS = TARGET_VARIANTS_ALZHEIMERS + TARGET_VARIANTS_SCHIZOPHRENIA + TARGET_VARIANTS_BREAST_CANCER + TARGET_VARIANTS_PROSTATE_CANCER + TARGET_VARIANTS_TYPE2_DIABETES + TARGET_VARIANTS_CORONARY_ARTERY_DISEASE


def make_record_map(vcf_path):
    """Create mapping from variant identifiers to genotype values."""
    record_map = {}
    vcf_reader = pysam.VariantFile(vcf_path)
    for record in vcf_reader.fetch():
        # Get genotype value (0=ref/ref, 1=ref/alt, 2=alt/alt)
        # Handle missing genotypes gracefully
        try:
            gt = record.samples[0]['GT']
            if None in gt:
                alt_count = 0  # Treat missing as reference
            else:
                alt_count = sum(gt)
        except (KeyError, IndexError):
            alt_count = 0
            
        # Map by rsID if available
        if record.id and record.id != '.':
            record_map[record.id] = alt_count
            
        # Map by chromosomal coordinates
        if record.alts:
            key = (str(record.chrom), record.pos, record.alts[0])
            record_map[key] = alt_count
            
    return record_map

def encode_on_variant_list(record_map: dict, filter_list: list):
    """Encode specific variants from the target list."""
    for pos_or_id in filter_list:
        if isinstance(pos_or_id, tuple):
            # Genomic coordinate specification
            key = (str(pos_or_id[0]), pos_or_id[1], pos_or_id[2])
        elif isinstance(pos_or_id, str):
            # rsID specification
            key = pos_or_id
        else:
            raise ValueError(f"Invalid variant specification: {pos_or_id}")
            
        # Return genotype count (0, 1, or 2) or 0 if variant not found
        yield record_map.get(key, 0)

def encode_vcf(vcf_path: str) -> List[int]:
    """
    Encode VCF genomic data to integer vectors suitable for FHE.
    
    Returns list of integers representing genotype counts for each target variant:
    - 0: homozygous reference (no risk alleles)
    - 1: heterozygous (one risk allele) 
    - 2: homozygous alternate (two risk alleles)
    
    For privacy-sensitive allele frequency analysis of Alzheimer's disease variants.
    """
    record_map = make_record_map(vcf_path)
    encoded_data = list(encode_on_variant_list(record_map, TARGET_VARIANTS))
    return encoded_data
