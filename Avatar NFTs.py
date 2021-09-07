import pandas as pd;
import numpy.random as random;
random.seed(int("Digg".encode('utf-8').hex()))

def the_rareset():
    local_df = pd.DataFrame()
    jewel_type = {1:"Jade ", 2:"Diamond ", 3:"Diamond ", 4:"Diamond "}
    for key in jewel_type:
        nft = {}
        if (key==1):
            base = "Honey"
            row_index = base_Types.loc[(base_Types["Attributes"]==base),"Count"].index[0]
            nft["Base"] = base
            base_Types.loc[row_index,"Count"]+=1
        else:
            rnd_row = random.randint(len(base_Types))
            nft["Base"] = base_Types.iloc[rnd_row,0]
            base_Types.iloc[rnd_row,2]+=1
            
        
        row_index = head_Rares.loc[(head_Rares["Attributes"]=="Crown"),"Count"].index[0]
        nft ["Head"] = jewel_type[key] + "Crown"
        head_Rares.loc[row_index,"Count"]+=1
        if ((head_Rares.loc[row_index,"Count"]) == (head_Rares.loc[row_index,"Max"])):
            reached_Max.append(head_Rares.loc[row_index,"Attributes"])
            head_Rares.drop(row_index,inplace=True)
        rnd_row = random.randint(len(hair_Rares))
        nft["Hair"] = hair_Rares.iloc[rnd_row,0]
        hair_Rares.iloc[rnd_row,2]+=1
        nft.update({"Eye":"Digg","Ear":(jewel_type[key] + "Chandelier Earring")})
        eye_Rares.loc[(eye_Rares["Attributes"]=="Digg"),"Count"]+=1
        ear_Rares.loc[(ear_Rares["Attributes"]=="Chandelier Earring"),"Count"]+=1
        rnd_row = random.randint(len(face_Rares))
        nft["Face"] = face_Rares.iloc[rnd_row,0]
        face_Rares.iloc[rnd_row,2]+=1
        nft.update({"Neck":(jewel_type[key] + "Necklace")})
        neck_Rares.loc[(neck_Rares["Attributes"]=="Necklace"),"Count"]+=1
        local_df = local_df.append(nft, ignore_index=True)
    return(local_df)

def the_rare_jewelry(jewel_count):
    local_df = pd.DataFrame()
    attributes_Set = set()
    for jewel in jewel_count:
        j = 0
        while j < jewel_count[jewel]:
            nft = {}
            chosen_Att="fffffff"
            rnd_row = random.randint(len(base_Types))
            nft["Base"] = base_Types.iloc[rnd_row,0]
            base_Types.iloc[rnd_row,2]+=1
            chosen_Att=str(rnd_row)+chosen_Att[1:]
            
            two_jewel = random.choice(["Head","Ear","Neck"], 2, replace=False)
            if ("Head" in two_jewel):
                rnd_row = random.randint(len(head_Rares))
                nft["Head"] = jewel + head_Rares.iloc[rnd_row,0]
                head_Rares.iloc[rnd_row,2]+=1
                chosen_Att=chosen_Att[:1]+str(rnd_row)+chosen_Att[2:]
            if ("Ear" in two_jewel):
                rnd_row = random.randint(len(ear_Rares))
                nft["Ear"] = jewel + ear_Rares.iloc[rnd_row,0]
                ear_Rares.iloc[rnd_row,2]+=1
                chosen_Att=chosen_Att[:4]+str(rnd_row)+chosen_Att[5:]
            if ("Neck" in two_jewel):
                rnd_row = random.randint(len(neck_Rares))
                nft["Neck"] = jewel + neck_Rares.iloc[rnd_row,0]
                neck_Rares.iloc[rnd_row,2]+=1
                chosen_Att=chosen_Att[:6]+str(rnd_row)
                
            while(1):
                rnd_row = random.randint([len(hair_Rares),len(eye_Rares),len(face_Rares)])
                chosen_Att = chosen_Att[:2]+ str(rnd_row[0])+ str(rnd_row[1])+ chosen_Att[4:5]+ str(rnd_row[2])+ chosen_Att[6:]
                if ( not(chosen_Att in attributes_Set) ):
                    attributes_Set.add(chosen_Att)
                    break
                print("REPEAT!")
            
            nft["Hair"] = hair_Rares.iloc[rnd_row[0],0]
            hair_Rares.iloc[rnd_row[0],2]+=1
            
            nft["Eye"] = eye_Rares.iloc[rnd_row[1],0]
            eye_Rares.iloc[rnd_row[1],2]+=1
            
            nft["Face"] = face_Rares.iloc[rnd_row[2],0]
            face_Rares.iloc[rnd_row[2],2]+=1
            
            local_df = local_df.append(nft, ignore_index=True)
            
            j+=1
    
    return(local_df)

