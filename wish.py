import streamlit as st
import time

# 1. 页面配置
st.set_page_config(page_title="Special Gift", page_icon="🌹", layout="centered")

# 2. 回归经典：大厂极简玻璃拟态
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@400;700&display=swap');

    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #ff6a88 100%);
        background-size: 400% 400%;
        animation: gradientBG 12s ease infinite;
    }
    @keyframes gradientBG {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    /* 回归最初的方框设计：纯粹、无边框、高透 */
    .glass-card {
        background: rgba(255, 255, 255, 0.15);
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        border-radius: 24px;
        padding: 40px 30px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
        text-align: center;
        margin-top: 20px;
        color: white;
    }

    .title-text {
        font-size: 32px !important;
        font-weight: 700;
        margin-bottom: 10px;
    }

    .main-desc {
        font-size: 22px !important;
        line-height: 1.6;
        margin-bottom: 30px;
    }

    /* 保证输入框在深色背景下清晰 */
    .stTextInput>div>div {
        background: rgba(255, 255, 255, 0.9) !important;
        border-radius: 12px !important;
    }
    .stTextInput input {
        color: #333 !important;
    }

    .stButton>button {
        background: white !important;
        color: #764ba2 !important;
        border-radius: 50px !important;
        padding: 8px 45px !important;
        font-size: 18px !important;
        font-weight: 700 !important;
        border: none !important;
    }
    
    header {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# 3. 状态管理
if 'step' not in st.session_state:
    st.session_state.step = 1

# --- 界面逻辑 ---

# 顶部标题（放回方框上方，保持最初的开阔感）
st.markdown("<h1 style='text-align:center; color:white;'>Happy 3.8 Day</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:rgba(255,255,255,0.8); letter-spacing:3px;'>女神节 · 专属礼遇</p>", unsafe_allow_html=True)

# 核心方框：仅包裹交互内容
st.markdown('<div class="glass-card">', unsafe_allow_html=True)

if st.session_state.step == 1:
    st.markdown('<p class="title-text">Step 01</p>', unsafe_allow_html=True)
    st.markdown('<p class="main-desc">Hi, 今天是几月几日？</p>', unsafe_allow_html=True)
    q1 = st.text_input("Date", placeholder="例如: 3.8", label_visibility="collapsed")
    if st.button("下一步"):
        if "3" in q1 and "8" in q1:
            st.session_state.step = 2
            st.rerun()
        else: st.error("日期不对哦~")

elif st.session_state.step == 2:
    st.markdown('<p class="title-text">Step 02</p>', unsafe_allow_html=True)
    st.markdown('<p class="main-desc">让我猜猜，谁还在加班？🤔</p>', unsafe_allow_html=True)
    q2 = st.text_input("Name", placeholder="输入名字", label_visibility="collapsed")
    if st.button("解锁心意"):
        if any(x in q2 for x in ["沈渊博", "我", "你自己"]):
            st.session_state.step = 3
            st.rerun()
        else: st.warning("名字不对哦~")

elif st.session_state.step == 3:
    st.snow()
    st.markdown('<p class="title-text">Phase 01</p>', unsafe_allow_html=True)
    st.markdown('<p class="main-desc">“ 愿你所有的努力，<br>都有温暖的回响。 ”</p>', unsafe_allow_html=True)
    st.write("沈老师，加班辛苦啦。休息一下吧。☕")
    if st.button("继续"):
        st.session_state.step = 4
        st.rerun()

elif st.session_state.step == 4:
    st.balloons()
    st.markdown('<p class="title-text">Phase 02</p>', unsafe_allow_html=True)
    st.markdown('<p class="main-desc">“ 3月8日，<br>愿你始终闪闪发光。 ”</p>', unsafe_allow_html=True)
    st.write("愿你做自己的女王，不卑不亢。🌹")
    if st.button("压轴惊喜"):
        st.session_state.step = 5
        st.rerun()

elif st.session_state.step == 5:
    st.balloons()
    st.markdown('<p class="title-text">Best Wish</p>', unsafe_allow_html=True)
    st.markdown('<p class="main-desc" style="font-weight:700; color:#ffeaa7;">祝下周公开课，<br>旗开得胜，圆满成功！</p>', unsafe_allow_html=True)
    st.write("你是最棒的，加油！💪")
    if st.button("重新开始"):
        st.session_state.step = 1
        st.rerun()

st.markdown('</div>', unsafe_allow_html=True)