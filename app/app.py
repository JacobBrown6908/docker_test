import os
import shutil
import pandas as pd
import streamlit as st


st.set_page_config(
    page_title="Bio-Mechanical",
    layout="wide"
)


home, ml, segmentation, appendix = st.tabs(
    [
        "Home",
        "Machine Learning",
        "Segmentation",
        "Appendix",
    ]
)


ml_files = ["C053L", "C054L", "6012", "6013", "6139", "6140", "6315", "6342R", "6344R"]
ml_locations_full = ["full_segmentation/Control/C053L","full_segmentation/Control/C054L","full_segmentation/Injured/6012","full_segmentation/Injured/6013","full_segmentation/Injured/6139","full_segmentation/Injured/6140","full_segmentation/Injured/6315","full_segmentation/Injured/6342R","full_segmentation/Injured/6344R"]
ml_locations_part = ["partial_segmentation/Control/C053L","partial_segmentation/Control/C054L","partial_segmentation/Injured/6012","partial_segmentation/Injured/6013","partial_segmentation/Injured/6139","partial_segmentation/Injured/6140","partial_segmentation/Injured/6315","partial_segmentation/Injured/6342R","partial_segmentation/Injured/6344R"]
ml_locations_mri = ["mri_slices/Control/C053L","mri_slices/Control/C054L","mri_slices/Injured/6012","mri_slices/Injured/6013","mri_slices/Injured/6139","mri_slices/Injured/6140","mri_slices/Injured/6315","mri_slices/Injured/6342R","mri_slices/Injured/6344R"]


seg_files = ["C052L", "6342L", "6127L", "6126L", "6342R", "6344R"]
seg_locations_full = ["full_segmentation/Control/C052L","full_segmentation/Control/6342L","full_segmentation/Injured/6127L","full_segmentation/Injured/6126L", "full_segmentation/Injured/6342R","full_segmentation/Injured/6344R"]
seg_locations_part = ["partial_segmentation/Control/C052L","partial_segmentation/Control/6342L","partial_segmentation/Injured/6127L","partial_segmentation/Injured/6126L","partial_segmentation/Injured/6342R","partial_segmentation/Injured/6344R"]
seg_locations_mri = ["mri_slices/Control/C052L","mri_slices/Control/6342L","mri_slices/Injured/6127L","mri_slices/Injured/6126L","mri_slices/Injured/6342R","mri_slices/Injured/6344R"]


with home:
    st.markdown("## **Home**")


with ml:
    st.markdown("## **Machine Learning**")



with segmentation:
    st.markdown("## **Segmentation**")



with appendix:
    st.markdwon("## **Appendix**")

st.write("### Partial Segmentation: Control (Non-Injured)")
st.picture("C:\Users\brown\OneDrive\Documents\DSS\Bio-Mechanical\DSS-Bio-Mechanical\app\partial_segmentation\Control\6342L\6342L_0.png")


st.write("### Partial Segmentation: Injured")
st.picture("C:\Users\brown\OneDrive\Documents\DSS\Bio-Mechanical\DSS-Bio-Mechanical\app\partial_segmentation\Injured\6342R\6342R_0.png")