def zero_att_NFTs():
    local_df = pd.DataFrame()
    for base in base_Types["Attributes"]:
        nft = {"Base":base}
        local_df = local_df.append(nft, ignore_index=True)
    base_Types["Count"]+=1
    return(local_df)

def one_att_NFTs():
    local_df = pd.DataFrame()
    for att in aux_DB[aux_DB["Category"]!="Base"]["Attributes"]:
        nft = {}
        base_row = random.randint(len(base_Types))
        nft["Base"] = base_Types.iloc[base_row,0]
        base_Types.iloc[base_row,2]+=1
        check_Max(base_Types,base_row)
        nft[(aux_DB[aux_DB["Attributes"]==att]["Category"].iloc[0])]=att
        local_df = local_df.append(nft, ignore_index=True)
    head_Category["Count"]+=1
    hair_Category["Count"]+=1
    eye_Category["Count"]+=1
    ear_Category["Count"]+=1
    face_Category["Count"]+=1
    neck_Category["Count"]+=1
    return(local_df)

def five_atts_NFTs():#number_of):
    local_df = pd.DataFrame()
    #j=0
    #while (j<number_of):
    
    rep_Try=0
    max_Try=20
    while(1):
        chosen_Att=[-1,-1,-1,-1,-1]
        rnd_row = random.randint([(len(head_Category)+len(hair_Category)),len(eye_Category),len(ear_Category),len(face_Category),len(neck_Category)])
        chosen_Att = [rnd_row[0], rnd_row[1], rnd_row[2], rnd_row[3], rnd_row[4]]
        chosen_Att = tuple(chosen_Att)
        if ( not(chosen_Att in attributes_Setlist) ):
            attributes_Setlist.add(chosen_Att)
            break
        rep_Try+=1
        if (rep_Try==max_Try):
            print("Repeat in {}".format(5))
            return(local_df)
        
    nft={}
    base_row = random.randint(len(base_Types))
    nft["Base"] = base_Types.iloc[base_row,0]
    base_Types.iloc[base_row,2]+=1
    check_Max(base_Types,base_row)
    
    if (rnd_row[0]<len(head_Category)):
        nft["Head"] = head_Category.iloc[rnd_row[0],0]
        head_Category.iloc[rnd_row[0],2]+=1
        check_Max(head_Category,rnd_row[0])
    else:
        rnd_row[0] = rnd_row[0] - len(head_Category)
        nft["Hair"] = hair_Category.iloc[rnd_row[0],0]
        hair_Category.iloc[rnd_row[0],2]+=1
        check_Max(hair_Category,rnd_row[0])
        
    nft["Eye"]=eye_Category.iloc[rnd_row[1],0]
    eye_Category.iloc[rnd_row[1],2]+=1
    check_Max(eye_Category,rnd_row[1])
    
    nft["Ear"]=ear_Category.iloc[rnd_row[2],0]
    ear_Category.iloc[rnd_row[2],2]+=1
    check_Max(ear_Category,rnd_row[2])
    
    nft["Face"]=face_Category.iloc[rnd_row[3],0]
    face_Category.iloc[rnd_row[3],2]+=1
    check_Max(face_Category,rnd_row[3])
    
    nft["Neck"]=neck_Category.iloc[rnd_row[4],0]
    neck_Category.iloc[rnd_row[4],2]+=1
    check_Max(neck_Category,rnd_row[4])
    
    local_df = local_df.append(nft, ignore_index=True)
    #j+=1
    return(local_df)

