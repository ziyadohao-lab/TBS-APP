import streamlit as st

st.set_page_config(page_title="Cooktop Troubleshooting", page_icon="🔧")

st.title("Cooktop Troubleshooting Tool")

# 初始化状态
if "step" not in st.session_state:
    st.session_state.step = 1
if "code" not in st.session_state:
    st.session_state.code = None


def next_step(step):
    st.session_state.step = step


# Step 1
if st.session_state.step == 1:

    st.subheader("Step 1")
    st.write("Is the manual operation successful?")

    col1, col2 = st.columns(2)

    if col1.button("Yes"):
        next_step(2)

    if col2.button("No"):
        next_step(10)


# Step 2
elif st.session_state.step == 2:

    st.subheader("Step 2")
    st.write("AP / Internet light normal?")

    col1, col2 = st.columns(2)

    if col1.button("Yes"):
        next_step(3)

    if col2.button("No"):
        st.session_state.code = 9100000
        next_step(99)


# Step 3
elif st.session_state.step == 3:

    st.subheader("Step 3")
    st.write("Switch online?")

    col1, col2 = st.columns(2)

    if col1.button("Yes"):
        st.session_state.code = 9111000
        next_step(99)

    if col2.button("No"):
        next_step(4)


# Step 4
elif st.session_state.step == 4:

    st.subheader("Step 4")
    st.write("Gateway two lights on?")

    col1, col2 = st.columns(2)

    if col1.button("Yes"):
        st.session_state.code = 9110100
        next_step(99)

    if col2.button("No"):
        next_step(5)


# Step 5
elif st.session_state.step == 5:

    st.subheader("Step 5")
    st.write("Repower the Gateway, two lights on?")

    col1, col2 = st.columns(2)

    if col1.button("Yes"):
        next_step(6)

    if col2.button("No"):
        st.session_state.code = 9110000
        next_step(99)


# Step 6
elif st.session_state.step == 6:

    st.subheader("Step 6")
    st.write("Issue solved?")

    col1, col2 = st.columns(2)

    if col1.button("Yes"):
        st.success("Done")

    if col2.button("No"):
        st.session_state.code = 9110011
        next_step(99)


# Step 10
elif st.session_state.step == 10:

    st.subheader("Step 2")
    st.write("Can you hear the relay sound when operating the switch?")

    col1, col2 = st.columns(2)

    if col1.button("Yes"):
        st.session_state.code = 9010000
        next_step(99)

    if col2.button("No"):
        next_step(11)


# Step 11
elif st.session_state.step == 11:

    st.subheader("Step 3")
    st.write("Indicator light on?")

    col1, col2 = st.columns(2)

    if col1.button("Yes"):
        st.session_state.code = 9001000
        next_step(99)

    if col2.button("No"):
        next_step(12)


# Step 12
elif st.session_state.step == 12:

    st.subheader("Step 4")
    st.write("Circuit breaker on?")

    col1, col2 = st.columns(2)

    if col1.button("Yes"):
        st.session_state.code = 9001000
        next_step(99)

    if col2.button("No"):
        st.session_state.code = 9000100
        next_step(99)


# Result
elif st.session_state.step == 99:

    code = st.session_state.code

    st.success(f"Diagnosis Code: {code}")

    if code == 9100000:
        st.write("AP / Internet issue")

    elif code == 9111000:
        st.write("Check Automation")

    elif code == 9110100:
        st.write("IP Issue")

    elif code == 9110011:
        st.write("IP Issue")

    elif code == 9110000:
        st.write("Internet Issue")

    elif code == 9010000:
        st.write("Cooktop damage not switch related issue")

    elif code == 9001000:
        st.write("Switch damage please contact professional for repair or replacement")

    elif code == 9000100:
        st.write("Please open the breaker")

    if st.button("Restart"):
        st.session_state.step = 1
        st.session_state.code = None