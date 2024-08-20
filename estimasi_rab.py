import streamlit as st

def show_estimasi_rab():
    st.header("Rekapitulasi dan Estimasi Akhir RAB")

    # Display the summary of the data input by the user
    st.subheader("Ringkasan Proyek")
    st.write("Berikut adalah ringkasan data yang telah Anda input:")

    # Placeholder for actual data summary
    st.write("Jalan Paving, Jalan Beton, Jalan Makadam, Saluran Drainase")

    st.markdown("---")

    # Export options
    st.subheader("Ekspor Data")
    if st.button("Ekspor ke Excel"):
        st.write("Data diekspor ke Excel.")
        # Placeholder for actual export code

    if st.button("Konfirmasi dan Selesai"):
        st.success("RAB telah berhasil direkapitulasi dan selesai.")
        st.balloons()
