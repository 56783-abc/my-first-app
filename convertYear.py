import streamlit as st
st.tillie("แอปพลิเคชั่นแปลง พ.ศ. เป็น ค.ศ.")

bh_year=st.number_input("พ.ศ.2567,value=2569)
ce_year=bh_year-543
st.header(f"ปี ค.ศ. คือ : {ce_year}")
