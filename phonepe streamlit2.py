import streamlit as st
from streamlit.components.v1 import html
from streamlit_option_menu import option_menu
import requests
import json
import os
import pandas as pd
import plotly.express as px
import streamlit as st
import plotly.graph_objects as go
import numpy as np

st.set_page_config(layout="wide")

st.header("Phonepe Pulse  |   The Beat of Progress")
path="C:/GUVI FOLDER/phonepe pulse visualization/data/aggregated/transaction/country/india/state/"
Agg_state_list=os.listdir(path)



#aggregated transaction dataframe

agg_tran={"State":[], "Years":[], "Quarters":[], "Transaction_type":[], "Transaction_count":[], "Transaction_amount":[]}

for state in Agg_state_list:
    pstate=path+state+"/"
    Agg_yr=os.listdir(pstate)
    for year in Agg_yr:
        pyear=pstate+year+"/"
        Agg_qtr_list=os.listdir(pyear)
        for quarter in Agg_qtr_list:
            pquarter=pyear+quarter
            data=open(pquarter,"r")
            file=json.load(data)
            for item in file['data']['transactionData']:
                Name=item['name']
                count=item['paymentInstruments'][0]['count']
                amount=item['paymentInstruments'][0]['amount']
                agg_tran['Transaction_type'].append(Name)
                agg_tran['Transaction_count'].append(int(count))
                agg_tran['Transaction_amount'].append(int((amount)))
                #agg_tran['Transaction_amount'].append(float(amount))
                agg_tran['State'].append(state)
                agg_tran['Years'].append(year)
                agg_tran['Quarters'].append(int(quarter.strip('.json')))

agg_tran_table=pd.DataFrame(agg_tran)
agg_tran_table.index=agg_tran_table.index+1

agg_tran_table['State']=agg_tran_table['State'].replace('andaman-&-nicobar-islands', 'Andaman & Nicobar')
agg_tran_table['State']=agg_tran_table['State'].str.replace('Dadra & Nagar Haveli & Daman & Diu', 'Dadra and Nagar Haveli and Daman and Diu')
agg_tran_table['State']=agg_tran_table['State'].str.replace('-', ' ')
agg_tran_table['State']=agg_tran_table['State'].str.title()


#map transaction dataframe

path="C:/GUVI FOLDER/phonepe pulse visualization/data/map/transaction/hover/country/india/state/"
Agg_state_list=os.listdir(path)

map_tran={"State":[], "Years":[], "Quarters":[], "District":[], "Transaction_count":[], "Transaction_amount":[]}

for state in Agg_state_list:
    pstate=path+state+"/"
    Agg_yr=os.listdir(pstate)
    for year in Agg_yr:
        pyear=pstate+year+"/"
        Agg_qtr_list=os.listdir(pyear)
        for quarter in Agg_qtr_list:
            pquarter=pyear+quarter
            data=open(pquarter,"r")
            file=json.load(data)
            for item in file['data']['hoverDataList']:
                Name=item['name']
                count=item['metric'][0]['count']
                amount=item['metric'][0]['amount']
                map_tran['District'].append(Name)
                map_tran['Transaction_count'].append(count)
                map_tran['Transaction_amount'].append(int(amount))
                map_tran['State'].append(state)
                map_tran['Years'].append(year)
                map_tran['Quarters'].append(int(quarter.strip('.json')))

map_tran_table=pd.DataFrame(map_tran)
map_tran_table.index=map_tran_table.index+1

map_tran_table['State']=map_tran_table['State'].replace('andaman-&-nicobar-islands', 'Andaman & Nicobar')
map_tran_table['State']=map_tran_table['State'].str.replace('Dadra & Nagar Haveli & Daman & Diu', 'Dadra and Nagar Haveli and Daman and Diu')
map_tran_table['District']=map_tran_table['District'].str.replace('district', '')
map_tran_table['State']=map_tran_table['State'].str.replace('-', ' ')
map_tran_table['State']=map_tran_table['State'].str.title()

#map user dataframe
path="C:/GUVI FOLDER/phonepe pulse visualization/data/map/user/hover/country/india/state/"
Agg_state_list=os.listdir(path)
#Agg_state_list

map_user={'State':[], 'Years':[],'Quarters':[], 'District':[], 'Registered_users':[], 'App_opens':[]}

for state in Agg_state_list:
    pstate=path+state+"/"
    Agg_yr=os.listdir(pstate)
    for year in Agg_yr:
        pyear=pstate+year+"/"
        Agg_qtr_list=os.listdir(pyear)
        for quarter in Agg_qtr_list:
            pquarter=pyear+quarter
            data=open(pquarter,"r")
            file=json.load(data)

            for item in file['data']['hoverData'].items():
                district=item[0]
                registeredUsers=item[1]['registeredUsers']
                appOpens=item[1]['appOpens']
                map_user['State'].append(state)
                map_user['Registered_users'].append(registeredUsers)
                map_user['App_opens'].append(appOpens)
                map_user['District'].append(district)
                map_user['Years'].append(year)
                map_user['Quarters'].append(int(quarter.strip('.json')))

                    
map_user_table=pd.DataFrame(map_user)
map_user_table.index=map_user_table.index+1

