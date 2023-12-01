import os
import pandas as pd

main_df = pd.DataFrame()

for json_file in os.listdir('JSON_FILES') :
    print(json_file)
    df = pd.read_json('JSON_FILES/'+json_file)
    for inx in df.index :
        attribute_json = df.iloc[inx].attributes
        df[attribute_json.get('trait_type')] = attribute_json.get('value')
    df.drop_duplicates(['dna'],inplace=True)
    df.drop(columns=['attributes'],inplace=True)
    df['file_name'] = json_file
    main_df = pd.concat([main_df,df],axis=0)

main_df.to_csv('all_flatten.csv',index=False)
main_df.to_excel('all_flatten.xlsx',index=False)