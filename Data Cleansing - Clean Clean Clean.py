#This Cleans the data further to just get the Image Name and not the entire regex match. Outputs a 90% Webscrape results. Only information missing is main body text
import pandas as pd

# Load the CSV file
file_path = r'C:\Users\Admin\Documents\Self learn\Data Analytics\Data Analytics Client 3\Clean Clean Clean.csv'
dfs = pd.read_csv(file_path)

regex_matches = dfs['IMAGE'].astype(str).tolist()

# Split each string at 'csm_' and keep the right side
clean_image_names = []
for match in regex_matches:
    clean_name = match.split('csm_')[-1] # Keep the right side of the split
    for ext in ['.jpg', '.jpeg', '.png', '.gif']:
        if ext in clean_name:
            clean_name = clean_name.split(ext)[0] # Keep the left side of the split
            clean_name += ext # Add the file extension back
            break
    clean_image_names.append(clean_name)

df_clean_names = pd.DataFrame(clean_image_names, columns=["IMAGE FILE"])
df = dfs.drop(labels='IMAGE', axis=1)
df.rename(columns={'ARTICLE TITLE':'TITLE', 'PAGENUMBER':'PAGE#'}, inplace=True)
df = pd.concat([df,df_clean_names], axis=1)

#print(df)
df.to_excel(r'C:\Users\Admin\Documents\Self learn\Data Analytics\Data Analytics Client 3\Webscrape Clean (Webscrape Clean (Article, Page, Title, URL, Image Used).xlsx', index=False)

