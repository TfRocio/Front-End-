import streamlit as st

# Set title for the app
st.title("Bot de Tránsito")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("Tell me any question that you got?"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Echo the user's message
    response = f"Echo: {prompt}"
    # Display bot's response in chat message container
    with st.chat_message("bot"):
        st.markdown(response)
    # Add bot's response to chat history
    st.session_state.messages.append({"role": "bot", "content": response})
