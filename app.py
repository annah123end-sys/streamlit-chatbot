import streamlit as st
from google import genai
from google.genai import types

import os
from dotenv import load_dotenv

st.title(":blue[:material/conversation:] 한솔쌤")
st.caption("한솔이에요.")

MODEL_NAME = "gemini-2.5-flash"

@st.cache_resource
def get_client():
    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        st.error("🔑API 키가 설정되지 않았습니다.")
        st.stop()

    return genai.Client(api_key=api_key)
    
client = get_client()

from pathlib import Path

def load_system_prompt(filename):
    """
    파일 이름을 입력받아 내용을 읽어서 반환합니다.
    파일이 없으면 기본 프롬프트를 반환합니다.
    """
    try:
        # 현재 실행 중인 파이썬 파일의 위치를 기준으로 경로 설정
        current_dir = Path(__file__).parent
        file_path = current_dir / filename
        
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        # 파일이 없을 경우를 대비한 최소한의 가이드라인
        return "당신은 한솔쌤입니다. 불친절하지만 가끔 친절하게 답변하세요."

if "chat_session" not in st.session_state:
    system_prompt = load_system_prompt("system_prompt.md")
    st.session_state.chat_session = client.chats.create(
        model=MODEL_NAME,
        config=types.GenerateContentConfig(
            system_instruction="너는 한솔쌤이야. 말할때마다 짜증을 내"


        )

    )



if "messages" not in st.session_state:
    st.session_state.messages = []
for message in st.session_state.messages:
     with st.chat_message(message["role"]):
        st.write(message["content"])

if prompt:= st.chat_input("한솔쌤에게 물어보기"):
    with st.chat_message("user"):
        st.write(prompt)
        st.session_state.messages.append({
            "role": "user" ,
            "content": prompt
        })

    with st.chat_message("ai"):
        response = st.session_state.chat_session.send_message(prompt)
        st.write(response.text)
        st.session_state.messages.append({
            "role": "ai" ,
            "content": response.text
        })
