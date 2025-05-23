import streamlit as st

# Header
st.set_page_config(page_title="Influencer Optimization App", layout="centered")
st.title("Aplikasi Pemilihan Influencer Optimal")

# Platform Selection
platform = st.selectbox("Pilih Platform:", [
    "Instagram", "YouTube", "TikTok", "Threads"
])

# Niche Selection
niche = st.selectbox("Pilih Niche Konten:", [
    "Fashion", "Teknologi", "Kesehatan & Fitness", "Gaming", "Kuliner"
])

# Budget Input
budget = st.number_input("Masukkan Budget Maksimal (USD):", min_value=0)

# Algorithm Selection
algorithm = st.radio("Pilih Algoritma:", [
    "Greedy", "Dynamic Programming", "Backtracking"
])

# Button to run optimization
if st.button("Jalankan Optimasi"):
    st.info("Hasil optimasi akan ditampilkan di sini setelah backend dihubungkan.")
    # Placeholder untuk hasil nanti
    st.write("\n\n---")
    st.subheader("Influencer Terpilih")
    st.write("(Tabel influencer akan muncul di sini)")

    st.subheader("Statistik")
    st.metric("Total Engagement", "-")
    st.metric("Total Biaya", "-")
    st.metric("Waktu Eksekusi", "-")

# Footer
st.markdown("\n\n---")
st.caption("Aplikasi ini dikembangkan untuk membandingkan kinerja berbagai algoritma dalam memilih influencer terbaik berdasarkan batasan pengguna.")
