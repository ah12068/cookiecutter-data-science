import streamlit as st
import pickle

# Text/Title
st.title("Streamlit Tutorials")

# SIDEBARS
st.sidebar.header("About")
st.sidebar.text("This is Streamlit Tut")

# Header/Subheader
st.header("This is a header")
st.subheader("This is a subheader")

# Text
st.text("Hello Streamlit")

# Markdown
st.markdown("### This is a Markdown")

st.success("Successful")

st.info("Information!")

st.warning("This is a warning")

st.error("This is an error Danger")

st.exception("NameError('name three not defined')")

# Checkbox
if st.checkbox("Show/Hide"):
	st.text("Showing or Hiding Widget")


# Radio Buttons
status = st.radio("What is your status",("Active","Inactive"))

if status == 'Active':
	st.success("You are Active")
else:
	st.warning("Inactive, Activate")

# SelectBox
occupation = st.selectbox("Your Occupation",["Programmer","DataScientist","Doctor","Businessman"])
st.write("You selected this option ",occupation)


# MultiSelect
location = st.multiselect("Where do you work?",("London","New York","Accra","Kiev","Nepal"))
st.write("You selected",len(location),"locations")

# Slider
level = st.slider("What is your level",1,5)


# Buttons
st.button("Simple Button")

if st.button("About"):
	st.text("Streamlit is Cool")

# Receiving User Text Input
firstname = st.text_input("Enter Your Firstname","Type Here..")
if st.button("Submit"):
	result = firstname.title()
	st.success(result)


# Text Area
message = st.text_area("Enter Your message","Type Here..")
if st.button("Submit"):
	result = message.title()
	st.success(result)

# Date Input
import datetime
today = st.date_input("Today is",datetime.datetime.now())

# Time
the_time = st.time_input("The time is",datetime.time())

# Progress Bar
import time
my_bar = st.progress(0)
for p in range(10):
    my_bar.progress(p + 1)


# Spinner
with st.spinner("Waiting .."):
     time.sleep(5)
     st.success("Finished!")


# Balloons
st.balloons()
