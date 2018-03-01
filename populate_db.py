from db.models import *
import pandas as pd

df = pd.read_csv('BRCA1_test_set_crop.txt', sep='\t', header=0)

for i in range(df.shape[0]):
    existing, created = Platform.objects.get_or_create(platform=df.iloc[i]['Sequencer'])
    if created == True:
        platform_id = Platform.objects.latest('id_platform')
        print('new', platform_id)
    else:
        platform_id = existing.id_platform
        print('old', platform_id)

for i in range(df.shape[0]):
    existing, created = Stage.objects.get_or_create(stage=df.iloc[i]['Stage'])
    if created == True:
        stage_id = Stage.objects.latest('id_stage')
        print('new', stage_id)
    else:
        stage_id = existing.id_stage
        print('old', stage_id)

for i in range(df.shape[0]):
    existing, created = Description.objects.get_or_create(description=df.iloc[i]['Description'])
    if created == True:
        description_id = Description.objects.latest('id_description')
        print('new', description_id)
    else:
        description_id = existing.id_description
        print('old', description_id)

for i in range(df.shape[0]):
    existing, created = Variant.objects.get_or_create(cdna=df.iloc[i]['Variant cDNA'],
    protein=df.iloc[i]['Variant Protein'], genomic=df.iloc[i]['Variant Genome'])
    if created == True:
        variant_id = Variant.objects.latest('id_variant')
        print('new', variant_id)
    else:
        variant_id = existing.id_variant
        print('old', variant_id)






for i in range(df.shape[0]):
    existing, created = Variant.objects.get_or_create(cdna=df.iloc[i]['Variant cDNA'],
    protein=df.iloc[i]['Variant Protein'], genomic=df.iloc[i]['Variant Genome'])
    if created == True:
        print(created)
