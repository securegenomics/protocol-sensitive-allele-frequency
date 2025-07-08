# Reference for PRS models -> https://chatgpt.com/s/dr_686c84c4b4b48191b3c779a6393f15f0

# These are the most clinically significant and population-variable SNPs for AD research
TARGET_VARIANTS_ALZHEIMERS = [
    ("rs429358", 12.0),    # APOE ε4 homozygotes (late-onset AD OR ≈12:contentReference[oaicite:6]{index=6})
    ("rs7412", 0.62),      # APOE ε2 allele (protective; OR≈0.62, 38% reduced risk:contentReference[oaicite:7]{index=7})
    ("rs2075650", 4.18),   # TOMM40 (tags APOE ε4); risk allele OR≈4.18:contentReference[oaicite:8]{index=8}
    ("rs199768005", 0.10), # Rare APOE (p.V236E) variant; OR≈0.10 (highly protective):contentReference[oaicite:9]{index=9}
    ("rs6857", 1.27),      # NECTIN2 (APOE locus) variant; risk allele OR≈1.27
    ("rs11136000", 1.19),  # CLU variant; OR≈1.19
    ("rs3851179", 1.18),   # PICALM variant; OR≈1.18
    ("rs6733839", 1.22),   # BIN1 variant; OR≈1.22
    ("rs6656401", 1.18),   # CR1 variant; OR≈1.18
    ("rs3764650", 1.23),   # ABCA7 variant; OR≈1.23
]

TARGET_VARIANTS_SCHIZOPHRENIA = [
    ("rs1344706", 1.12),  # ZNF804A risk allele (meta-analysis OR≈1.12):contentReference[oaicite:13]{index=13} 
    ("rs13194053", 1.10), # MHC/HLA region SNP (small effect, OR≈1.10)
    ("rs1006737", 1.15),  # CACNA1C SNP (common risk, OR≈1.15)
    ("rs10994336", 1.10), # ANK3 SNP (OR≈1.10)
    ("rs6994992", 1.10),  # NRG1 promoter SNP (OR≈1.10)
    ("rs13242038", 1.10), # GRM3 variant (OR≈1.10)
    ("rs4570625", 1.10),  # TPH2 variant (OR≈1.10)
    ("rs4680",    1.15),  # COMT Val158Met (risk allele OR≈1.15)
    ("rs6265",    1.15),  # BDNF Val66Met (risk allele OR≈1.15)
    ("rs1800497", 1.10),  # DRD2 Taq1A (OR≈1.10)
]


TARGET_VARIANTS_BREAST_CANCER = [
    ("rs2981579", 1.27),   # FGFR2 proxy SNP; OR≈1.27:contentReference[oaicite:20]{index=20}
    ("rs3803662", 1.28),   # TOX3 SNP; OR≈1.28
    ("rs1045485", 1.10),   # CASP8 variant; OR≈1.10
    ("rs2981582", 1.26),   # FGFR2 intron 2; OR≈1.26:contentReference[oaicite:21]{index=21}
    ("rs1801516", 1.10),   # ATM missense; OR≈1.10
    ("rs17879961", 1.50),  # CHEK2 I157T; OR≈1.50
    ("rs11515",    1.10),  # CDKN2A promoter SNP; OR≈1.10
    ("rs25487",    1.10),  # XRCC1 Arg399Gln; OR≈1.10
    ("rs80357713", 5.00),  # BRCA1 truncating (185delAG); OR large (~5+)
    ("rs11571833", 1.53),  # BRCA2 K3326*; OR≈1.53:contentReference[oaicite:22]{index=22}
    ("rs180177102", 3.00), # PALB2 truncating; OR≈3.0
    ("rs555607708", 2.34), # CHEK2 1100delC; OR≈2.34:contentReference[oaicite:23]{index=23}
]

TARGET_VARIANTS_PROSTATE_CANCER = [
    ("rs10993994", 1.24),  # MSMB promoter T allele; OR≈1.24:contentReference[oaicite:25]{index=25}
    ("rs10896449", 1.10),  # Chr11q13 variant; OR≈1.10
    ("rs4245739", 1.12),   # MDM4 3'UTR variant; OR≈1.12
    ("rs16901979", 1.44),  # 8q24.21 variant (region 2, E. Asian); OR≈1.44
    ("rs1447295", 1.20),   # 8q24.21 variant (region 1); OR≈1.20
    ("rs10086908", 1.10),  # 8q24.21 variant (region 5); OR≈1.10
    ("rs1512268", 1.10),   # 8p21 region; OR≈1.10
]

TARGET_VARIANTS_TYPE2_DIABETES = [
    ("rs7903146", 1.40),   # TCF7L2 T allele; OR≈1.37–1.45:contentReference[oaicite:27]{index=27}
    ("rs13266634", 1.15),  # SLC30A8 (ZnT8) R325W; OR≈1.15
    ("rs1801282", 1.14),   # PPARG Pro12Ala (G allele); OR≈1.14 (A is protective)
    ("rs10923931", 1.12),  # IGF2BP2 variant; OR≈1.12
    ("rs4402960", 1.12),   # IGF2BP2 (alternate SNP); OR≈1.12
    ("rs5215",    1.10),   # KCNJ11 E23K (G allele); OR≈1.10
]

TARGET_VARIANTS_CORONARY_ARTERY_DISEASE = [
    ("rs1333049", 1.47),   # Chr9p21 C allele; OR≈1.47 (het) up to ~1.9 (hom) 
    ("rs662799",  1.15),   # APOA5 variant; OR≈1.15
    ("rs6922269", 1.10),   # MTHFD1L SNP; OR≈1.10
    ("rs2943634", 1.10),   # Intergenic 2q36.3; OR≈1.10
    ("rs501120",  1.10),   # CXCL12 locus; OR≈1.10
    ("rs17228212",1.10),   # SMAD3 SNP; OR≈1.10
    ("rs9818870", 1.10),   # MRAS SNP; OR≈1.10
    ("rs9982601", 1.10),   # SLC5A3 region; OR≈1.10
    ("rs11556924",1.10),   # ZC3HC1 (NIPA) SNP; OR≈1.10
    ("rs3869109", 1.10),   # HLA-C region; OR≈1.10
    ("rs11206510",1.15),   # PCSK9 SNP; OR≈1.15
    ("rs599839", 1.15),    # SORT1 (1p13) SNP; OR≈1.15
    ("rs17465637",1.10),   # MIA3 SNP; OR≈1.10
    ("rs3184504",1.10),    # SH2B3 (LNK) R262W; OR≈1.10
]

TARGET_VARIANTS = TARGET_VARIANTS_ALZHEIMERS + TARGET_VARIANTS_SCHIZOPHRENIA + TARGET_VARIANTS_BREAST_CANCER + TARGET_VARIANTS_PROSTATE_CANCER + TARGET_VARIANTS_TYPE2_DIABETES + TARGET_VARIANTS_CORONARY_ARTERY_DISEASE
