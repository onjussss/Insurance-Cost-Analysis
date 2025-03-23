import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# ---- Function 1: Scatter Plot (Charges vs Age by Smoker Status) ----
def graph1(df):
    colors = {'yes': 'red', 'no': 'blue'}
    
    fig, ax = plt.subplots(figsize=(12, 7))
    
    for smoker_status in df['smoker'].unique():
        subset = df[df['smoker'] == smoker_status]
        ax.scatter(subset['age'], subset['charges'], 
                   c=colors[smoker_status], label=f'Smoker: {smoker_status}', 
                   alpha=0.7, s=80, edgecolors='black')

    ax.set_xlabel("Age", fontsize=14, fontweight='bold')
    ax.set_ylabel("Charges", fontsize=14, fontweight='bold')
    ax.set_title("Scatter Plot: Charges vs. Age (by Smoker Status)", fontsize=16, fontweight='bold')
    ax.legend(fontsize=12, edgecolor='black')
    ax.grid(True, linestyle='--', alpha=0.6)

    st.pyplot(fig)  # ✅ Display in Streamlit

# ---- Function 2: Box Plot (Charges by Region) ----
def graph2(df):
    region_colors = {
        "southeast": "#FF9999",
        "southwest": "#66B2FF",
        "northeast": "#99FF99",
        "northwest": "#FFCC99"
    }

    regions = df["region"].unique()
    data = [df[df["region"] == region]["charges"] for region in regions]

    fig, ax = plt.subplots(figsize=(10, 6))
    box = ax.boxplot(
        data, labels=regions, notch=True, patch_artist=True, 
        showfliers=True, medianprops={'color': 'black', 'linewidth': 2}
    )

    for patch, color in zip(box["boxes"], region_colors.values()):
        patch.set_facecolor(color)

    for i, region in enumerate(regions):
        mean_value = df[df["region"] == region]["charges"].mean()
        ax.scatter(i + 1, mean_value, color="black", marker="o", s=70, label="Mean" if i == 0 else "")

    ax.set_xlabel("Region", fontsize=14, fontweight="bold")
    ax.set_ylabel("Charges", fontsize=14, fontweight="bold")
    ax.set_title("Box Plot: Insurance Charges by Region", fontsize=14, fontweight="bold")
    ax.grid(axis="y", linestyle="--", alpha=0.7)
    ax.legend()

    st.pyplot(fig)  # ✅ Display in Streamlit

# ---- Function 3: Bar Chart (Average Charges by Smoker & Sex) ----
def graph3(df):
    grouped_data = df.groupby(["smoker", "sex"])["charges"].mean().reset_index()
    smoker_statuses = grouped_data["smoker"].unique()
    sexes = grouped_data["sex"].unique()

    bar_width = 0.4
    x = np.arange(len(smoker_statuses))

    fig, ax = plt.subplots(figsize=(8, 6))
    colors = {"male": "#4C72B0", "female": "#DD8452"}

    for i, sex in enumerate(sexes):
        means = grouped_data[grouped_data["sex"] == sex]["charges"]
        ax.bar(x + i * bar_width, means, bar_width, label=sex.capitalize(), 
               color=colors[sex], alpha=0.85, linewidth=0.8, edgecolor="black")

        for j, mean in enumerate(means):
            ax.text(x[j] + i * bar_width, mean + 1500, f"{mean:.0f}", 
                    ha="center", fontsize=10, fontweight="bold", color="black")

    ax.set_xlabel("Smoker Status", fontsize=12, fontweight='bold')
    ax.set_ylabel("Average Charges", fontsize=12, fontweight='bold')
    ax.set_title("Average Insurance Charges by Smoker Status & Sex", fontsize=14, fontweight='bold')
    ax.set_xticks(x + bar_width / 2)
    ax.set_xticklabels(["Non-Smoker", "Smoker"], fontsize=11)
    ax.legend(title="Sex", fontsize=11)
    ax.grid(axis="y", linestyle="--", alpha=0.5)

    st.pyplot(fig)  # ✅ Display in Streamlit

