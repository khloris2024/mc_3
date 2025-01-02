import streamlit as st
import pandas as pd
# import matplotlib.pyplot as plt
import plotly.express as px
def read_dataset():
    df = pd.read_csv('score.csv', index_col=None)
    return df
    # return df

def process(df):
    df.fillna(0, inplace=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.write("Khối chuyên")
        toantin = st.checkbox('Toan - Tin',value=True)
        if toantin is False:
            df = df[~(df['Class'].str.contains('CT'))]
        lhs = st.checkbox('Ly - Hoa - Sinh',value=True)
        if lhs is False:
            df = df[~(df['Class'].str.contains('CSI') | df['Class'].str.contains('CH') | df['Class'].str.contains('CL'))]
        va = st.checkbox('Van - Anh',value=True)
        if va is False:
            df = df[~(df['Class'].str.contains('CA') | df['Class'].str.contains('CV'))]
        others = st.checkbox('Khac',value=True)
       
    with col2:
        # st.write("Khoi lop")
        khoilop = ['Tất cả','Lớp 10', 'Lớp 11', 'Lớp 12']
        khoi =  st.radio("Khoi lop", khoilop, index = None)
        if khoi == 'Lớp 10':
            df = df[df['Class'].str.startswith('10')]
        elif khoi == 'Lớp 11':
            df = df[df['Class'].str.startswith('11')]
        elif khoi == 'Lớp 12':
            df = df[df['Class'].str.startswith('12')]
        else:
            df = df

    with col3:
        time = ['Tat ca', 'Sang', 'Chieu']
        giohoc = st.selectbox('Gio hoc',time)
        if giohoc == 'Sang':
            df = df[df['MC-Class'].str.startswith('M')]
        elif giohoc == 'Chieu':
            df = df[df['MC-Class'].str.startswith('A')]
        else:
            df = df


    col4, col5 = st.columns(2)
    with col4:
        df['P3'] = df['P3-1']+df['P3-2']+df['P3-3']+df['P3-4']
        total= df['P1'] + df['P2'] +df['P3']
        df['total'] = total
        df.drop(columns=['P3-1','P3-2','P3-3','P3-4'], inplace = True)
        st.dataframe(df,hide_index=True)
    with col5:
        col5_1, col5_2, col5_3 = st.columns(3)
        with col5_1:
            st.write("Cao nhat:",max(df['total']))
        with col5_3:
            st.write("Trung binh",round((sum(df['total'])/len(df)),1))
        with col5_2:
            st.write("Thap nhat",min(df['total']))
        tb = total/3
        # df1 = df[df['Gender'].isin(['M','F'])]
        df1 = df[['total','Gender','MC-Class']].groupby(['Gender','MC-Class']).median()
        df1.reset_index(inplace=True)
        fig = px.bar(df1, x='Gender', y='total', color='MC-Class', barmode='group')
        st.plotly_chart(fig, use_container_width=True)

        
    




def main():
    st.header("Bảng điểm thi giữa kì lớp MC4AI")
    df=read_dataset()
    process(df)
    # show interface

       # filter

       # list & chart

main()