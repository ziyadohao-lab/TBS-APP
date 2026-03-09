import streamlit as st

st.set_page_config(page_title="Troubleshooting", page_icon="🔧")

st.markdown("""
<style>

/* YES 按钮 */
button[data-testid="baseButton-secondary"][key*="yes"] {
    background-color: #28a745;
    color: white;
    border-radius: 8px;
    font-size: 18px;
    height: 50px;
}

button[data-testid="baseButton-secondary"][key*="yes"]:hover {
    background-color: #218838;
}

/* NO 按钮 */
button[data-testid="baseButton-secondary"][key*="no"] {
    background-color: #dc3545;
    color: white;
    border-radius: 8px;
    font-size: 18px;
    height: 50px;
}

button[data-testid="baseButton-secondary"][key*="no"]:hover {
    background-color: #c82333;
}

</style>
""", unsafe_allow_html=True)

st.title("Troubleshooting Tool")

# 初始化状态
if "step" not in st.session_state:
    st.session_state.step = 1
if "code" not in st.session_state:
    st.session_state.code = None


# ===== 如果已经得到结果，直接输出并停止 =====
if st.session_state.code is not None:

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
        st.rerun()

    st.stop()
# ============================================


def next_step(step):
    st.session_state.step = step
    st.rerun()


# Step 1
if st.session_state.step == 1:

    st.subheader("Step 1")
    st.write("Is the manual operation successful?")

    col1, col2 = st.columns(2)

    if col1.button("Yes", key="yes1"):
        next_step(2)

    if col2.button("No", key="no1"):
        next_step(10)


# Step 2
elif st.session_state.step == 2:

    st.subheader("Step 2")
    st.write("AP / Internet light normal?")

    col1, col2 = st.columns(2)

    if col1.button("Yes", key="yes2"):
        next_step(3)

    if col2.button("No", key="no2"):
        st.session_state.code = 9100000
        st.rerun()


# Step 3
elif st.session_state.step == 3:

    st.subheader("Step 3")
    st.write("Switch online?")

    col1, col2 = st.columns(2)

    if col1.button("Yes", key="yes3"):
        st.session_state.code = 9111000
        st.rerun()

    if col2.button("No", key="no3"):
        next_step(4)


# Step 4
elif st.session_state.step == 4:

    st.subheader("Step 4")
    st.write("Gateway two lights on?")

    col1, col2 = st.columns(2)

    if col1.button("Yes", key="yes4"):
        st.session_state.code = 9110100
        st.rerun()

    if col2.button("No", key="no4"):
        next_step(5)


# Step 5
elif st.session_state.step == 5:

    st.subheader("Step 5")
    st.write("Repower the Gateway, two lights on?")

    col1, col2 = st.columns(2)

    if col1.button("Yes", key="yes5"):
        next_step(6)

    if col2.button("No", key="no5"):
        st.session_state.code = 9110000
        st.rerun()


# Step 6
elif st.session_state.step == 6:

    st.subheader("Step 6")
    st.write("Issue solved?")

    col1, col2 = st.columns(2)

    if col1.button("Yes", key="yes6"):
        st.success("Done")

    if col2.button("No", key="no6"):
        st.session_state.code = 9110011
        st.rerun()


# Step 10
elif st.session_state.step == 10:

    st.subheader("Step 2")
    st.write("Can you hear the relay sound when operating the switch?")

    col1, col2 = st.columns(2)

    if col1.button("Yes", key="yes10"):
        st.session_state.code = 9010000
        st.rerun()

    if col2.button("No", key="no10"):
        next_step(11)


# Step 11
elif st.session_state.step == 11:

    st.subheader("Step 3")
    st.write("Indicator light on?")

    col1, col2 = st.columns(2)

    if col1.button("Yes", key="yes11"):
        st.session_state.code = 9001000
        st.rerun()

    if col2.button("No", key="no11"):
        next_step(12)


# Step 12
elif st.session_state.step == 12:

    st.subheader("Step 4")
    st.write("Circuit breaker on?")

    col1, col2 = st.columns(2)

    if col1.button("Yes", key="yes12"):
        st.session_state.code = 9001000
        st.rerun()

    if col2.button("No", key="no12"):
        st.session_state.code = 9000100

        st.rerun()



