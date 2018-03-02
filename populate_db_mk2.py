from db.models import *
import pandas as pd
import myvariant

df = pd.read_csv('BRCA1_test_set_crop.txt', sep='\t', header=0)
# loop through df of records and assign keys
for i in range(df.shape[0]):
    # populate Sequencer/Platform
    existing, created = Platform.objects.get_or_create(platform=df.iloc[i]['Sequencer'])

d_stage = {1:'one', 2:'two', 3:'three'}
for i in range(df.shape[0]):
    # populate Stage
    existing, created = Stage.objects.get_or_create(stage=df.iloc[i]['Stage'], stage_str=d_stage[df.iloc[i]['Stage']])

for i in range(df.shape[0]):
    # populate Description
    existing, created = Description.objects.get_or_create(description=df.iloc[i]['Description'])

for i in range(df.shape[0]):
    # populate and annotate Variant 
    mv = myvariant.MyVariantInfo()
    var_ann = mv.getvariant('chr17:' + (df.iloc[i]['Variant Genome']), ['dbsnp.rsid', 'cadd.polyphen.cat', 'cadd.sift.cat', 'gnomad_exome.af.af'])
    if var_ann is None:
        rsID_ann= "N/A"
        polyphen_ann = "N/A" 
        sift_ann= "N/A"
        gnomad_ann = "N/A"
    else:
        # check if variant has a dbSNP iD
        if 'dbsnp' in var_ann:
            rsID_ann = var_ann['dbsnp']['rsid']  
        else:
            rsID_ann = "N/A"
        # check if variant has a Polyphen score and Sift score. 
        if 'cadd' in var_ann:
            polyphen_ann = var_ann['cadd']['polyphen']['cat']
            sift_ann=   polyphen_ann = var_ann['cadd']['sift']['cat']  
        else:
            polyphen_ann = "N/A"
            sift_ann = "N/A"
        # check if variant has a gnomad MAF. 
        if 'gnomad_exome' in var_ann:
            gnomad_ann = var_ann['gnomad_exome']['af']['af']
        else:
            gnomad_ann = "N/A"
    # Populate dv 
    existing, created = Variant.objects.get_or_create(cdna=df.iloc[i]['Variant cDNA'],
    protein=df.iloc[i]['Variant Protein'], genomic=df.iloc[i]['Variant Genome'],rsid = rsID_ann, polyphen = polyphen_ann, sift = sift_ann, gnomad_af = gnomad_ann)

for i in range(df.shape[0]):
    # populate Patient
    record = Patient.objects.create(name = df.iloc[i]['Name'],
                        age = df.iloc[i]['Age'],
                        id_stage = Stage.objects.filter(stage=df.iloc[i]['Stage'])[0],
                        id_description = Description.objects.filter(description=df.iloc[i]['Description'])[0],
                        id_platform = Platform.objects.filter(platform=df.iloc[i]['Sequencer'])[0],
                        id_variant = Variant.objects.filter(cdna=df.iloc[i]['Variant cDNA'], protein=df.iloc[i]['Variant Protein'], genomic=df.iloc[i]['Variant Genome'])[0],)
