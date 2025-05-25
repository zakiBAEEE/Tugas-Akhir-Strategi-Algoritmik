import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import time
from utils.metrics import format_rupiah 

from utils.data_loader import load_dataset, filter_by_niche, prepare_knapsack_data
from algorithms.greedy import greedy_knapsack
from algorithms.dynamic_programming import dp_knapsack
from utils.metrics import compute_metrics

st.set_page_config(page_title="Influencer Optimization App", layout="centered")
st.title("📱 Aplikasi Pemilihan Influencer Optimal")

platform = st.selectbox("Pilih Platform:", ["Instagram", "Threads"])

df = load_dataset(platform)
niche_options = sorted(df['TOPIC_CATEGORY'].dropna().unique())
niche = st.selectbox("Pilih Niche Konten:", niche_options)

min_budget = df['ESTIMATED_COST'].min()
min_budget_label = f"Masukkan Budget - Minimal: Rp{min_budget:,.0f}".replace(",", ".")

budget = st.number_input(min_budget_label, min_value=0)

compare_mode = st.checkbox("Bandingkan Semua Algoritma")

if not compare_mode:
    algorithm = st.radio("Pilih Algoritma:", ["Greedy", "Dynamic Programming"])

if st.button("Jalankan Optimasi"):
    df_filtered = filter_by_niche(df, niche)
    values, costs = prepare_knapsack_data(df_filtered)

    if compare_mode:
        # Mode perbandingan semua algoritma
        algorithms = {
            "Greedy": greedy_knapsack,
            "Dynamic Programming": dp_knapsack,
        }

        results = []
        influencer_results = {}

        for name, func in algorithms.items():
            start_time = time.time()
            selected = func(costs, values, budget)
            end_time = time.time()

            metrics = compute_metrics(selected, costs, values, start_time, end_time)

            results.append({
                "Algoritma": name,
                "Total Engagement": metrics["total_value"],
                "Total Biaya (IDR)": metrics["total_cost"],
                "Waktu Eksekusi (s)": round(metrics["duration"], 5)
            })

            influencer_results[name] = df_filtered.iloc[selected][['NAME', 'TOPIC_CATEGORY', 'ESTIMATED_COST', 'BENEFIT_SCORE']]

        df_result = pd.DataFrame(results)

        st.subheader("📊 Perbandingan Algoritma")
        st.dataframe(df_result)

        st.subheader("📈 Visualisasi Performa Algoritma")

        metrik_list = ["Total Engagement", "Total Biaya (IDR)", "Waktu Eksekusi (s)"]
        warna = ['#1f77b4', '#ff7f0e', '#2ca02c']

        for i, metrik in enumerate(metrik_list):
            st.markdown(f"#### {metrik}")
            fig, ax = plt.subplots(figsize=(8, 4))
            df_result.plot(kind='bar', x='Algoritma', y=metrik, ax=ax, color=warna[i])
            ax.set_ylabel(metrik)
            ax.set_xlabel("Algoritma")
            ax.set_title(f"Perbandingan {metrik}")
            st.pyplot(fig)


        st.subheader("📋 Influencer Terpilih per Algoritma")
        for algo, df_sel in influencer_results.items():
            st.markdown(f"### {algo}")
            if df_sel.empty:
                st.warning("Tidak ada influencer yang dipilih.")
            else:
                st.dataframe(df_sel)

    else:
        start_time = time.time()
        if algorithm == "Greedy":
            selected = greedy_knapsack(costs, values, budget)
        elif algorithm == "Dynamic Programming":
            selected = dp_knapsack(costs, values, budget)
        end_time = time.time()

        df_result = df_filtered.iloc[selected][['NAME', 'TOPIC_CATEGORY', 'ESTIMATED_COST', 'BENEFIT_SCORE']]
        st.subheader("📋 Influencer Terpilih")
        if df_result.empty:
            st.warning("Tidak ada influencer yang dipilih.")
        else:
            st.dataframe(df_result)

        metrics = compute_metrics(selected, costs, values, start_time, end_time)
        st.subheader("📊 Statistik")
        st.metric("Total Engagement", f"{metrics['total_value']:.0f}")
        st.metric("Total Biaya (IDR)", format_rupiah(metrics['total_cost']))
        st.metric("Waktu Eksekusi (detik)", f"{metrics['duration']:.4f}")

st.markdown("---")
st.caption("Aplikasi ini dikembangkan untuk membandingkan kinerja berbagai algoritma dalam memilih influencer terbaik berdasarkan batasan pengguna.")
