import streamlit as st
from load_css import local_css

st.set_page_config(layout="wide", page_title="JCE", page_icon="https://plus.jakarta.go.id/media/arti-logo-1.svg")
st.title("Jakarta Coastal Embankment 🌊")
local_css("style.css")

col1, col2, col3, col4 = st.columns(4)
col1.metric(label = "Built", value = '10.2 km', delta = "29.14%")
col2.metric("Protects", "1.85 Million")
col3.metric("Coastal Flooding Height", "20-50 cm")
col4.metric("AVG Land Subsidence", "7.5-14 cm/year")

map1, map2, map3 = st.columns(3)
map1.markdown("""
   <iframe width="640" height="480" src="https://www.google.com/maps/d/u/0/embed?mid=1qavyDenBsua_WhonEvvjc1Dc8b3mdGM&ehbc=2E312F" frameborder="0"></iframe>
    """, unsafe_allow_html=True)
map3.subheader('Embankment and Land Subsidence')
map3.text('Map visualization of embankments that is pl')
map3.text('anned and has been built. Rate of land subs')
map3.text('idence prediction of Jakarta regencies in ')
map3.text('the year 2025')
map3.caption('Source: Dr. Heri Andreas (FITB, ITB) and NCICD Jakarta')
map3.text('')
map3.text('Description:')
t = "<div><span class='highlight blue'>≥ 2 m</span> </span> <span class='highlight red'>1.9 m - 1.1 m</span> </span> <span class='highlight yel'>1 m ≥ </span></div>"
map3.markdown(t, unsafe_allow_html=True)
map3.text('')
map3.caption('Land Susidence')
x = "<div><span class='highlight kol'>Planned</span> </span> <span class='highlight lol'>Built</span></div>"
map3.markdown(x, unsafe_allow_html=True)
map3.text('')
map3.caption('Embankment')

st.text('')
st.text('')
st.markdown("<h2 style='text-align: center; color: white;'>Flood and Tap Water Coverage</h2>", unsafe_allow_html=True)
st.text('')
st.markdown("""
    <iframe width="100%" height="850" src="https://datastudio.google.com/embed/reporting/7eb9d03a-2236-45bb-bf9c-ad70e0ac0cc8" frameborder="0" style="border:0" allowfullscreen></iframe>
    """, unsafe_allow_html=True)

st.text('')
st.text('')
st.markdown("<h4 style='text-align: center; color: white;'>Capstone Project for:</h4>", unsafe_allow_html=True)
st.text('')
st.text('')
img1, img2 = st.columns(2)
img1.image('logo (1).png', width=362)
img2.image('gengigih-homepage-footer-logo.png',width=362)
st.text('')
st.text('')
st.caption("*This dashboard is made by DA_DM11 for Generasi Gigih's team capstone project discussing Coastal Embankment in Jakarta. Any affiliation with organizations in this web is only for media purpose and doesn't represent their views")
