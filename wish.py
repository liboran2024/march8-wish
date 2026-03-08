import streamlit as st
import time

# 1. 页面配置
st.set_page_config(page_title="3.8 Special Gift", page_icon="🌹", layout="centered")

# 2. UI 样式：确保内容完美嵌套在方框内
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@400;700&family=Dancing+Script:wght@700&display=swap');

    /* 动态极光背景 */
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

    /* 核心圆角方框（Glass Card） */
    .glass-card {
        background: rgba(255, 255, 255, 0.15);
        backdrop-filter: blur(25px);
        -webkit-backdrop-filter: blur(25px);
        border-radius: 32px;
        padding: 40px 25px;
        box-shadow: 0 15px 35px rgba(0, 0, 0, 0.2);
        text-align: center;
        border: none;
        margin-top: 20px;
        color: white;
    }

    /* 方框内标题：两行大小接近，排版紧凑 */
    .inner-title-1 {
        font-family: 'Dancing Script', cursive;
        font-size: 38px !important;
        color: #ffffff;
        margin-bottom: 0px;
        line-height: 1.2;
    }
    .inner-title-2 {
        font-family: 'Noto Sans SC', sans-serif;
        font-size: 24px !important;
        font-weight: 500;
        color: rgba(255, 255, 255, 0.95);
        letter-spacing: 2px;
        margin-top: 5px;
        margin-bottom: 30px;
    }

    .main-desc {
        font-size: 22px !important;
        line-height: 1.6;
        margin-bottom: 30px;
    }

    /* 输入框样式：纯净无毛边 */
    .stTextInput>div>div {
        background: rgba(255, 255, 255, 0.95) !important;
        border-radius: 12px !important;
        border: none !important;
    }
    .stTextInput input {
        color: #333 !important;
        font-size: 18px !important;
    }

    /* 按钮：高亮对比 */
    .stButton>button {
        background: white !important;
        color: #764ba2 !important;
        border-radius: 50px !important;
        padding: 10px 50px !important;
        font-size: 20px !important;
        font-weight: 700 !important;
        border: none !important;
        transition: 0.3s;
    }
    .stButton>button:hover {
        transform: scale(1.05);
        box-shadow: 0 8px 15px rgba(0,0,0,0.2) !important;
    }

    header {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# 3. 状态管理
if 'step' not in st.session_state:
    st.session_state.step = 1

# --- 逻辑渲染：核心方框开始 ---
st.markdown('<div class="glass-card">', unsafe_allow_html=True)

# 无论哪一步，这两行标题都会稳稳地待在方框顶部
st.markdown('<p class="inner-title-1">Happy 3.8 Day</p>', unsafe_allow_html=True)
st.markdown('<p class="inner-title-2">女神节 · 专属礼遇</p>', unsafe_allow_html=True)
st.markdown("<hr style='border: 0.5px solid rgba(255,255,255,0.2); margin-bottom: 30px;'>", unsafe_allow_html=True)

if st.session_state.step == 1:
    st.markdown('<p class="main-desc">Hi, 今天是几月几日？<br><span style="font-size:15px; opacity:0.8;">(请输入日期，如 3.8)</span></p>', unsafe_allow_html=True)
    q1 = st.text_input("Date", placeholder="在此输入", label_visibility="collapsed")
    if st.button("下一步"):
        if "3" in q1 and "8" in q1:
            st.session_state.step = 2
            st.rerun()
        else: st.error("日期似乎不对哦？")

elif st.session_state.step == 2:
    st.markdown('<p class="main-desc">让我猜猜，哪位女神<br>现在还在辛苦地加班？🤔</p>', unsafe_allow_html=True)
    q2 = st.text_input("Name", placeholder="输入名字", label_visibility="collapsed")
    if st.button("解锁心意"):
        if any(x in q2 for x in ["沈渊博", "我", "你自己"]):
            st.session_state.step = 3
            st.rerun()
        else: st.warning("名字输入有误，再确认一下？")

elif st.session_state.step == 3:
    st.snow()
    st.markdown('<p class="main-desc">“ 愿你所有的努力，<br>都有温暖的回响。 ”</p>', unsafe_allow_html=True)
    st.write("沈老师，加班辛苦啦。喝杯温水，稍微休息一下。☕")
    if st.button("继续"):
        st.session_state.step = 4
        st.rerun()

elif st.session_state.step == 4:
    st.balloons()
    st.markdown('<p class="main-desc">“ 3月8日，<br>愿你始终闪闪发光。 ”</p>', unsafe_allow_html=True)
    st.write("愿你做自己的女王，不卑不亢，温柔且坚强。🌹")
    if st.button("压轴惊喜"):
        st.session_state.step = 5
        st.rerun()

elif st.session_state.step == 5:
    st.toast("🎇 旗开得胜！", icon="💖")
    st.balloons()
    st.markdown('<p class="main-desc" style="font-weight:700; color:#ffeaa7; font-size:28px !important;">祝下周公开课，<br>旗开得胜，圆满成功！</p>', unsafe_allow_html=True)
    st.write("你专注的样子最有魅力。你是最棒的，我们都为你加油！💪")
    if st.button("重新回味"):
        st.session_state.step = 1
        st.rerun()

st.markdown('</div>', unsafe_allow_html=True) # 核心方框结束