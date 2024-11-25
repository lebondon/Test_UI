import streamlit as st
import pandas as pd
import xlsxwriter
import io

def convert_to_excel(df):
    output = io.BytesIO()
    writer = pd.ExcelWriter(output, engine="xlsxwriter")
    df.to_excel(writer, sheet_name="data")
    # see: https://xlsxwriter.readthedocs.io/working_with_pandas.html
    writer.close()
    return output.getvalue()

def process_dataframe(df):
    df=df.dropna()
    df = df[df.Price != 'Ask For Price']
    df=df[df.values != 'Ask For Price']
    df['Price'] = df['Price'].str.replace(r',', '', regex=True).astype(float)
    df['kms_driven'] = df['kms_driven'].str.slice(stop=-4)
    df['kms_driven'] = df['kms_driven'].str.replace(r',', '', regex=True).astype(int)
    df['house'] = df['name'].str.extract(r'^(\S+)')
    df.drop('name',axis=1)
    df['Price']=df['Price'].apply(lambda x: x/100) 
    df=df.drop(columns='name')
    one_hot=pd.get_dummies(df['fuel_type'])
    df=df.drop('fuel_type',axis=1)
    df = df.join(one_hot)
    return df
     

def main():
    st.title('Car Dataset Tranformation')
    uploaded_file = st.file_uploader("inserisci un file CSV o XLSX",type=['csv','xlsx'])

    if uploaded_file is not None:
        if uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file)
            st.success("File CSV caricato con successo!")
        elif uploaded_file.name.endswith('.xlsx'):
            df = pd.read_excel(uploaded_file)
            st.success("File XLSX caricato con successo!")
        else:
            st.error("Formato file non supportato!")
    if st.button('Start Processing', help="Process Dataframe"):
            df=process_dataframe(df)
            st.dataframe(df)
            st.balloons()
            st.download_button(
                                label="download as Excel-file",
                                data=convert_to_excel(df),
                                file_name="data.xlsx",
                                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                                key="excel_download",
                                )   


if __name__== "__main__":
    main()