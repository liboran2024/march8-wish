import streamlit as st
import time

# 1. 页面基础配置 (Google Style: Clean & Spacious)
st.set_page_config(page_title="A Special Message", page_icon="🤍", layout="centered")

# 2. 注入 Google Material Design 风格 CSS
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Google+Sans:wght@400;500;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Google Sans', sans-serif;
    }
    
    .stApp {
        background-color: #FFFFFF;
        transition: background-color 0.8s ease;
    }

    /* 渐进式内容卡片 */
    .content-frame {
        text-align: center;
        padding: 50px 20px;
        animation: fadeIn 1.2s ease-in-out;
    }

    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }

    /* 谷歌风按钮：扁平化、高圆角 */
    .stButton>button {
        background-color: #1a73e8;
        color: white !important;
        border-radius: 24px !important;
        padding: 10px 32px !important;
        border: none !important;
        font-weight: 500 !important;
        letter-spacing: 0.25px !important;
        box-shadow: 0 1px 3px rgba(60,64,67,0.3), 0 4px 8px rgba(60,64,67,0.15);
    }
    
    .stButton>button:hover {
        background-color: #1765cc;
        box-shadow: 0 1px 3px rgba(60,64,67,0.3), 0 4px 8px rgba(60,64,67,0.3);
    }

    /* 文本渐进样式 */
    .main-text {
        font-size: 28px;
        color: #3c4043;
        line-height: 1.6;
        margin-bottom: 40px;
    }
    .sub-text {
        font-size: 16px;
        color: #70757a;
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. 状态管理 (控制流程：q1 -> q2 -> wish1 -> wish2 -> wish3)
if 'step' not in st.session_state:
    st.session_state.step = 'q1'

def next_step():
    # 模拟平滑切换感
    placeholder = st.empty