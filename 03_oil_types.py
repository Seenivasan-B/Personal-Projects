import streamlit as st

# Adding the titles and definition 
st.title("Type of Oil Reservoir")
st.text("Finding the type of oil reservoir based on API gravity(API), Gas-Oil ratio(GOR) and\nOil formation volume factor(Bo).")
st.markdown("---")

# Gathering the inputs
API = st.number_input(label='**API** - Enter the value of API gravity ' + ' (Degrees)',step=1.,format='%.0f')
GOR = st.number_input(label='**GOR** - Enter the value of Gas Oil Ratio '+ ' (scf/stb)',step=100.,format='%.0f')
BO = st.number_input(label='**Bo** - Enter the value of Oil Formation Volume Factor ' + ' (bbl/stb)',step=.1,format='%.1f')

# Running the caculation and storing the output
def oil_type():
    if 15<API<40 and 200<=GOR<=700 and 1.2<=BO<= 1.5:
        return "Ordinary Black Oil"
    elif 0<API<35 and 0<=GOR<=200 and 1<=BO<=1.2:
        return "Heavy Oil"
    elif 45<API<55 and 2000<=GOR<=3200 and 1<=BO <2:
        return "Volatile Oil"
    elif 60>API>50 and 10000>=GOR>=3000 and BO>2:
        return "Near Critical Oil"
    else:
        return "Unable to determine the type of oil Reservoir verify input values"

st.markdown("---")

# Viewing the output and the corresponding image 

col1, col2 = st.columns([1,1],gap='medium')

with col1:
    st.subheader('The type of oil reservoir is ')
    st.subheader(oil_type())

with col2:
    if oil_type() == "Ordinary Black Oil":
        st.image(r"C:\Users\seeni\Downloads\Black oil.png",caption = oil_type())
    elif oil_type() == "Heavy Oil":
        st.image(r"C:\Users\seeni\Downloads\Low shrinkage.png",caption = oil_type())
    elif oil_type() == "Volatile Oil":
        st.image(r"C:\Users\seeni\Downloads\volatile oil.png",caption = oil_type())
    elif oil_type() == "Near Critical Oil":
        st.image(r"C:\Users\seeni\Downloads\near critical.png",caption = oil_type())
    else :
        None
st.markdown("---")    
