import streamlit as st
from backend import process_locid, process_mlocid,df, show_cellular_localisation
from pages.footer_all import base_footer

def local_info_page():
    st.title("Cellular Localisation Search")
    st.write("**cell local data information**")
    col1, col2 = st.columns(2)

    with col1:
        con1 = st.container(border=True)
        tid = con1.text_input("Enter the Gene ID: ", placeholder="e.g., Ca_00001", key="local_Tid_input1").strip()
        mtid = con1.text_input("Enter multiple Gene IDs: ", placeholder="e.g., Ca_00001, Ca_00002", key="local_mTid_input2").strip()
        if mtid:
            mtid_list = [item.strip() for item in mtid.replace(",", " ").split()]
            mtid_list = list(set(mtid_list))
            mtid = ",".join(mtid_list)

    with col2:
        con2 = st.container(border=True)
        locid = con2.text_input("Enter the NCBI ID: ", placeholder="e.g., LOC101511858", key="local_Locid_input1").strip()
        mlocid = con2.text_input("Enter multiple NCBI IDs: ", placeholder="e.g., LOC101511858, LOC101496413", key="local_mLocid_input2").strip()
        if mlocid:
            mlocid_list = [item.strip() for item in mlocid.replace(",", " ").split()]
            mlocid_list = list(set(mlocid_list))
            mlocid = ",".join(mlocid_list)

    con1, con2, con3 = st.columns([2, 2, 2])
    with con2:
        start_button = st.button("Search", use_container_width=True, key="local_Searchbutton1")

    if start_button:
        if tid:
            if 'Transcript id' in df.columns and 'lncRNA' in df.columns:
                matching_row = df[df['Transcript id'] == tid]

                if not matching_row.empty:
                    con=st.container(border=True)
                    with con:
                        st.subheader("Cellular Localisation data")
                        show_cellular_localisation(tid)

            st.toast("Task completed successfully.")
            
        elif mtid:
            mtid_list = [tid.strip() for tid in mtid.replace(",", " ").split()]
            mtid_list.sort()
            if 'Transcript id' in df.columns and 'lncRNA' in df.columns:
                matching_rows = df[df['Transcript id'].isin(mtid_list)]
                if not matching_rows.empty:
                    con=st.container(border=True)
                    with con:
                        st.subheader("Cellular Localisation data")
                        show_cellular_localisation(mtid_list, is_multi=True)

            st.toast("Task completed successfully.")
            
        elif locid:
            tid = process_locid(locid)
            if 'Transcript id' in df.columns and 'lncRNA' in df.columns:
                matching_row = df[df['Transcript id'] == tid]

                if not matching_row.empty:
                    con=st.container(border=True)
                    with con:
                        st.subheader("Cellular Localisation data")
                        show_cellular_localisation(tid)
            
            st.toast("Task completed successfully.")
            
        elif mlocid:
            mtid = process_mlocid(mlocid)
            mtid_list = [tid.strip() for tid in mtid.replace(",", " ").split()]
            mtid_list.sort()
            if 'Transcript id' in df.columns and 'lncRNA' in df.columns:
                matching_rows = df[df['Transcript id'].isin(mtid_list)]
                if not matching_rows.empty:
                    con=st.container(border=True)
                    with con:
                        st.subheader("Cellular Localisation data")
                        show_cellular_localisation(mtid_list, is_multi=True)

            st.toast("Task completed successfully.")
            
        else:
            st.warning("Need either a Gene ID or NCBI ID to proceed.")
            
    elif tid == "":
        st.warning("Need Gene ID/ NCBI ID to proceed.")
    else:
        st.write("Press the 'Search' button to begin ...")
        st.write("Follow the instructions or check out tutorials")

    base_footer()

if __name__ == "__main__":
    local_info_page()
