import streamlit as st
import time
import random

# 页面基础配置
st.set_page_config(page_title="3.8 专属惊喜", page_icon="🌹", layout="centered")

# 自定义 CSS 让界面更精致
st.markdown("""
    <style>
    .main { background-color: #fff5f5; }
    .stButton>button { width: 100%; border-radius: 20px; border: 1px solid #ff4b4b; color: #ff4b4b; }
    h1 { color: #d63384; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

st.title("✨ 属于你的 3.8 节惊喜 ✨")

# 1. 身份验证（增加一点仪式感）
if 'auth' not in st.session_state:
    st.session_state.auth = False

if not st.session_state.auth:
    psw = st.text_input("请输入我们的专属暗号（比如你的生日）：", type="password")
    if psw == "0308": # 这里改为你们约定的数字
        st.session_state.auth = True
        st.success("验证通过！正在开启...")
        time.sleep(1)
        st.rerun()
    elif psw:
        st.error("暗号不对哦，再想想？")

# 2. 验证通过后的交互内容
if st.session_state.auth:
    # 模拟“爱意加载”
    progress_text = "正在调动全宇宙的浪漫资源..."
    my_bar = st.progress(0, text=progress_text)
    for percent_complete in range(100):
        time.sleep(0.01)
        my_bar.progress(percent_complete + 1, text=progress_text)
    
    st.balloons() # 满屏气球
    
    st.header("🌹 亲爱的，女神节快乐！")
    
    # 动态祝福展示
    quotes = [
        "愿你眼中总有光芒，活成自己喜欢的模样。",
        "不只是今天，每一天你都闪闪发光。",
        "世界因你而温柔，愿你被生活温柔以待。",
        "做自己的女王，不卑不亢，不慌不忙。"
    ]
    
    st.info(random.choice(quotes))
    
    # 互动环节
    col1, col2 = st.columns(2)
    with col1:
        if st.button("点此接收一束花 💐"):
            st.write("🌷🌻🌹🌼🌸🌺")
    with col2:
        if st.button("点此接收一个抱抱 🤗"):
            st.write("🧸💖✨")

    # 底部留言
    st.text_area("我想对你说：", "在这里写下你最想对她说的话，她可以直接看到...")