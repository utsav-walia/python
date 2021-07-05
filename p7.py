print(df[df.PTS>20])
print(df.groupby('Tm').get_group)
print(df.groupby('Pos').PTS.describe())
positions = ['C','PF','SF','PG','']

PTS['PTS'].hist(by=PTS)['Pos'], layout = (1,5), figsize = (16,2)



g = sns.FaceGrid(PTS, col = "Pos")
print(g)
