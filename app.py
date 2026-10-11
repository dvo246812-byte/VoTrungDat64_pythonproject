
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Quan ly diem sinh vien",
    layout="wide"
)

st.title("QUAN LY DIEM SINH VIEN")

data = {
    "MSSV": [
        "SV001", "SV002", "SV003", "SV004", "SV005",
        "SV006", "SV007", "SV008", "SV009", "SV010"
    ],
    "Ho ten": [
        "An", "Binh", "Chi", "Dung", "Ha",
        "Hung", "Lan", "Minh", "Nam", "Phuong"
    ],
    "Chuyen can": [8, 9, 7, 10, 8, 6, 9, 7, 8, 10],
    "Giua ky": [7, 8, 6, 9, 7, 5, 8, 7, 6, 9],
    "Cuoi ky": [9, 8, 7, 10, 8, 6, 9, 8, 7, 10]
}

df = pd.DataFrame(data)

df["Tong ket"] = (
    0.2 * df["Chuyen can"]
    + 0.3 * df["Giua ky"]
    + 0.5 * df["Cuoi ky"]
)

def xep_loai(diem):
    if diem >= 8.5:
        return "Gioi"
    elif diem >= 7:
        return "Kha"
    elif diem >= 5:
        return "Trung binh"
    return "Yeu"

df["Xep loai"] = df["Tong ket"].apply(xep_loai)

st.subheader("1. Bang diem sinh vien")
st.dataframe(df, use_container_width=True)

st.subheader("2. Thong ke")

st.metric("Diem trung binh", f'{df["Tong ket"].mean():.2f}')
st.metric("So sinh vien dat", f'{(df["Tong ket"] >= 5).sum()}/10')

st.write("Sinh vien co diem cao nhat")
st.dataframe(df[df["Tong ket"] == df["Tong ket"].max()])

st.write("Sinh vien co diem thap nhat")
st.dataframe(df[df["Tong ket"] == df["Tong ket"].min()])

st.subheader("3. Tra cuu sinh vien")

ten = st.selectbox("Chon sinh vien", df["Ho ten"].tolist())
sv = df[df["Ho ten"] == ten].iloc[0]

st.write("MSSV:", sv["MSSV"])
st.write("Chuyen can:", sv["Chuyen can"])
st.write("Giua ky:", sv["Giua ky"])
st.write("Cuoi ky:", sv["Cuoi ky"])
st.write("Tong ket:", f'{sv["Tong ket"]:.2f}')
st.write("Xep loai:", sv["Xep loai"])

st.subheader("4. Bieu do diem tong ket")

fig, ax = plt.subplots(figsize=(10, 5))
ax.bar(df["Ho ten"], df["Tong ket"])
ax.set_xlabel("Ho ten sinh vien")
ax.set_ylabel("Diem tong ket")
ax.set_title("DIEM TONG KET CUA 10 SINH VIEN")
ax.set_ylim(0, 10)
plt.xticks(rotation=45)
fig.tight_layout()

st.pyplot(fig)
plt.close(fig)

st.divider()
st.caption("Nguoi tao: [Võ Trung Đạt] - MSSV: [060208003897]")
      
