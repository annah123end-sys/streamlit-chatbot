import streamlit as st

st.title(":orange[:material/smart_toy:] 에코봇")

if "messages" not in st.session_state:
    st.session_state.messages = []
for message in st.session_state.messages:
     with st.chat_message(message["role"]):
        st.write(message["content"])

if prompt:= st.chat_input("에코봇에게 물어보기"):
    with st.chat_message("user"):
        st.write(prompt)
        st.session_state.messages.append({
            "role": "user" ,
            "content": prompt
        })

    with st.chat_message("ai"):
        st.write(prompt)
        st.session_state.messages.append({
            "role": "ai" ,
            "content": prompt
        })