def multi_atts_NFTs(n):
    local_df = pd.DataFrame()
    dict_Categories={0:"HH", 1:[eye_Category,"Eye"], 2:[ear_Category,"Ear"], 3:[face_Category,"Face"], 4:[neck_Category,"Neck"]}
    rep_Try = 0
    max_Try = 15
    k = 1
    flag = False
    while(1):
        res_Catch = random.choice(list(dict_Categories.keys()),n,replace=False)
        res_Catch.sort()
        if (k>1):
            while((res_Catch==rnd_ch).all()):
                res_Catch = random.choice(list(dict_Categories.keys()),n,replace=False)
                res_Catch.sort()
        rnd_ch = res_Catch
        list_ch=[]
        if (rnd_ch[0]==0):
            list_ch.append(len(head_Category)+len(hair_Category))
            j=1
        else:
            j=0
        while (j<n):
            list_ch.append(len(dict_Categories[rnd_ch[j]][0]))
            j+=1
        while(rep_Try<(k*max_Try)):
            chosen_Att=[-1,-1,-1,-1,-1]
            res_row=random.randint(list_ch)
            if (not(rep_Try==(k-1)*max_Try)):
                while((res_row==rnd_row).all()):
                    res_row=random.randint(list_ch)
            rnd_row= res_row
            j=0
            while(j<n):
                chosen_Att[rnd_ch[j]]=rnd_row[j]
                j+=1
            chosen_Att=tuple(chosen_Att)
            if ( not(chosen_Att in attributes_Setlist) ):
                attributes_Setlist.add(chosen_Att)
                flag=True
                break
            rep_Try+=1
        if (flag):
            break
        if (rep_Try==4*max_Try):
            #print("Crush in {}".format(n))
            return(local_df)
        k+=1
    
    nft={}
    base_row = random.randint(len(base_Types))
    nft["Base"] = base_Types.iloc[base_row,0]
    base_Types.iloc[base_row,2]+=1
    check_Max(base_Types,base_row)
    
    if(rnd_ch[0]==0):
        j=1
        if (rnd_row[0]<len(head_Category)):
            nft["Head"] = head_Category.iloc[rnd_row[0],0]
            head_Category.iloc[rnd_row[0],2]+=1
            check_Max(head_Category,rnd_row[0])
        else:
            rnd_row[0] = rnd_row[0] - len(head_Category)
            nft["Hair"] = hair_Category.iloc[rnd_row[0],0]
            hair_Category.iloc[rnd_row[0],2]+=1
            check_Max(hair_Category,rnd_row[0])
    else:
        j=0
    
    while(j<n):
        nft[dict_Categories[rnd_ch[j]][1]] = (dict_Categories[rnd_ch[j]][0]).iloc[rnd_row[j],0]
        dict_Categories[rnd_ch[j]][0].iloc[rnd_row[j],2]+=1
        check_Max(dict_Categories[rnd_ch[j]][0],rnd_row[j])
        j+=1
        
    local_df = local_df.append(nft, ignore_index=True)
    return(local_df)

