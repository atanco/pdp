import pandas as pd


a=[]
i=0
for i in range(21):
    a.append(i*5)

print(a)

weights=[]

for i in a:
    for j in a:
        for z in a:
            for k in a:
                for l in a:
                    if i+j+z+k+l==100:
                        weights.append([i,j,z,k,l])

print(weights[0])
print(len(weights))
df=pd.DataFrame(columns=['ST','CB', 'PB','GO','CA'])
for row in weights:
    df.loc[len(df)]=row

print(df)
df.to_csv("portfolio_allocations")