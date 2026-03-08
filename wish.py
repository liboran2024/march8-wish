import streamlit as st
import time

# 1. 页面配置
st.set_page_config(page_title="Special Message", page_icon="🤍", layout="centered")

# 2. 极其稳健的 CSS (确保不崩页面)
st.markdown("""
    <style>
    /* 强行设置背景色和文字颜色，防止黑夜模式干扰 */
    .stApp {
        background-color: #FFFFFF !important;
    }
    .content-frame {
        text-align: center;
        padding: 40px 10px;
        color: #3c4043;
    }
    .main-text {
        font-size: 26px;
        font-weight: 500;
        margin-bottom: 30px;
        line-height: 1.5;
        font-family: "PingFang SC", "Microsoft YaHei", sans-serif;
    }
    .sub-text {
        font-size: 14px;
        color: #70757a;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-bottom: 10px;
    }
    /* 谷歌蓝按钮 */
    .stButton>button {
        background-color: #1a73e8 !important;
        color: white !important;
        border-radius: 20px !important;
        border: none !important;
        padding: 8px 30px !important;
        font-weight: 500 !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. 状态管理
if 'step' not in st.session_state:
    st.session_state.step = 'q1'

# --- 关卡逻辑 ---

if st.session_state.step == 'q1':
    st.markdown('<div class="content-frame"><p class="sub-text">Step 01</p><p class="main-text">Hi, 今天是几月几日？</p></div>', unsafe_allow_html=True)
    ans1 = st.text_input("Date", placeholder="例如: 3.8", label_visibility="collapsed")
    if st.button("继续"):
        if "3" in ans1 and "8" in ans1:
            st.session_state.step = 'q2'
            st.rerun()
        else:
            st.error("日期不对哦，再想想？")

elif st.session_state.step == 'q2':
    st.markdown('<div class="content-frame"><p class="sub-text">Step 02</p><p class="main-text">让我猜猜，谁还在辛苦加班？</p></div>', unsafe_allow_html=True)
    ans2 = st.text_input("Name", placeholder="请输入名字", label_visibility="collapsed")
    if st.button("揭晓答案"):
        if "沈渊博" in ans2 or "我" in ans2:
            st.session_state.step = 'wish1'
            st.rerun()
        else:
            st.warning("这位同学似乎不在加班名单上呢...")

elif st.session_state.step == 'wish1':
    st.markdown('<div class="content-frame"><p class="sub-text">Phase 01 / 03</p><p class="main-text">“愿你所有的努力，<br>都有温暖的回响。”</p></div>', unsafe_allow_html=True)
    st.write("沈老师，加班辛苦了。喝杯水，放松一下吧。")
    if st.button("Next →"):
        st.session_state.step = 'wish2'
        st.rerun()

elif st.session_state.step == 'wish2':
    st.markdown('<div class="content-frame"><p class="sub-text">Phase 02 / 03</p><p class="main-text">“3月8日，<br>愿你始终闪闪发光。”</p></div>', unsafe_allow_html=True)
    st.write("每一天，你都拥有选择的自由，和热爱生活的勇气。")
    if st.button("Next →"):
        st.session_state.step = 'wish3'
        st.rerun()

elif st.session_state.step == 'wish3':
    st.balloons()
    st.markdown('<div class="content-frame"><p class="sub-text">Final</p><p class="main-text" style="color:#1a73e8;">“祝下周公开课，<br>旗开得胜，圆满成功！”</p></div>', unsafe_allow_html=True)
    st.write("自信的你最迷人，加油！")
    if st.button("Back"):
        st.session_state.step = 'q1'
        st.rerun()