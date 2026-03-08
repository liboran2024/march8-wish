import streamlit as st
import time

# 页面配置
st.set_page_config(page_title="3.8 专属动态贺卡", page_icon="💌", layout="centered")

# --- 核心 UI 样式（贺卡化 & 动态爱心背景） ---
st.markdown("""
    <style>
    /* 全局背景：动态渐变 */
    .stApp {
        background: linear-gradient(-45deg, #ff9a9e, #fad0c4, #fad0c9, #ffdde1);
        background-size: 400% 400%;
        animation: gradient 15s ease infinite;
    }
    @keyframes gradient {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    /* 贺卡容器样式 */
    .card {
        background: rgba(255, 255, 255, 0.9);
        border-radius: 30px;
        padding: 40px;
        box-shadow: 0 20px 40px rgba(0,0,0,0.1);
        border: 2px solid #fff;
        text-align: center;
        transition: transform 0.3s ease;
        animation: float 3s ease-in-out infinite;
    }
    @keyframes float {
        0% { transform: translateY(0px); }
        50% { transform: translateY(-10px); }
        100% { transform: translateY(0px); }
    }

    /* 按钮美化 */
    .stButton>button {
        background: linear-gradient(90deg, #ff758c 0%, #ff7eb3 100%);
        color: white !important;
        border-radius: 50px !important;
        border: none !important;
        padding: 10px 30px !important;
        font-size: 18px !important;
        font-weight: bold !important;
        box-shadow: 0 4px 15px rgba(255, 117, 140, 0.4);
    }
    </style>
    
    <div style="position: fixed; top: 0; left: 0; width: 100%; height: 100%; pointer-events: none; z-index: 0;">
        <marquee direction="down" scrollamount="5" style="height: 100%; width: 100%; opacity: 0.3;">
            <span style="font-size: 30px; margin-left: 10%;">❤️</span>
            <span style="font-size: 20px; margin-left: 20%;">🌸</span>
            <span style="font-size: 40px; margin-left: 50%;">✨</span>
            <span style="font-size: 25px; margin-left: 80%;">❤️</span>
        </marquee>
    </div>
    """, unsafe_allow_html=True)

# --- 逻辑控制 ---
if 'stage' not in st.session_state:
    st.session_state.stage = 'q1'

# 关卡显示函数
def show_card(content_type):
    st.markdown('<div class="card">', unsafe_allow_html=True)
    if content_type == 'q1':
        st.markdown("<h3>🕵️ 身份验证 (1/2)</h3>", unsafe_allow_html=True)
        date_ans = st.text_input("今天是几月几日？", placeholder="例如：308")
        if st.button("下一步"):
            if "3" in date_ans and "8" in date_ans:
                st.session_state.stage = 'q2'
                st.rerun()
            else: st.warning("记错日期的后果很严重哦~")
            
    elif content_type == 'q2':
        st.markdown("<h3>🤔 身份验证 (2/2)</h3>", unsafe_allow_html=True)
        st.write("让我猜猜，哪位小仙女现在还在辛勤加班？")
        name_ans = st.text_input("输入Ta的名字：", placeholder="提示：沈...")
        if st.button("解锁贺卡"):
            if "沈渊博" in name_ans or "我" in name_ans:
                st.session_state.stage = 'wish'
                st.rerun()
            else: st.warning("名字不对，礼物不给！")

    elif content_type == 'wish':
        st.balloons()
        st.markdown("<h2 style='color: #ff4b6b;'>💝 专属贺卡 💝</h2>", unsafe_allow_html=True)
        
        # 第一层：工作祝福
        st.markdown("""
            <p style='font-size: 18px; color: #666;'><b>Phase 1: 能量补给站</b><br>
            亲爱的沈老师，工作辛苦啦！<br>
            愿你的所有努力都有回响，加班的时光也能被温柔治愈。</p>
            <hr style='border: 0.5px solid #eee'>
        """, unsafe_allow_html=True)
        
        # 第二层：节日祝福
        st.markdown("""
            <p style='font-size: 20px; color: #d63384;'><b>Phase 2: 女神节快乐</b><br>
            3月8日，愿你眼里有星辰，生活有甜头。<br>
            在这个属于你的日子里，要做最快乐的小朋友！</p>
            <hr style='border: 0.5px solid #eee'>
        """, unsafe_allow_html=True)
        
        # 第三层：公开课祝福
        st.markdown("""
            <p style='font-size: 22px; color: #ff758c; font-weight: bold;'><b>Phase 3: 必胜锦囊</b><br>
            最最重要的是——祝下周公开课顺利！<br>
            你专注的样子最迷人，一定能大获成功！🚀</p>
        """, unsafe_allow_html=True)
        
        if st.button("重新感受浪漫"):
            st.session_state.stage = 'q1'
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# 执行显示
show_card(st.session_state.stage)