from openai import OpenAI
import streamlit as st
# Config Parse
# from configparser import ConfigParser
# config = ConfigParser()
# config.read("config.ini")

# key = config["OPEN_AI"]["API_KEY"]
# key = st.secrets["openai"]["OPENAI_API_KEY"]
# api_key = st.secrets["GOOGLE_API_KEY"] 
key=st.secrets["OPENAI_API_KEY"]
def air_conditioner_recommendation(user_request):
    client = OpenAI(api_key=key)


    completion = client.chat.completions.create(
    model="ft:gpt-3.5-turbo-0125:personal:microjet-v2:AYROs5Ka",
    messages=[
        {"role": "system", "content": "You are a professional air conditioning technician who provides adviceon choosing suitable air conditioning models. below are the air conditioner models you can recommend: zhac1-2.9-o / zhac1-2.9-i, zhac1-3.6-o / zhac1-3.6-i, zhac1-4.1-o / zhac1-4.1-i, zhac1-5.2-o / zhac1-5.2-i, zhac1-6.3-o / zhac1-6.3-i, zhac1-7.3-o / zhac1-7.3-i."},  

         {"role": "user", "content": user_request}

    ]
    )
  
 
    return(completion.choices[0].message.content)
    # return 
