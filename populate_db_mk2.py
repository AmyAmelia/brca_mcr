from db.models import *
import pandas as pd

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
    # populate Variant
    existing, created = Variant.objects.get_or_create(cdna=df.iloc[i]['Variant cDNA'],
    protein=df.iloc[i]['Variant Protein'], genomic=df.iloc[i]['Variant Genome'])


for i in range(df.shape[0]):
    # populate Patient
    record = Patient.objects.create(name = df.iloc[i]['Name'],
                        age = df.iloc[i]['Age'],
                        id_stage = Stage.objects.filter(stage=df.iloc[i]['Stage'])[0],
                        id_description = Description.objects.filter(description=df.iloc[i]['Description'])[0],
                        id_platform = Platform.objects.filter(platform=df.iloc[i]['Sequencer'])[0],
                        id_variant = Variant.objects.filter(cdna=df.iloc[i]['Variant cDNA'], protein=df.iloc[i]['Variant Protein'], genomic=df.iloc[i]['Variant Genome'])[0],)