map_user_table['State']=map_user_table['State'].replace('andaman-&-nicobar-islands', 'Andaman & Nicobar')
map_user_table['State']=map_user_table['State'].str.replace('Dadra & Nagar Haveli & Daman & Diu', 'Dadra and Nagar Haveli and Daman and Diu')
map_user_table['District']=map_user_table['District'].str.replace('district', '')
map_user_table['State']=map_user_table['State'].str.replace('-', ' ')
map_user_table['State']=map_user_table['State'].str.title()

                    

#top pincode transaction dataframe
path="C:/GUVI FOLDER/phonepe pulse visualization/data/top/transaction/country/india/"
Year_list=os.listdir(path)
#Agg_state_list

Top_tranp={"Years":[], "Quarters":[], "Top_pincodes":[], "Transaction_count":[], "Transaction_amount":[]}

for year in Year_list:
    if year != "state":
        pyear=path+year+"/"
        Quarter_list=os.listdir(pyear)
        for quarter in Quarter_list:
            pquarter=pyear+quarter
            data=open(pquarter,"r")
            file=json.load(data)
            #print(D['data'])
            #print(json.dumps(D, indent=2, sort_keys=True))

            #try:
            for item in file['data']['pincodes']:
                pincode=item['entityName']
                count=item['metric']['count']
                amount=item['metric']['amount']
                Top_tranp['Years'].append(year)
                Top_tranp['Quarters'].append(int(quarter.strip('.json')))
                Top_tranp['Top_pincodes'].append(pincode)
                Top_tranp['Transaction_count'].append(count)
                Top_tranp['Transaction_amount'].append(int(amount))

                    #Top_trans['Quarter'].append(int(quarter.strip('.json')))
            #except:
                #pass
        else:
            pass

Top_tranp_table=pd.DataFrame(Top_tranp)
Top_tranp_table.index=Top_tranp_table.index+1

#top pincode user dataframe
path="C:/GUVI FOLDER/phonepe pulse visualization/data/top/user/country/india/"
Year_list=os.listdir(path)
#Agg_state_list

Top_usersp={"Years":[], "Quarters":[], "Top_pincodes":[], "Registered_users":[]}

for year in Year_list:
    if year != "state":
        pyear=path+year+"/"
        Quarter_list=os.listdir(pyear)
        for quarter in Quarter_list:
            pquarter=pyear+quarter
            data=open(pquarter,"r")
            file=json.load(data)
        
            for item in file['data']['pincodes']:
                pincode=item['name']
                regUser=item['registeredUsers']
                Top_usersp['Years'].append(year)
                Top_usersp['Quarters'].append(int(quarter.strip('.json')))
                Top_usersp['Top_pincodes'].append(pincode)
                Top_usersp['Registered_users'].append(regUser)

#         else:
#             pass

Top_usersp_table=pd.DataFrame(Top_usersp)
Top_usersp_table['Top_pincodes']=Top_usersp_table['Top_pincodes'].str.title()
Top_usersp_table.index=Top_usersp_table.index+1


# geo visualization 
geojson_url = "https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson"
response = requests.get(geojson_url)
geojson_data = response.json()

#to display All India map
def aggregationU(Year, Quarter):  
    plot_agg=agg_tran_table[agg_tran_table["Years"]==Year]
    plot_agg.reset_index(drop=True, inplace=True)

    plot_agg_quarter=plot_agg[plot_agg["Quarters"]==Quarter]
    plot_agg_group=plot_agg_quarter.groupby("State")[["Transaction_count", "Transaction_amount"]].sum()
    #plot_agg_group=plot_agg_group.sort_values(by="Transaction_amount", ascending=False)
    plot_agg_group=plot_agg_group.reset_index()
    plot_agg_group.index=plot_agg_group.index+1

    return plot_agg_group



def dynamic_map_tranU(dataframemap):
    fig_choropleth = px.choropleth(
        dataframemap,
        geojson=geojson_data,
        featureidkey='properties.ST_NM',
        locations='State',
        color='Transaction_amount',
        hover_name='State',
        hover_data=['Transaction_count'],
        color_continuous_scale='Sunsetdark',
        title='Total Transaction Amount by State',
        labels={'Transaction_amount': 'Transaction Amount', 'Transaction_count': 'Transaction Count'},
        fitbounds= "locations"
    )
    #fig_choropleth.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    fig_choropleth.update_geos(visible =False)
    fig_choropleth.update_layout(coloraxis_colorbar=dict(title=' ', showticklabels=True), width=750, height=600)

    return fig_choropleth

#To display map after filter
def aggregationF(State, Year, Quarter):
    plot_map=map_tran_table[map_tran_table["Years"]==Year]
    plot_map.reset_index(drop=True, inplace=True)

    plot_map_quarter=plot_map[plot_map["Quarters"]==Quarter]
    plot_map_state=plot_map_quarter[plot_map_quarter["State"]==State]
    plot_map_group=plot_map_state.sort_values(by="Transaction_amount", ascending=False)
    plot_map_group=plot_map_group.reset_index()
    plot_map_group.index=plot_map_group.index+1

    return plot_map_state

