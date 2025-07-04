import streamlit as st
from backend import process_locid, process_mlocid, df, show_mirna_data, mlocid_error
from pages.footer_all import base_footer

def mirna_info_page():
    st.title("miRNA Search")
    st.write("**miRNA information**")
    col1, col2 = st.columns(2)
    with col1:
        c1 = st.container(border=True)
        tid = c1.text_input("Enter the Gene ID: ", placeholder="e.g., Ca_00001", key="mirna_Tid_input1").strip(); mtid = c1.text_input("Enter multiple Gene IDs: ", placeholder="e.g., Ca_00001, Ca_00002", key="mirna_mTid_input2").strip()
        if mtid:
            mtid_list = [item.strip() for item in mtid.replace(",", " ").split()]
            mtid_list = list(set(mtid_list))
            mtid = ",".join(mtid_list)
    with col2:
        c2 = st.container(border=True)
        locid = c2.text_input("Enter the NCBI ID: ", placeholder="e.g., LOC101511858", key="mirna_Locid_input1").strip()
        mlocid = c2.text_input("Enter multiple NCBI IDs: ", placeholder="e.g., LOC101511858, LOC101496413", key="mirna_mLocid_input2").strip()
        if mlocid:
            mlocid_list = [item.strip() for item in mlocid.replace(",", " ").split()]
            mlocid_list = list(set(mlocid_list))
            mlocid = ",".join(mlocid_list)
    cc1, cc2, cc3 = st.columns([2, 2, 2])
    with cc2:
        start_button = st.button("Search", use_container_width=True, key="mirna_Searchbutton1")

    if start_button:
        if tid:
            if 'Transcript id' in df.columns and 'lncRNA' in df.columns:
                matching_row = df[df['Transcript id'] == tid]
                if not matching_row.empty:
                    con = st.container(border=True)
                    with con:
                        st.subheader("miRNA data")
                        show_mirna_data(tid)
                else:
                    st.error(f"No match found for Gene ID: {tid}")
            st.toast("Task completed successfully.")
        elif mtid:
            mtid_list = [x.strip() for x in mtid.replace(",", " ").split()]
            mtid_list.sort()
            if 'Transcript id' in df.columns and 'lncRNA' in df.columns:
                matching_rows = df[df['Transcript id'].isin(mtid_list)]
                found_ids = matching_rows['Transcript id'].unique().tolist()
                not_found_ids = [x for x in mtid_list if x not in found_ids]
                if not matching_rows.empty:
                    con = st.container(border=True)
                    with con:
                        st.subheader("miRNA data")
                        show_mirna_data(mtid_list, is_multi=True)
                if not_found_ids:
                    st.error(f"No matches found for Gene IDs: {', '.join(not_found_ids)}")
            st.toast("Task completed successfully.")
        elif locid:
            tid = process_locid(locid)
            if 'Transcript id' in df.columns and 'lncRNA' in df.columns:
                matching_row = df[df['Transcript id'] == tid]
                if not matching_row.empty:
                    con = st.container(border=True)
                    with con:
                        st.subheader("miRNA data")
                        show_mirna_data(tid)
                else:
                    st.error(f"No match found for NCBI ID: {locid}")
            st.toast("Task completed successfully.")
        elif mlocid:
            available, rejected = mlocid_error(mlocid)
            if available:
                mtid = process_mlocid(",".join(available))
                mtid_list = [x.strip() for x in mtid.replace(",", " ").split()]
                mtid_list.sort()
                if 'Transcript id' in df.columns and 'lncRNA' in df.columns:
                    matching_rows = df[df['Transcript id'].isin(mtid_list)]
                    if not matching_rows.empty:
                        con = st.container(border=True)
                        with con:
                            st.subheader("miRNA data")
                            show_mirna_data(mtid_list, is_multi=True)
                st.toast("Task completed successfully.")
            if rejected:
                st.error(f"No matches found for NCBI IDs: {', '.join(rejected)}")
        
        else:
            st.warning("Need either a Gene ID or NCBI ID to proceed.")
    elif tid == "":
        st.warning("Need Gene ID to proceed.")
    else:
        st.write("Press the 'Search' button to begin ...")
        st.write("Follow the instructions or check out tutorials")

    base_footer()

if __name__ == "__main__":
    mirna_info_page()
