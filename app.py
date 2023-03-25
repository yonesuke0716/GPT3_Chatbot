import streamlit as st

import openai

st.title("ChatGPT Chatbot")
# APIキーの設定
openai.api_key = "your openapi key"


@st.cache_resource
def chat_save():
    chat_dict_list = []
    return chat_dict_list


chat_log = chat_save()
input_text = st.text_input("チャット入力欄", "入力後、「送信」ボタンを押してください。")
if st.button("送信"):
    chat_log.append({"role": "user", "content": input_text})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=chat_log,
        max_tokens=1000,
    )
    chat_log.append(
        {
            "role": "assistant",
            "content": response.choices[0]["message"]["content"].strip(),
        }
    )
    for num in range(len(chat_log)):
        if num % 2 == 0:
            st.subheader("あなた:")
        else:
            st.subheader("GPT:")
        st.write(chat_log[num]["content"])
else:
    st.write("チャットを入力したら、「送信」ボタンを押してください。")
