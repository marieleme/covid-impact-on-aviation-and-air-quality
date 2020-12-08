import pandas as pd

months=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

LFPG_df = pd.DataFrame(columns = ['origin', 'destination', 'total'], index=months)
EGLL_df = pd.DataFrame(columns = ['origin', 'destination', 'total'], index=months)
EHAM_df = pd.DataFrame(columns = ['origin', 'destination', 'total'], index=months)
KATL_df = pd.DataFrame(columns = ['origin', 'destination', 'total'], index=months)
KORD_df = pd.DataFrame(columns = ['origin', 'destination', 'total'], index=months)
KLAX_df = pd.DataFrame(columns = ['origin', 'destination', 'total'], index=months)
OMAA_df = pd.DataFrame(columns = ['origin', 'destination', 'total'], index=months)
RJTT_df = pd.DataFrame(columns = ['origin', 'destination', 'total'], index=months)
VHHH_df = pd.DataFrame(columns = ['origin', 'destination', 'total'], index=months)

def read_csv(filename, month):
    df = pd.read_csv(filename, usecols=['origin', 'destination'])

    LFPG_dic = {'origin': 0, 'destination': 0}
    EGLL_dic = {'origin': 0, 'destination': 0}
    EHAM_dic = {'origin': 0, 'destination': 0}
    KATL_dic = {'origin': 0, 'destination': 0}
    KORD_dic = {'origin': 0, 'destination': 0}
    KLAX_dic = {'origin': 0, 'destination': 0}
    OMAA_dic = {'origin': 0, 'destination': 0}
    RJTT_dic = {'origin': 0, 'destination': 0}
    VHHH_dic = {'origin': 0, 'destination': 0}

    for (columnName, columnData) in df.iteritems():
        for i in columnData.values:
            if i == "LFPG":
                LFPG_dic[columnName] += 1
            elif i == "EGLL":
                EGLL_dic[columnName] += 1
            elif i == "EHAM":
                EHAM_dic[columnName] += 1
            elif i == "KATL":
                KATL_dic[columnName] += 1
            elif i == "KORD":
                KORD_dic[columnName] += 1
            elif i == "KLAX":
                KLAX_dic[columnName] += 1
            elif i == "OMAA":
                OMAA_dic[columnName] += 1
            elif i == "RJTT":
                RJTT_dic[columnName] += 1
            elif i == "VHHH":
                VHHH_dic[columnName] += 1

    
    LFPG_df.loc[month]['origin'] = LFPG_dic['origin']  
    EGLL_df.loc[month]['origin'] = EGLL_dic['origin']  
    EHAM_df.loc[month]['origin'] = EHAM_dic['origin']  
    KATL_df.loc[month]['origin'] = KATL_dic['origin']  
    KORD_df.loc[month]['origin'] = KORD_dic['origin']  
    KLAX_df.loc[month]['origin'] = KLAX_dic['origin']  
    OMAA_df.loc[month]['origin'] = OMAA_dic['origin']  
    RJTT_df.loc[month]['origin'] = RJTT_dic['origin']  
    VHHH_df.loc[month]['origin'] = VHHH_dic['origin']  
    
    LFPG_df.loc[month]['destination'] = LFPG_dic['destination']  
    EGLL_df.loc[month]['destination'] = EGLL_dic['destination']  
    EHAM_df.loc[month]['destination'] = EHAM_dic['destination']  
    KATL_df.loc[month]['destination'] = KATL_dic['destination']  
    KORD_df.loc[month]['destination'] = KORD_dic['destination']  
    KLAX_df.loc[month]['destination'] = KLAX_dic['destination']  
    OMAA_df.loc[month]['destination'] = OMAA_dic['destination']  
    RJTT_df.loc[month]['destination'] = RJTT_dic['destination']  
    VHHH_df.loc[month]['destination'] = VHHH_dic['destination'] 

    LFPG_df.loc[month]['total'] = LFPG_dic['destination'] + LFPG_dic['origin']
    EGLL_df.loc[month]['total'] = EGLL_dic['destination'] + EGLL_dic['origin']
    EHAM_df.loc[month]['total'] = EHAM_dic['destination'] + EHAM_dic['origin']
    KATL_df.loc[month]['total'] = KATL_dic['destination'] + KATL_dic['origin'] 
    KORD_df.loc[month]['total'] = KORD_dic['destination'] + KORD_dic['origin']
    KLAX_df.loc[month]['total'] = KLAX_dic['destination'] + KLAX_dic['origin'] 
    OMAA_df.loc[month]['total'] = OMAA_dic['destination'] + OMAA_dic['origin'] 
    RJTT_df.loc[month]['total'] = RJTT_dic['destination'] + RJTT_dic['origin'] 
    VHHH_df.loc[month]['total'] = VHHH_dic['destination'] + VHHH_dic['origin'] 
     

def convert_to_csv(year):
    LFPG_df.to_csv("simpleData/LFPG" + "_" + year)
    EGLL_df.to_csv("simpleData/EGLL" + "_" + year)
    EHAM_df.to_csv("simpleData/EHAM" + "_" + year)
    KATL_df.to_csv("simpleData/KATL" + "_" + year) 
    KORD_df.to_csv("simpleData/KORD" + "_" + year)
    KLAX_df.to_csv("simpleData/KLAX" + "_" + year) 
    OMAA_df.to_csv("simpleData/OMAA" + "_" + year) 
    RJTT_df.to_csv("simpleData/RJTT" + "_" + year) 
    VHHH_df.to_csv("simpleData/VHHH" + "_" + year) 


def main():
    read_csv("dataset_flights/flightlist_20190101_20190131.csv","Jan")
    read_csv("dataset_flights/flightlist_20190201_20190228.csv","Feb")
    read_csv("dataset_flights/flightlist_20190301_20190331.csv","Mar")
    read_csv("dataset_flights/flightlist_20190401_20190430.csv","Apr")
    read_csv("dataset_flights/flightlist_20190501_20190531.csv","May")
    read_csv("dataset_flights/flightlist_20190601_20190630.csv","Jun")
    read_csv("dataset_flights/flightlist_20190701_20190731.csv","Jul")
    read_csv("dataset_flights/flightlist_20190801_20190831.csv","Aug")
    read_csv("dataset_flights/flightlist_20190901_20190930.csv","Sep")
    read_csv("dataset_flights/flightlist_20191001_20191031.csv","Oct")
    read_csv("dataset_flights/flightlist_20191101_20191130.csv","Nov")
    read_csv("dataset_flights/flightlist_20191201_20191231.csv","Dec")

    convert_to_csv("2019")


if __name__ == "__main__":
    main()