def dynamic_map_tranF(dataframemap):
    fig_choropleth = px.choropleth(
        dataframemap,
        geojson=geojson_data,
        featureidkey='properties.ST_NM',
        locations='State',
        color='Transaction_amount',
        hover_name='State',
        hover_data=['Transaction_count'],
        color_continuous_scale='Sunsetdark',
        title='Total Transaction Amount by State',
        labels={'Transaction_amount': 'Transaction Amount', 'Transaction_count': 'Transaction Count'},
        fitbounds= "locations"
    )
    #fig_choropleth.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    fig_choropleth.update_geos(visible =False)
    fig_choropleth.update_layout(coloraxis_showscale=False, width=750, height=600)

    return fig_choropleth

#Top 10 states 
def aggregationUs(Years, Quarters):
    plot_agg=map_tran_table[map_tran_table["Years"]==Years]
    plot_agg.reset_index(drop=True, inplace=True)

    plot_agg_quarter=plot_agg[plot_agg["Quarters"]==Quarters]
    plot_agg_group=plot_agg_quarter.groupby("State")[["Transaction_count", "Transaction_amount"]].sum()
    plot_agg_group=plot_agg_group.sort_values(by="Transaction_amount", ascending=False)
    #plot_agg_group=plot_agg_group.head(10)
    plot_agg_group=plot_agg_group.reset_index()
    plot_agg_group.index=plot_agg_group.index+1
    plot_agg_group["rownumber"]=plot_agg_group.reset_index().index+1
    plot_agg_group["Transaction_amount"]=plot_agg_group["Transaction_amount"].apply(lambda x: f'{x:,}')
    return plot_agg_group

#top 10 districts in All India
def aggregationUd(Years, Quarters):
    plot_map=map_tran_table[map_tran_table["Years"]==Years]
    plot_map.reset_index(drop=True, inplace=True)

    plot_map_quarter=plot_map[plot_map["Quarters"]==Quarters]
    plot_map_group=plot_map_quarter.groupby("District")[["Transaction_count", "Transaction_amount"]].sum()
    plot_map_group=plot_map_group.sort_values(by="Transaction_amount", ascending=False)
    #plot_map_group=plot_map_group.head(10)
    plot_map_group=plot_map_group.reset_index()
    plot_map_group.index=plot_map_group.index+1
    plot_map_group["rownumber"]=plot_map_group.reset_index().index+1
    plot_map_group["Transaction_amount"]=plot_map_group["Transaction_amount"].apply(lambda x: f'{x:,}')
    return plot_map_group

#top 10 pincode in All India
def aggregationUp(Years, Quarters):
    plot_piny=Top_tranp_table[Top_tranp_table["Years"]==Years]
    plot_pinq=plot_piny[plot_piny["Quarters"]==Quarters]
    plot_pinq.reset_index(drop=True, inplace=True)
    plot_pinq.index=plot_pinq.index+1
    plot_pinq["rownumber"]=plot_pinq.reset_index().index+1
    plot_pinq["Transaction_amount"]=plot_pinq["Transaction_amount"].apply(lambda x: f'{x:,}')
    return plot_pinq


#top 10 districts state wise
def aggregationFd(Years, Quarters, State):
    plot_map=map_tran_table[map_tran_table["Years"]==Years]
    plot_map.reset_index(drop=True, inplace=True)

    plot_map_quarter=plot_map[plot_map["Quarters"]==Quarters]
    plot_map_state=plot_map_quarter[plot_map_quarter["State"]==State]
    plot_map_group=plot_map_state.groupby("District")[["Transaction_count", "Transaction_amount"]].sum()
    plot_map_group=plot_map_group.sort_values(by="Transaction_amount", ascending=False)
    #plot_map_group=plot_map_group.head(10)
    plot_map_group=plot_map_group.reset_index()
    plot_map_group.index=plot_map_group.index+1
    plot_map_group["rownumber"]=plot_map_group.reset_index().index+1
    plot_map_group["Transaction_amount"]=plot_map_group["Transaction_amount"].apply(lambda x: f'{x:,}')
    return plot_map_group


#value to display in categories
def aggregation_catU(Year, Quarter):  
    plot_agg=agg_tran_table[agg_tran_table["Years"]==Year]
    plot_agg.reset_index(drop=True, inplace=True)

    plot_agg_quarter=plot_agg[plot_agg["Quarters"]==Quarter]
    plot_agg_group=plot_agg_quarter.groupby("Transaction_type")[["Transaction_amount"]].sum()
    plot_agg_group=plot_agg_group.sort_values(by="Transaction_amount", ascending=False)
    plot_agg_group=plot_agg_group.reset_index()
    #plot_agg_group.index=plot_agg_group.index+1

    return plot_agg_group

def aggregation_catF(State, Year, Quarter):  
    plot_agg=agg_tran_table[agg_tran_table["Years"]==Year]
    plot_agg.reset_index(drop=True, inplace=True)

    plot_agg_quarter=plot_agg[plot_agg["Quarters"]==Quarter]
    plot_agg_state= plot_agg_quarter[plot_agg_quarter["State"]==State]
    plot_agg_state=plot_agg_state.groupby("Transaction_type")[["Transaction_amount"]].sum()
    plot_agg_state=plot_agg_state.sort_values(by="Transaction_amount", ascending=False)
    plot_agg_state=plot_agg_state.reset_index()
    #plot_agg_group.index=plot_agg_group.index+1

    return plot_agg_state