# ---- Function 4: Histogram (BMI Distribution) ----
def graph4(df):
    bmi_values = df["bmi"]

    fig, ax = plt.subplots(figsize=(9, 6))
    bins = np.arange(15, 55, 5)
    ax.hist(bmi_values, bins=bins, color='#4682B4', alpha=0.6, 
            edgecolor="black", linewidth=1.2, label="BMI Distribution")

    ax.axvline(25, color='darkorange', linestyle="dashed", linewidth=2.5, label="Overweight (BMI 25)")
    ax.axvline(30, color='red', linestyle="dashed", linewidth=2.5, label="Obese (BMI 30)")

    ax.set_xlabel("BMI", fontsize=13, fontweight='bold')
    ax.set_ylabel("Frequency", fontsize=13, fontweight='bold')
    ax.set_title("Histogram: Distribution of BMI", fontsize=15, fontweight='bold')
    ax.grid(axis='y', linestyle="--", alpha=0.5)
    ax.legend(fontsize=11, loc="upper right")

    st.pyplot(fig)  # ✅ Display in Streamlit

# ---- Function 5: Correlation Heatmap ----
def graph5(df):
    numerical_df = df.select_dtypes(include=[np.number])
    correlation_matrix = numerical_df.corr()

    fig, ax = plt.subplots(figsize=(8, 6))
    cax = ax.imshow(correlation_matrix, cmap="coolwarm", vmin=-1, vmax=1)
    fig.colorbar(cax, ax=ax)

    labels = numerical_df.columns
    ax.set_xticks(np.arange(len(labels)))
    ax.set_yticks(np.arange(len(labels)))
    ax.set_xticklabels(labels, fontsize=12, fontweight="bold", rotation=45, ha="right")
    ax.set_yticklabels(labels, fontsize=12, fontweight="bold")

    for i in range(len(labels)):
        for j in range(len(labels)):
            ax.text(j, i, f"{correlation_matrix.iloc[i, j]:.2f}", 
                    ha="center", va="center", color="black", fontsize=10)

    ax.set_title("Correlation Matrix of Numerical Variables", fontsize=14, fontweight='bold')

    st.pyplot(fig)  # ✅ Display in Streamlit

# ---- Function 6: Bar Chart (Average Charges by BMI Category) ----
def graph6():
    bmi_categories = ["Underweight", "Normal", "Overweight", "Obese"]
    charges = [8658, 10405, 11007, 15492]

    fig, ax = plt.subplots(figsize=(10, 6))
    bars = ax.bar(bmi_categories, charges, color=['navy', 'teal', 'seagreen', 'lightgreen'])

    for bar in bars:
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height(),
                f"{bar.get_height():,.0f}", ha='center', va='bottom', 
                fontsize=12, fontweight='bold', color='black')

    ax.set_xlabel("BMI Category", fontsize=14, fontweight='bold')
    ax.set_ylabel("Average Medical Charges", fontsize=14, fontweight='bold')
    ax.set_title("Average Medical Charges by BMI Category", fontsize=16, fontweight='bold')

    st.pyplot(fig)  # ✅ Display in Streamlit

# ---- Streamlit App ----
st.set_page_config(page_title="Insurance Analysis", page_icon="📊")

df = pd.read_csv("insurance_dataset_analysis/insurance.csv")

st.title("📊 Insurance Data Analysis")

st.write("### Scatter Plot: Charges vs Age (by Smoker Status)")
graph1(df)

st.write("### Box Plot: Insurance Charges by Region")
graph2(df)

st.write("### Bar Chart: Average Charges by Smoker & Sex")
graph3(df)

st.write("### Histogram: BMI Distribution")
graph4(df)

st.write("### Correlation Matrix of Numerical Variables")
graph5(df)

st.write("### Average Medical Charges by BMI Category")
graph6()