def remaining_two_atts_NFTs():
    local_df = pd.DataFrame()
    dict_Categories={0:"HH", 1:[eye_Category,"Eye"], 2:[ear_Category,"Ear"], 3:[face_Category,"Face"], 4:[neck_Category,"Neck"]}
    for category_Number in dict_Categories:
        if(category_Number==0):
            j=0
            while (j<(len(head_Category)+len(hair_Category))):
                i=category_Number+1
                while(i<5):
                    k=0
                    while(k<len(dict_Categories[i][0])):
                        chosen_Att=[-1,-1,-1,-1,-1]
                        chosen_Att[category_Number]=j
                        chosen_Att[i]=k
                        chosen_Att=tuple(chosen_Att)
                        if (not(chosen_Att in attributes_Setlist)):
                            attributes_Setlist.add(chosen_Att)
                            nft={}
                            if (j<len(head_Category)):
                                nft["Head"]=head_Category.iloc[j,0]
                                head_Category.iloc[j,2]+=1
                                check_Max(head_Category,j)
                            else:
                                nft["Hair"]=hair_Category.iloc[j-len(head_Category),0]
                                hair_Category.iloc[j-len(head_Category),2]+=1
                                check_Max(hair_Category,j-len(head_Category))
                            nft[dict_Categories[i][1]]=dict_Categories[i][0].iloc[k,0]
                            dict_Categories[i][0].iloc[k,2]+=1
                            check_Max(dict_Categories[i][0],k)
                            base_row = random.randint(len(base_Types))
                            nft["Base"] = base_Types.iloc[base_row,0]
                            base_Types.iloc[base_row,2]+=1
                            check_Max(base_Types,base_row)
                            local_df = local_df.append(nft, ignore_index=True)
                        k+=1
                    i+=1
                j+=1
        else:
            j=0
            while(j<len(dict_Categories[category_Number][0])):
                i=category_Number+1
                while(i<5):
                    k=0
                    while(k<len(dict_Categories[i][0])):
                        chosen_Att=[-1,-1,-1,-1,-1]
                        chosen_Att[category_Number]=j
                        chosen_Att[i]=k
                        chosen_Att=tuple(chosen_Att)
                        if (not(chosen_Att in attributes_Setlist)):
                            attributes_Setlist.add(chosen_Att)
                            nft={}
                            nft[dict_Categories[category_Number][1]]=dict_Categories[category_Number][0].iloc[j,0]
                            dict_Categories[category_Number][0].iloc[j,2]+=1
                            check_Max(dict_Categories[category_Number][0],j)
                            nft[dict_Categories[i][1]]=dict_Categories[i][0].iloc[k,0]
                            dict_Categories[i][0].iloc[k,2]+=1
                            check_Max(dict_Categories[i][0],k)
                            base_row = random.randint(len(base_Types))
                            nft["Base"] = base_Types.iloc[base_row,0]
                            base_Types.iloc[base_row,2]+=1
                            check_Max(base_Types,base_row)
                            local_df = local_df.append(nft, ignore_index=True)
                        k+=1
                    i+=1
                j+=1
    return(local_df)

def check_Max(category_Dataframe, row_Number):
    if ((category_Dataframe.iloc[row_Number]["Count"]) == (category_Dataframe.iloc[row_Number]["Max"])):
        reached_Max.append(category_Dataframe.iloc[row_Number]["Attributes"])
        category_Dataframe.drop(category_Dataframe.index[row_Number],inplace=True)

def fill_database_reachedMax():
    for att_Max in reached_Max:
        database_all.loc[(database_all["Attributes"]==att_Max), "Count"] = database_all.loc[(database_all["Attributes"]==att_Max), "Max"]

df = pd.DataFrame(columns=["Base","Head","Hair","Eye","Ear","Face","Neck"])
database_all = pd.read_excel("Attributes.xlsx","Attributes",dtype={"Count":int,"Max":int})

reached_Max = []
base_Types = database_all[database_all["Category"]=="Base"].copy()
head_Rares = database_all[(database_all["Category"]=="Head") & (database_all["Rarity"]=="Rare")].copy()
hair_Rares = database_all[(database_all["Category"]=="Hair") & (database_all["Rarity"]=="Rare")].copy()
eye_Rares = database_all[(database_all["Category"]=="Eye") & (database_all["Rarity"]=="Rare")].copy()
ear_Rares = database_all[(database_all["Category"]=="Ear") & (database_all["Rarity"]=="Rare")].copy()
face_Rares = database_all[(database_all["Category"]=="Face") & (database_all["Rarity"]=="Rare")].copy()
neck_Rares = database_all[(database_all["Category"]=="Neck") & (database_all["Rarity"]=="Rare")].copy()