#----------------------------------------------------------------------------------------------------------------------------------
#Data for user map
def mapuserU(Year, Quarter):  
    plot_map=map_user_table[map_user_table["Years"]==Year]
    plot_map.reset_index(drop=True, inplace=True)

    plot_map_quarter=plot_map[plot_map["Quarters"]==Quarter]
    plot_map_group=plot_map_quarter.groupby("State")[["Registered_users", "App_opens"]].sum()
    plot_map_group=plot_map_group.reset_index()
    plot_map_group.index=plot_map_group.index+1
    
    return plot_map_group

def dynamic_map_userU(dataframemap):
    fig_choropleth = px.choropleth(
        dataframemap,
        geojson=geojson_data,
        featureidkey='properties.ST_NM',
        locations='State',
        color='Registered_users',
        hover_name='State',
        hover_data=['App_opens'],
        color_continuous_scale='darkmint',
        title='Total Registered Users by State',
        labels={'Registered_users': 'Registered Users', 'App_opens': 'App Opens'},
        fitbounds= "locations"
    )
    #fig_choropleth.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    fig_choropleth.update_geos(visible =False)
    fig_choropleth.update_layout(coloraxis_colorbar=dict(title=' ', showticklabels=True), width=750, height=600)

    return fig_choropleth


def mapuserF(State, Year, Quarter):
    plot_map=map_user_table[map_user_table["Years"]==Year]
    plot_map.reset_index(drop=True, inplace=True)
    plot_map_quarter=plot_map[plot_map["Quarters"]==Quarter]
    plot_map_state=plot_map_quarter[plot_map_quarter["State"]==State]
    plot_map_group=plot_map_state.sort_values(by="Registered_users", ascending=False)
    plot_map_group=plot_map_group.reset_index()
    plot_map_group.index=plot_map_group.index+1

    return plot_map_group

def dynamic_map_userF(dataframemap):
    fig_choropleth = px.choropleth(
        dataframemap,
        geojson=geojson_data,
        featureidkey='properties.ST_NM',
        locations='State',
        color='Registered_users',
        hover_name='State',
        hover_data=['App_opens'],
        color_continuous_scale='darkmint',
        title="Total Registered users by state",
        labels={'Registered_users': 'Registered Users', 'App_opens': 'App Opens'},
        fitbounds= "locations"
    )
    #fig_choropleth.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    fig_choropleth.update_geos(visible =False)
    fig_choropleth.update_layout(coloraxis_showscale=False, width=750, height=600)

    return fig_choropleth
                
                
# # geo visualization 
# geojson_url = "https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson"
# response = requests.get(geojson_url)
# geojson_data = response.json()


#streamlit code

