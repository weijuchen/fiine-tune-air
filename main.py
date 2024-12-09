import streamlit as st

from utility import air_conditioner_recommendation

st.title("研能科技空調推薦系統 🆒")

st.divider()
# user_request=st.text_input(r"$\textsf{\Large 🌡️ 請輸入使用者之空間用途及使用坪數 🌡️}$")
user_request=st.text_input("🌡️ 請輸入用戶之空間用途及使用坪數 (使用坪數請輸入10-25坪) 🌡️ ")
submit = st.button("❄️ 產生推薦空調型號 ❄️")



if submit and not user_request:
    st.info("请输入使用者之空間用途及使用坪數")
    st.stop()

if submit:
    with st.spinner("AI正在運行中，請稍後..."):
        result = air_conditioner_recommendation(user_request)
        
        
    st.success("空調推薦系統執行完畢！")
    st.subheader("推薦型號 ✇🌫 ：")
    st.write(result)
 