df = df.append(the_rareset(),ignore_index=True)
df = df.append(the_rare_jewelry({"Diamond ":17}),ignore_index=True)
fill_database_reachedMax()
database_all= pd.concat([database_all,head_Rares]).drop_duplicates(["Attributes"],keep="last").sort_index()
database_all= pd.concat([database_all,hair_Rares]).drop_duplicates(["Attributes"],keep="last").sort_index()
database_all= pd.concat([database_all,eye_Rares]).drop_duplicates(["Attributes"],keep="last").sort_index()
database_all= pd.concat([database_all,ear_Rares]).drop_duplicates(["Attributes"],keep="last").sort_index()
database_all= pd.concat([database_all,face_Rares]).drop_duplicates(["Attributes"],keep="last").sort_index()
database_all= pd.concat([database_all,neck_Rares]).drop_duplicates(["Attributes"],keep="last").sort_index()

reached_Max = []
aux_DB = database_all[database_all["Count"]<database_all["Max"]].copy()
head_Category = aux_DB[(aux_DB["Category"]=="Head")].copy()
hair_Category = aux_DB[(aux_DB["Category"]=="Hair")].copy()
eye_Category = aux_DB[(aux_DB["Category"]=="Eye")].copy()
ear_Category = aux_DB[(aux_DB["Category"]=="Ear")].copy()
face_Category = aux_DB[(aux_DB["Category"]=="Face")].copy()
neck_Category = aux_DB[(aux_DB["Category"]=="Neck")].copy()

df = df.append(zero_att_NFTs(),ignore_index=True)
df = df.append(one_att_NFTs(),ignore_index=True)

nft_Total = 21000
designed_Series = 0
max_five_Atts = int((13.6/100)*21000)
max_two_Atts = 1389
max_four_Atts = int((34.1/100)*21000)
max_three_Atts = nft_Total - 5 - 62 - 21 - designed_Series - max_five_Atts - max_four_Atts - max_two_Atts
count_Atts = [0,0,0,0]
max_Atts=[max_two_Atts,max_three_Atts,max_four_Atts,max_five_Atts]
attributes_Setlist = set()
att_Number_list = [2,3,4,5]
while(len(att_Number_list)>0):
    chosen_Number = random.choice(att_Number_list)
    if (chosen_Number==5):
        res_df=five_atts_NFTs()
    else:
        res_df=multi_atts_NFTs(chosen_Number)
    df = df.append(res_df,ignore_index=True)
    count_Atts[chosen_Number-2]+=1
    if (count_Atts[chosen_Number-2]==max_Atts[chosen_Number-2]):
        att_Number_list.remove(chosen_Number)

df = df.append(remaining_two_atts_NFTs(),ignore_index=True)

remaining = nft_Total - len(df)
for i in range(remaining):
    df = df.append(multi_atts_NFTs(3),ignore_index=True)

remaining = nft_Total - len(df)
for i in range(remaining):
    df = df.append(multi_atts_NFTs(4),ignore_index=True)

fill_database_reachedMax()
database_all= pd.concat([database_all,head_Category]).drop_duplicates(["Attributes"],keep="last").sort_index()
database_all= pd.concat([database_all,hair_Category]).drop_duplicates(["Attributes"],keep="last").sort_index()
database_all= pd.concat([database_all,eye_Category]).drop_duplicates(["Attributes"],keep="last").sort_index()
database_all= pd.concat([database_all,ear_Category]).drop_duplicates(["Attributes"],keep="last").sort_index()
database_all= pd.concat([database_all,face_Category]).drop_duplicates(["Attributes"],keep="last").sort_index()
database_all= pd.concat([database_all,neck_Category]).drop_duplicates(["Attributes"],keep="last").sort_index()

(database_all.drop("Rarity",axis=1)).to_excel("All-Attributes-Count.xlsx")

(df.fillna("---")).to_excel("NFTs.xlsx")