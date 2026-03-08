import streamlit as st
import time

# 1. 页面配置
st.set_page_config(page_title="Special Gift", page_icon="🎁", layout="centered")

# 2. 深度定制 UI (解决字体大小、对比度、渐变高级感)
st.markdown("""
    <style>
    /* 引入更高级的思源黑体 */
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@400;700&display=swap');

    /* 极光动态背景：使用更深邃、更有质感的配色 */
    .stApp {
        background: linear-gradient(125deg, #6a11cb 0%, #2575fc 50%, #ff0844 100%);
        background-size: 400% 400%;
        animation: gradientBG 15s ease infinite;
    }
    @keyframes gradientBG {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    /* 贺卡容器：增强对比度，解决白字看不清问题 */
    .glass-card {
        background: rgba(255, 255, 255, 0.15);
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        border-radius: 28px;
        border: 1px solid rgba(255, 255, 255, 0.3);
        padding: 45px 30px;
        box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);
        text-align: center;
        animation: slideUp 1s cubic-bezier(0.16, 1, 0.3, 1);
    }
    @keyframes slideUp {
        from { opacity: 0; transform: translateY(40px); }
        to { opacity: 1; transform: translateY(0); }
    }

    /* 字体调整：加大加粗，增强可读性 */
    .title-text {
        font-size: 42px !important;
        font-weight: 700;
        color: #ffffff;
        margin-bottom: 15px;
        letter-spacing: 2px;
    }
    .main-desc {
        font-size: 24px !important; /* 加大字体 */
        color: #ffffff;
        line-height: 1.6;
        margin-bottom: 35px;
        font-family: 'Noto Sans SC', sans-serif;
    }

    /* 输入框优化：解决输入文字看不清的问题 */
    .stTextInput>div>div>input {
        background: rgba(255, 255, 255, 0.9) !important; /* 浅白色背景 */
        color: #1a1a1a !important; /* 深色文字，确保清晰 */
        font-size: 18px !important;
        height: 50px !important;
        border-radius: 12px !important;
        border: 2px solid transparent !important;
    }
    .stTextInput>div>div>input:focus {
        border: 2px solid #ff0844 !important;
    }

    /* 按钮优化 */
    .stButton>button {
        background: linear-gradient(90deg, #ff0844 0%, #ffb199 100%) !important;
        color: white !important;
        border: none !important;
        padding: 12px 40px !important;
        font-size: 20px !important;
        border-radius: 30px !important;
        font-weight: 700 !important;
        box-shadow: 0 10px 20px rgba(255, 8, 68, 0.3) !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. 状态管理
if 'step' not in st.session_state:
    st.session_state.step = 1

# --- 关卡逻辑 ---

if st.session_state.step == 1:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown('<p class="title-text">Step 01</p>', unsafe_allow_html=True)
    st.markdown('<p class="main-desc">Hi, 今天是几月几日？<br><small style="font-size:14px; opacity:0.8;">(请输入日期，如 3.8)</small></p>', unsafe_allow_html=True)
    q1 = st.text_input("DateInput", placeholder="在此输入...", label_visibility="collapsed")
    if st.button("下一步 →"):
        if "3" in q1 and "8" in q1:
            st.session_state.step = 2
            st.rerun()
        else: st.error("日期似乎不对哦，再想一想？")
    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.step == 2:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown('<p class="title-text">Step 02</p>', unsafe_allow_html=True)
    st.markdown('<p class="main-desc">让我猜猜，哪位女神<br>现在还在辛苦地加班？🤔</p>', unsafe_allow_html=True)
    q2 = st.text_input("NameInput", placeholder="输入那个人的名字", label_visibility="collapsed")
    if st.button("锁定目标"):
        if any(x in q2 for x in ["沈渊博", "我", "你自己"]):
            st.session_state.step = 3
            st.rerun()
        else: st.warning("答案不在库中，再试一次？")
    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.step == 3:
    st.snow() # 意境雪花
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown('<p class="title-text">Phase 01</p>', unsafe_allow_html=True)
    st.markdown('<p class="main-desc">“ 愿你所有的努力，<br>都有温暖的回响。 ”</p>', unsafe_allow_html=True)
    st.write("---")
    st.markdown("<p style='color:white; font-size:18px;'>沈老师，加班辛苦啦。<br>喝杯温水，奖励自己一下吧。🍵</p>", unsafe_allow_html=True)
    if st.button("继续开启惊喜"):
        st.session_state.step = 4
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.step == 4:
    st.balloons() # 气球
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown('<p class="title-text">Phase 02</p>', unsafe_allow_html=True)
    st.markdown('<p class="main-desc">“ 3月8日，<br>愿你始终闪闪发光。 ”</p>', unsafe_allow_html=True)
    st.write("---")
    st.markdown("<p style='color:white; font-size:18px;'>在这个属于你的日子里，<br>你就是全宇宙最耀眼的存在。🌹</p>", unsafe_allow_html=True)
    if st.button("查看最终心愿"):
        st.session_state.step = 5
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.step == 5:
    # 模拟“爱心雨+烟花”组合效果
    st.toast("🎇 旗开得胜！", icon="💖")
    st.toast("🚀 圆满成功！", icon="🔥")
    st.balloons()
    
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown('<p class="title-text">Best Wish</p>', unsafe_allow_html=True)
    st.markdown('<p class="main-desc" style="font-weight:700; color:#ffda79;">“ 祝下周公开课，<br>旗开得胜，圆满成功！ ”</p>', unsafe_allow_html=True)
    st.write("---")
    st.markdown("<p style='color:white; font-size:20px;'>自信的你最迷人。<br>你是最棒的，加油！加油！！加油！！！💪</p>", unsafe_allow_html=True)
    if st.button("回味一下"):
        st.session_state.step = 1
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)