selected=option_menu(
    menu_title="",
    options=["TRANSACTION", "USER", "ABOUT"],
    icons=["Currency rupee", "Currency rupee", "Currency rupee"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal"
)


if selected == "TRANSACTION":
    
#     tab1, tab2, tab3 = st.tabs(["AGGREGATED", "MAP", "TOP"])
    
#     with tab1:
        
        
        col11, col12, col13, col14 = st.columns([4, 2, 2, 2], gap="large")
        
        with col11:
            st.subheader("GEO VISUALIZATION")
        
        with col12:
            State=st.selectbox("State", ('All India','Andaman & Nicobar','Andhra Pradesh','Arunachal Pradesh','Assam','Bihar',
                                   'Chandigarh','Chhattisgarh','Dadra and Nagar Haveli and Daman and Diu','Delhi','Goa',
                                   'Gujarat','Haryana','Himachal Pradesh','Jammu & Kashmir','Jharkhand','Karnataka','Kerala','Ladakh',
                                   'Lakshadweep','Madhya Pradesh','Maharashtra','Manipur','Meghalaya','Mizoram','Nagaland','Odisha',
                                   'Puducherry','Punjab','Rajasthan','Sikkim','Tamil Nadu','Telangana','Tripura',
                                   'Uttar Pradesh','Uttarakhand','West Bengal'))
            
        with col13:
            year_value=["2018", "2019", "2020", "2021", "2022", "2023", "2024"]
            default_year=year_value.index("2024")
            Year=st.selectbox("Year", year_value, index=default_year)
            
        with col14:
            quarter_value=[1, 2, 3, 4]
            default_quarter=quarter_value.index(1)
            Quarter=st.selectbox("Quarter", quarter_value, index=default_quarter)
            
            
        col21, col22 = st.columns([2, 1])
        
        with col21:
            #st.plotly_chart(fig_choropleth, use_container_width=True)
            if State=='All India':
                displayU=aggregationU(Year, Quarter)
                dyn_mapU=dynamic_map_tranU(displayU)
                st.plotly_chart(dyn_mapU)
                
            else:
                displayF=aggregationF(State, Year, Quarter)
                dyn_mapF=dynamic_map_tranF(displayF)
                st.plotly_chart(dyn_mapF)

            
            # Alternative configurations:
            # st.plotly_chart(india_map, config=dict({'displayModeBar': False}, **{'displaylogo': False}))
            # st.plotly_chart(india_map, config=dict({'displayModeBar': False}, **{'displaylogo': False}), use_container_width=True)
        
        with col22:
            if State=="All India":
                st.title(":blue[Transactions]")
                st.subheader("All PhonePe transactions (UPI + Cards + Wallets)")
                tt=displayU["Transaction_count"].sum()
                st.write(f'# :blue[{tt:,}]')
                
            else:
                st.title(":blue[Transactions]")
                st.subheader("All PhonePe transactions (UPI + Cards + Wallets)")
                tt=displayF["Transaction_count"].sum()
                st.write(f'# :blue[{tt:,}]')
          
            #agt=f"{agt:,}"
               #st.html("""<span style='color: SkyBlue; font-size: 2rem'> f"{agt}" </span>""")
            #st.write(f'## :blue[{"₹"+agt}]')
            
            
            col221, col222, col223=st.columns([3,1,2])
            with col221:
                if State=="All India":
                    st.write("#### Total Transaction amount")
                    tta=round(displayU["Transaction_amount"].sum()/10000000)
                    st.write("")
                    st.write("")
                    st.write(f'## :blue[₹{tta:,}Cr]')
                    
                else:
                    st.write("#### Total Transaction amount")
                    tta=round(displayF["Transaction_amount"].sum()/10000000)
                    st.write("")
                    st.write("")
                    st.write(f'## :blue[₹{tta:,}Cr]')
                
            with col223:
                if State=="All India":
                    st.write("#### Avg. transaction value")
                    at=round(displayU["Transaction_amount"].sum()/displayU["Transaction_count"].sum())
                    st.write(f'## :blue[{at:,}Cr]')
                    
                else:
                    st.write("#### Avg. transaction value")
                    at=round(displayF["Transaction_amount"].sum()/displayF["Transaction_count"].sum())
                    st.write(f'## :blue[{at:,}Cr]')
                
                
            st.write("### Categories")
 
            if State=="All India":
                cat_value=aggregation_catU(Year, Quarter)
            
            else:
                cat_value=aggregation_catF(State, Year, Quarter)
           

            blankindex=['']*len(cat_value)
            cat_value.index=blankindex
            
            
            fs=cat_value[cat_value["Transaction_type"]=="Financial Services"]
            fsd=fs["Transaction_amount"]
            mp=cat_value[cat_value["Transaction_type"]=="Merchant payments"]
            mpd=mp["Transaction_amount"]
            ot=cat_value[cat_value["Transaction_type"]=="Others"]
            otd=ot["Transaction_amount"]
            p2p=cat_value[cat_value["Transaction_type"]=="Peer-to-peer payments"]
            p2pd=p2p["Transaction_amount"]
            rbp=cat_value[cat_value["Transaction_type"]=="Recharge & bill payments"]
            rbpd=rbp["Transaction_amount"]
          
           
        
            st.write("##### Merchant payments: " f" :blue[{mpd[0]:,}]")
            st.write("##### Peer-to-peer payments: " f" :blue[{p2pd[0]:,}]")
            st.write("##### Recharge and bill payments: " f" :blue[{rbpd[0]:,}]")
            st.write("##### Financial services: " f" :blue[{fsd[0]:,}]")
            st.write("##### others: " f" :blue[{otd[0]:,}]")
                
                
   
                
        st.title("Top performers")
        
        col31, col32 =st.columns([1,2])
 
        if State=="All India":
            
            with col31:
               
                top10=st.radio(" ", ["State", "District", "Pin Codes"], horizontal=True)
                    
                if top10=="State":
                    
                    with col31:
                        statetable=aggregationUs(Year, Quarter)
                        statetable10=statetable.head(10)

                        figtops=go.Figure(data=[go.Table(
                            header=dict(values=["Rank", "State", "Transaction amount"],
                                    line_color='darkslategray',
                                    fill_color='lightskyblue',
                                    font=dict(color='black'),
                                    align='left'),
                            cells=dict(values=[statetable10.rownumber, statetable10.State, statetable10.Transaction_amount],
                                    line_color='darkslategray',
                                    fill_color=[['lightcyan',"yellow"]*18],
                                    font=dict(color='black'),
                                    align='left'))])
                        figtops.update_layout(title="Top 10 States", width=400)
                        st.write(figtops)
                                
                        
                    with col32:
                        st.write("")
                        st.write("")
                        st.write("")
                        plgraph10=px.bar(statetable10, x="State", y="Transaction_amount", color="State", color_discrete_sequence=["orangered"], width=900)
                        st.plotly_chart(plgraph10)
                        

                elif top10=="District":
                    with col31:
                        distableU=aggregationUd(Year, Quarter)
                        distableU10=distableU.head(10)

                        figtops=go.Figure(data=[go.Table(
                            header=dict(values=["Rank", "District", "Transaction amount"],
                                    line_color='darkslategray',
                                    fill_color='lightskyblue',
                                    font=dict(color='black'),
                                    align='left'),
                            cells=dict(values=[distableU10.rownumber, distableU10.District, distableU10.Transaction_amount],
                                    line_color='darkslategray',
                                    fill_color=[['lightcyan',"yellow"]*18],
                                    font=dict(color='black'),
                                    align='left'))])
                        figtops.update_layout(title="Top 10 Districts", width=400)
                        st.write(figtops)
                        
                                         
                    
                    with col32:
                        st.write("")
                        st.write("")
                        st.write("")
                        plgraph10=px.bar(distableU10, x="District", y="Transaction_amount", color="District", color_discrete_sequence=["orangered"], width=900)
                        st.plotly_chart(plgraph10)

                        

                elif top10=="Pin Codes":
                    with col31:
                        pintable=aggregationUp(Year, Quarter)

                        figtops=go.Figure(data=[go.Table(
                            header=dict(values=["Rank", "Pin Code", "Transaction amount"],
                                    line_color='darkslategray',
                                    fill_color='lightskyblue',
                                    font=dict(color='black'),
                                    align='left'),
                            cells=dict(values=[pintable.rownumber, pintable.Top_pincodes, pintable.Transaction_amount],
                                    line_color='darkslategray',
                                    fill_color=[['lightcyan',"yellow"]*18],
                                    font=dict(color='black'),
                                    align='left'))])
                        figtops.update_layout(title="Top 10 Pin Codes", width=400)
                        st.write(figtops)
                        
                        
                    with col32:
                        st.write("")
                        st.write("")
                        plgraph10=px.bar(pintable, x="Top_pincodes", y="Transaction_amount", color="Top_pincodes", color_discrete_sequence=["orangered"], width=900)
                        st.plotly_chart(plgraph10)


               
                  
                    
        else:            
            with col31:

#                 distableF=displayF.copy(deep=True)
#                 distableF=distableF.sort_values(by="Transaction_amount", ascending=False)
#                 distableF10=distableF.head(10)
#                 distableF10.reset_index(drop=True, inplace=True)
#                 distableF10.index=distableF10.index+1
#                 distableF10["rownumber"]=distableF10.reset_index().index+1
#                 distableF10["Transaction_amount"]=distableF10["Transaction_amount"].apply(lambda x: f'{x:,}')
                distableF10=aggregationFd(Year, Quarter, State)
                distableF10=distableF10.head(10)

                figtops=go.Figure(data=[go.Table(
                    header=dict(values=["Rank", "District", "Transaction amount"],
                            line_color='darkslategray',
                            fill_color='lightskyblue',
                            font=dict(color='black'),
                            align='left'),
                    cells=dict(values=[distableF10.rownumber, distableF10.District, distableF10.Transaction_amount],
                            line_color='darkslategray',
                            fill_color=[['lightcyan',"yellow"]*18],
                            font=dict(color='black'),
                            align='left'))])
                figtops.update_layout(title="Top 10 Districts", width=400)
                st.write(figtops)
                
                
                
                
                
                        
            with col32:
                plgraph10=px.bar(distableF10, x="District", y="Transaction_amount", color="District", color_discrete_sequence=["orangered"], width=900)
                st.plotly_chart(plgraph10)
                
#         if top10!="Pin Codes":        
#             st.title("Overall Performance")
            
        col41, col42=st.columns([1,2])
        try:
            if top10=="State":
                with col41:

                    figtops=go.Figure(data=[go.Table(
                            header=dict(values=["Rank", "State", "Transaction amount"],
                                    line_color='darkslategray',
                                    fill_color='lightskyblue',
                                    font=dict(color='black'),
                                    align='left'),
                            cells=dict(values=[statetable.rownumber, statetable.State, statetable.Transaction_amount],
                                    line_color='darkslategray',
                                    fill_color=[['lightcyan',"yellow"]*18],
                                    font=dict(color='black'),
                                    align='left'))])
                    figtops.update_layout(title="All States", width=400)
                    st.write(figtops)

                with col42:
                    st.title("")
                    st.title("")
                    plgraph=px.bar(statetable, x="State", y="Transaction_amount", color="State", color_discrete_sequence=["orangered"], width=900)
                    st.plotly_chart(plgraph)

            elif top10=="District":
                with col41:

                    figtops=go.Figure(data=[go.Table(
                            header=dict(values=["Rank", "District", "Transaction amount"],
                                    line_color='darkslategray',
                                    fill_color='lightskyblue',
                                    font=dict(color='black'),
                                    align='left'),
                            cells=dict(values=[distableU.rownumber, distableU.District, distableU.Transaction_amount],
                                    line_color='darkslategray',
                                    fill_color=[['lightcyan',"yellow"]*400],
                                    font=dict(color='black'),
                                    align='left'))])
                    figtops.update_layout(title="All Districts", width=400)
                    st.write(figtops)
                    
                    

                with col42:
#                     plgraph=px.bar(distableU, x="District", y="Transaction_amount", color="District", color_discrete_sequence=["orangered"], width=900)
#                     st.plotly_chart(plgraph)
                    
                    plgraph=px.line(distableU, x="District", y="Transaction_amount", width=900)
                    st.plotly_chart(plgraph)

                    
                    

            elif top10=="Pin Codes":
                pass
        
        except:
            disF10=aggregationFd(Year, Quarter, State)
            
            with col41:

                    figtops=go.Figure(data=[go.Table(
                            header=dict(values=["Rank", "District", "Transaction amount"],
                                    line_color='darkslategray',
                                    fill_color='lightskyblue',
                                    font=dict(color='black'),
                                    align='left'),
                            cells=dict(values=[disF10.rownumber, disF10.District, disF10.Transaction_amount],
                                    line_color='darkslategray',
                                    fill_color=[['lightcyan',"yellow"]*18],
                                    font=dict(color='black'),
                                    align='left'))])
                    figtops.update_layout(title="All District", width=400)
                    st.write(figtops)

            with col42:
                st.title("")
                st.title("")
                plgraph=px.bar(disF10, x="District", y="Transaction_amount", color="District", color_discrete_sequence=["orangered"], width=900)
                st.plotly_chart(plgraph)

                  
if selected=="USER":
    st.write("will be updated soon")
  
        
    col11, col12, col13, col14 = st.columns([4, 2, 2, 2], gap="large")

    with col11:
        st.subheader("GEO VISUALIZATION")

    with col12:
        State=st.selectbox("State", ('All India','Andaman & Nicobar','Andhra Pradesh','Arunachal Pradesh','Assam','Bihar',
                               'Chandigarh','Chhattisgarh','Dadra and Nagar Haveli and Daman and Diu','Delhi','Goa',
                               'Gujarat','Haryana','Himachal Pradesh','Jammu & Kashmir','Jharkhand','Karnataka','Kerala','Ladakh',
                               'Lakshadweep','Madhya Pradesh','Maharashtra','Manipur','Meghalaya','Mizoram','Nagaland','Odisha',
                               'Puducherry','Punjab','Rajasthan','Sikkim','Tamil Nadu','Telangana','Tripura',
                               'Uttar Pradesh','Uttarakhand','West Bengal'))

    with col13:
        year_value=["2018", "2019", "2020", "2021", "2022", "2023", "2024"]
        default_year=year_value.index("2024")
        Year=st.selectbox("Year", year_value, index=default_year)

    with col14:
        quarter_value=[1, 2, 3, 4]
        default_quarter=quarter_value.index(1)
        Quarter=st.selectbox("Quarter", quarter_value, index=default_quarter)

    col21, col22 = st.columns([2, 1])

    with col21:
        #st.plotly_chart(fig_choropleth, use_container_width=True)
        if State=='All India':
#                 displayU=aggregationU(Year, Quarter)
#                 dyn_mapU=dynamic_map_tranU(displayU)
#                 st.plotly_chart(dyn_mapU)

            alluser=mapuserU(Year, Quarter)
            allusermap=dynamic_map_userU(alluser)
            st.plotly_chart(allusermap)

        else:
#                 displayF=aggregationF(State, Year, Quarter)
#                 dyn_mapF=dynamic_map_tranF(displayF)
#                 st.plotly_chart(dyn_mapF)

            stateuser=mapuserF(State, Year, Quarter)
            usermapF=dynamic_map_userF(stateuser)
            st.plotly_chart(usermapF)


        # Alternative configurations:
        # st.plotly_chart(india_map, config=dict({'displayModeBar': False}, **{'displaylogo': False}))
        # st.plotly_chart(india_map, config=dict({'displayModeBar': False}, **{'displaylogo': False}), use_container_width=True)

    with col22:
        if State=="All India":
            st.title(":purple[Users]")
            #Registered users upto
            df1=map_user_table[map_user_table["Years"]<Year]
            df2=map_user_table[(map_user_table["Years"]==Year) & (map_user_table["Quarters"]==Quarter)]
            df=pd.concat([df1,df2], axis=0)
           
            st.subheader(f"Registered PhonePe users till Q{Quarter} {Year} ")
            ru=df["Registered_users"].sum()
            st.write(f'# :orange[{ru:,}]')
            
            st.subheader(f"PhonePe app opens in Q{Quarter} {Year}")
            
            ao=alluser["App_opens"].sum()
            st.write(f"# :orange[{ao}]")
            

        else:
            st.title(":blue[Transactions]")
            st.subheader(f"Registered PhonePe users till Q{Quarter} {Year}")
            #registered users after filter
            df1=map_user_table[map_user_table["State"]==State]
            df2=df1[df1["Years"]<Year]
            df3=map_user_table[(map_user_table["State"]==State) & (map_user_table["Years"]==Year) & (map_user_table["Quarters"]<=Quarter)]
            df=pd.concat([df2,df3], axis=0)
            ru=df["Registered_users"].sum()
            st.write(f'# :violet[{ru:,}]')
            
            st.subheader(f"PhonePe app opens in Q{Quarter} {Year}")
            ao=stateuser["App_opens"].sum()
            st.write(f"# :violet[{ao}]")

    st.title("Top performers")

    col31, col32 =st.columns([1,2])

    if State=="All India":

        with col31:

            top10=st.radio(" ", ["State", "District", "Pin Codes"], horizontal=True)

            if top10=="State":

                with col31:
                    statetable=aggregationUs(Year, Quarter)
                    statetable10=statetable.head(10)

                    figtops=go.Figure(data=[go.Table(
                        header=dict(values=["Rank", "State", "Transaction amount"],
                                line_color='darkslategray',
                                fill_color='lightskyblue',
                                font=dict(color='black'),
                                align='left'),
                        cells=dict(values=[statetable10.rownumber, statetable10.State, statetable10.Transaction_amount],
                                line_color='darkslategray',
                                fill_color=[['lightcyan',"yellow"]*18],
                                font=dict(color='black'),
                                align='left'))])
                    figtops.update_layout(title="Top 10 States", width=400)
                    st.write(figtops)


                with col32:
                    st.write("")
                    st.write("")
                    st.write("")
                    plgraph10=px.bar(statetable10, x="State", y="Transaction_amount", color="State", color_discrete_sequence=["orangered"], width=900)
                    st.plotly_chart(plgraph10)


            elif top10=="District":
                with col31:
                    distableU=aggregationUd(Year, Quarter)
                    distableU10=distableU.head(10)

                    figtops=go.Figure(data=[go.Table(
                        header=dict(values=["Rank", "District", "Transaction amount"],
                                line_color='darkslategray',
                                fill_color='lightskyblue',
                                font=dict(color='black'),
                                align='left'),
                        cells=dict(values=[distableU10.rownumber, distableU10.District, distableU10.Transaction_amount],
                                line_color='darkslategray',
                                fill_color=[['lightcyan',"yellow"]*18],
                                font=dict(color='black'),
                                align='left'))])
                    figtops.update_layout(title="Top 10 Districts", width=400)
                    st.write(figtops)



                with col32:
                    st.write("")
                    st.write("")
                    st.write("")
                    plgraph10=px.bar(distableU10, x="District", y="Transaction_amount", color="District", color_discrete_sequence=["orangered"], width=900)
                    st.plotly_chart(plgraph10)



            elif top10=="Pin Codes":
                with col31:
                    pintable=aggregationUp(Year, Quarter)

                    figtops=go.Figure(data=[go.Table(
                        header=dict(values=["Rank", "Pin Code", "Transaction amount"],
                                line_color='darkslategray',
                                fill_color='lightskyblue',
                                font=dict(color='black'),
                                align='left'),
                        cells=dict(values=[pintable.rownumber, pintable.Top_pincodes, pintable.Transaction_amount],
                                line_color='darkslategray',
                                fill_color=[['lightcyan',"yellow"]*18],
                                font=dict(color='black'),
                                align='left'))])
                    figtops.update_layout(title="Top 10 Pin Codes", width=400)
                    st.write(figtops)


                with col32:
                    st.write("")
                    st.write("")
                    plgraph10=px.bar(pintable, x="Top_pincodes", y="Transaction_amount", color="Top_pincodes", color_discrete_sequence=["orangered"], width=900)
                    st.plotly_chart(plgraph10)





    else:            
        with col31:

            distableF10=aggregationFd(Year, Quarter, State)
            distableF10=distableF10.head(10)

            figtops=go.Figure(data=[go.Table(
                header=dict(values=["Rank", "District", "Transaction amount"],
                        line_color='darkslategray',
                        fill_color='lightskyblue',
                        font=dict(color='black'),
                        align='left'),
                cells=dict(values=[distableF10.rownumber, distableF10.District, distableF10.Transaction_amount],
                        line_color='darkslategray',
                        fill_color=[['lightcyan',"yellow"]*18],
                        font=dict(color='black'),
                        align='left'))])
            figtops.update_layout(title="Top 10 Districts", width=400)
            st.write(figtops)


        with col32:
            plgraph10=px.bar(distableF10, x="District", y="Transaction_amount", color="District", color_discrete_sequence=["orangered"], width=900)
            st.plotly_chart(plgraph10)


if selected=="ABOUT":
    st.write("PhonePe Group is India’s leading fintech company. Its flagship product, the PhonePe digital payments app, was launched in Aug 2016. Within a short period of time, the company has scaled rapidly to become India’s leading consumer payments app. On the back of its leadership in digital payments, PhonePe Group has expanded into financial services - Insurance, Lending, & Wealth as well as new consumer tech businesses - Pincode and Indus Appstore.")
        
        
    st.write("The Indian digital payments story has truly captured the world's imagination. From the largest towns to the remotest villages, there is a payments revolution being driven by the penetration of mobile phones and data.")

    st.write("When PhonePe started 5 years back, we were constantly looking for definitive data sources on digital payments in India. Some of the questions we were seeking answers to were - How are consumers truly using digital payments? What are the top cases? Are kiranas across Tier 2 and 3 getting a facelift with the penetration of QR codes?"
"This year as we became India's largest digital payments platform with 46% UPI market share, we decided to demystify the what, why and how of digital payments in India.")

    st.write("This year, as we crossed 2000 Cr. transactions and 30 Crore registered users, we thought as India's largest digital payments platform with 46% UPI market share, we have a ring-side view of how India sends, spends, manages and grows its money. So it was time to demystify and share the what, why and how of digital payments in India.")

    st.write("PhonePe Pulse is your window to the world of how India transacts with interesting trends, deep insights and in-depth analysis based on our data put together by the PhonePe team")

#"C:/Users/jodir/GUVI FOLDER/phonepe pulse visualization/phonepe streamlit2.py"


