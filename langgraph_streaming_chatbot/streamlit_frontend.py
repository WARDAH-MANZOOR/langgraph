import streamlit as st
from langgraph_backend import chatbot
from langchain_core.messages import HumanMessage, AIMessage


CONFIG = {'configurable':{'thread_id':'thread-1'}}
# session state me message history ko store karna 
if 'message_history' not in st.session_state:
    st.session_state['message_history'] = []
# # loading the conversation history
for message in st.session_state['message_history']:
    with st.chat_message(message['role']):
        st.text(message['content']) 


# message_history = [] # list use karne par message history har baar enter karne par reset hojati hai jske waja se hum session state use karte hain

# # loading the conversation history
# for message in message_history:
#     with st.chat_message(message['role']):
#         st.text(message['content']) 


# message history format

# {'role':'user','content':'Hi'} 
# {'role':'assistant','content':'Hello! How can I assist you today?'}

user_input = st.chat_input("Type your message here...")
if user_input:
    # add user message to message_history
    st.session_state['message_history'].append({'role':'user','content':user_input})
    with st.chat_message("user"):
        st.text(user_input)

    # response = chatbot.invoke({"messages":[HumanMessage(content=user_input)]}, config = CONFIG)   
    # ai_message = response['messages'][-1].content
    # add assistant message to message_history
    # st.session_state['message_history'].append({'role':'assistant','content':ai_message})
    with st.chat_message("assistant"):
        ai_message = st.write_stream(
            message_chunk.content for message_chunk,metadata in chatbot.stream(
                {"messages": [HumanMessage(content=user_input)]},
                config={"configurable": {"thread_id": "thread-1"}},
                stream_mode='messages',
            )
        )
st.session_state['message_history'].append({'role':'assistant','content':ai_message})


# for message_chunk,metadata in chatbot.stream(
    # {"messages": [HumanMessage(content="Hello, how are you?")]},
    # config={"configurable": {"thread_id": "thread-1"}},
    # stream_mode='messages',
# ):
#     if message_chunk.content:
#         print(message_chunk.content, end = " ", flush=True)

